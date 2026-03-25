"""
FastAPI application – REST API for the LinkedIn COMPLETE SYSTEM ($199).

Same step-by-step API pattern as the starter kit, but with richer prompts
that generate significantly more content per sheet.
"""

import os
import io
import logging
import httpx
from datetime import datetime

from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from dotenv import load_dotenv

from app.generator import LinkedInSystemGenerator, call_claude, parse_json_response
from app.excel_builder import ExcelBuilder
from app.prompts import (
    STRATEGIC_ANALYSIS_PROMPT,
    DASHBOARD_PROMPT,
    PROFILE_OPTIMIZATION_PROMPT,
    CONTENT_CALENDAR_PROMPT,
    OUTREACH_SYSTEM_PROMPT,
    SALES_SYSTEM_PROMPT,
    LEAD_MAGNET_FUNNEL_PROMPT,
    CONTENT_ENGINE_PROMPT,
    IMPLEMENTATION_TIMELINE_PROMPT,
    RESULTS_TRACKER_PROMPT,
)

load_dotenv()

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(name)s  %(message)s",
)
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# FastAPI app
# ---------------------------------------------------------------------------
app = FastAPI(
    title="90-Day LinkedIn Complete System",
    description=(
        "Generate a customized 11-sheet LinkedIn COMPLETE SYSTEM using AI. "
        "Uses a step-by-step API pattern for serverless compatibility. "
        "This is the $199 tier with 3-5× more content than the free starter kit."
    ),
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------------------------
# Request / Response schemas
# ---------------------------------------------------------------------------
class BusinessInfo(BaseModel):
    """Common business details sent with every step."""
    business_name: str = Field(default="My Business")
    name: str = Field(default="")
    email: str = Field(default="")
    services: str = Field(..., min_length=20)
    target_industry: str | None = None
    additional_context: str | None = None


class AnalysisResponse(BaseModel):
    """Response from Step 1 – strategic analysis."""
    status: str
    step: int
    total_steps: int
    message: str
    analysis: dict


class SheetRequest(BaseModel):
    """Request body for generating an individual sheet."""
    business_name: str = Field(default="My Business")
    services: str = Field(..., min_length=20)
    analysis: dict = Field(..., description="The analysis object from Step 1")
    step_name: str = Field(..., description="Sheet to generate: dashboard|profile|content_calendar|outreach|sales|lead_magnet|content_engine|implementation|tracker")


class SheetResponse(BaseModel):
    """Response from an individual sheet generation."""
    status: str
    step: int
    total_steps: int
    step_name: str
    message: str
    data: dict


class BuildRequest(BaseModel):
    """Request to build the final Excel workbook."""
    business_name: str = Field(default="My Business")
    name: str = Field(default="")
    email: str = Field(default="")
    analysis: dict
    sheets: dict = Field(..., description="Dict of all generated sheet data keyed by step_name")


class HealthResponse(BaseModel):
    status: str
    timestamp: str
    version: str


# ---------------------------------------------------------------------------
# Webhook — POST Excel + metadata to n8n after generation
# ---------------------------------------------------------------------------
WEBHOOK_URL = os.getenv(
    "WEBHOOK_URL",
    "https://vmi2632825.contaboserver.net/webhook/b02fb702-2d5c-42c6-8469-80059737e99e",
)


async def _post_to_webhook(file_bytes: bytes, filename: str, name: str, email: str, business_name: str):
    """POST the generated Excel + user info to the n8n webhook."""
    try:
        async with httpx.AsyncClient(timeout=30) as client:
            files = {"file": (filename, file_bytes, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")}
            data = {"name": name, "email": email, "business_name": business_name}
            resp = await client.post(WEBHOOK_URL, files=files, data=data)
            logger.info("Webhook POST %s → %s", WEBHOOK_URL, resp.status_code)
    except Exception as exc:
        logger.warning("Webhook POST failed (non-blocking): %s", exc)


# ---------------------------------------------------------------------------
# Step metadata
# ---------------------------------------------------------------------------
SHEET_STEPS = [
    {"step": 2,  "name": "dashboard",        "label": "Master Dashboard",       "prompt": DASHBOARD_PROMPT},
    {"step": 3,  "name": "profile",          "label": "Profile Optimization",   "prompt": PROFILE_OPTIMIZATION_PROMPT},
    {"step": 4,  "name": "content_calendar", "label": "90-Day Content Calendar","prompt": CONTENT_CALENDAR_PROMPT},
    {"step": 5,  "name": "outreach",         "label": "Outreach System",        "prompt": OUTREACH_SYSTEM_PROMPT},
    {"step": 6,  "name": "sales",            "label": "Sales System",           "prompt": SALES_SYSTEM_PROMPT},
    {"step": 7,  "name": "lead_magnet",      "label": "Lead Magnet Funnel",     "prompt": LEAD_MAGNET_FUNNEL_PROMPT},
    {"step": 8,  "name": "content_engine",   "label": "Content Engine",         "prompt": CONTENT_ENGINE_PROMPT},
    {"step": 9,  "name": "implementation",   "label": "Implementation Timeline","prompt": IMPLEMENTATION_TIMELINE_PROMPT},
    {"step": 10, "name": "tracker",          "label": "Results Tracker",        "prompt": RESULTS_TRACKER_PROMPT},
]

STEP_MAP = {s["name"]: s for s in SHEET_STEPS}
TOTAL_STEPS = 11  # 1 analysis + 9 sheets + 1 build


# ---------------------------------------------------------------------------
# Helper: build context kwargs from analysis
# ---------------------------------------------------------------------------
def _build_context(business_name: str, services: str, analysis: dict) -> dict:
    """Build prompt context strings from the analysis data."""
    profiles = analysis.get("icp_profiles", [])
    icp_parts = []
    for p in profiles:
        icp_parts.append(
            f"{p.get('name', 'N/A')}: {p.get('title', 'N/A')} at {p.get('org', 'N/A')}, "
            f"Size: {p.get('size_metric', 'N/A')}, Volume: {p.get('volume_metric', 'N/A')}"
        )

    pillars = analysis.get("content_pillars", [])
    pillar_str = ", ".join(f"{p['name']} ({p['percentage']}%)" for p in pillars)

    pps = analysis.get("pain_points", [])
    pp_str = "\n".join(f"- {pp['pain']}: {pp['solution']}" for pp in pps)

    pricing = analysis.get("pricing", {})
    pricing_str = ", ".join(
        f"{pricing.get(k, {}).get('name', k)}: {pricing.get(k, {}).get('price_range', 'N/A')}"
        for k in ("tier1", "tier2", "tier3", "tier4")
    )

    return {
        "business_name": business_name,
        "services": services,
        "icp_summary": "; ".join(icp_parts) or "N/A",
        "positioning_statement": analysis.get("positioning", {}).get("statement", "N/A"),
        "content_pillars": pillar_str or "N/A",
        "pain_points_list": pp_str or "N/A",
        "pricing_tiers": pricing_str,
        "tier1_price": pricing.get("tier1", {}).get("price_range", "N/A"),
    }


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------
@app.get("/api/health", response_model=HealthResponse, tags=["System"])
async def health_check():
    return HealthResponse(
        status="healthy",
        timestamp=datetime.utcnow().isoformat(),
        version="1.0.0",
    )


@app.post("/api/generate/analysis", response_model=AnalysisResponse, tags=["Generator"])
async def generate_analysis(request: BusinessInfo):
    """
    **Step 1 of 11** — Run strategic analysis.
    Returns the core analysis (ICP, pricing, positioning, pain points, content pillars).
    This data is needed for all subsequent steps.
    """
    try:
        extra = ""
        if request.target_industry:
            extra += f"\nTarget Industry: {request.target_industry}"
        if request.additional_context:
            extra += f"\nAdditional Context: {request.additional_context}"

        prompt = STRATEGIC_ANALYSIS_PROMPT.format(
            business_details=f"{request.business_name}: {request.services}",
            additional_context=extra,
        )

        raw = call_claude(
            prompt,
            system_prompt="You are a LinkedIn growth strategist. Return ONLY valid JSON.",
        )
        analysis = parse_json_response(raw)

        return AnalysisResponse(
            status="success",
            step=1,
            total_steps=TOTAL_STEPS,
            message="Strategic analysis complete",
            analysis=analysis,
        )

    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))
    except Exception as exc:
        logger.exception("Analysis generation failed")
        raise HTTPException(status_code=500, detail=f"Analysis failed: {exc}")


@app.post("/api/generate/sheet", response_model=SheetResponse, tags=["Generator"])
async def generate_sheet(request: SheetRequest):
    """
    **Steps 2-10 of 11** — Generate an individual sheet.

    Pass `step_name` as one of:
    `dashboard`, `profile`, `content_calendar`, `outreach`, `sales`,
    `lead_magnet`, `content_engine`, `implementation`, `tracker`

    Each call takes ~15-30 seconds (longer for content-heavy sheets like content_calendar).
    """
    step_meta = STEP_MAP.get(request.step_name)
    if not step_meta:
        valid = ", ".join(STEP_MAP.keys())
        raise HTTPException(
            status_code=400,
            detail=f"Invalid step_name '{request.step_name}'. Valid: {valid}",
        )

    try:
        ctx = _build_context(request.business_name, request.services, request.analysis)
        prompt = step_meta["prompt"].format(**ctx)

        # Complete System prompts generate 3-5× more content — need higher token limit
        max_tokens = 32768

        raw = call_claude(
            prompt,
            system_prompt="You are a LinkedIn growth strategist. Return ONLY valid JSON.",
            max_tokens=max_tokens,
        )
        data = parse_json_response(raw)

        return SheetResponse(
            status="success",
            step=step_meta["step"],
            total_steps=TOTAL_STEPS,
            step_name=request.step_name,
            message=f"{step_meta['label']} generated",
            data=data,
        )

    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))
    except Exception as exc:
        logger.exception("Sheet generation failed: %s", request.step_name)
        raise HTTPException(
            status_code=500,
            detail=f"Sheet '{request.step_name}' failed: {exc}",
        )


@app.post("/api/generate/build", tags=["Generator"])
async def build_excel(request: BuildRequest):
    """
    **Step 11 of 11** — Build the final Excel workbook.

    Builds the Excel, POSTs it to the n8n webhook with name + email,
    then returns the file as a download.
    """
    try:
        builder = ExcelBuilder(business_name=request.business_name)
        builder.build_all(request.analysis, request.sheets)

        buffer = io.BytesIO()
        builder.wb.save(buffer)
        file_bytes = buffer.getvalue()

        safe_name = "".join(
            c if c.isalnum() or c in (" ", "_", "-") else "_"
            for c in request.business_name
        ).strip().replace(" ", "_").lower()
        filename = f"{safe_name}_90day_linkedin_complete_system.xlsx"

        # Save to outputs/ folder
        os.makedirs("outputs", exist_ok=True)
        output_path = os.path.join("outputs", filename)
        with open(output_path, "wb") as f:
            f.write(file_bytes)
        logger.info("Excel saved to %s", output_path)

        # POST to n8n webhook (non-blocking — doesn't fail the request if webhook is down)
        await _post_to_webhook(file_bytes, filename, request.name, request.email, request.business_name)

        # Return file to caller
        return StreamingResponse(
            io.BytesIO(file_bytes),
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={"Content-Disposition": f'attachment; filename="{filename}"'},
        )

    except Exception as exc:
        logger.exception("Excel build failed")
        raise HTTPException(status_code=500, detail=f"Excel build failed: {exc}")
