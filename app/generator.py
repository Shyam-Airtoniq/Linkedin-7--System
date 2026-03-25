"""
Core generation logic for the LinkedIn System Generator.
Handles Anthropic API calls and content orchestration.
"""

import os
import json
import time
import logging
from typing import Optional
from anthropic import Anthropic
from dotenv import load_dotenv

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

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Anthropic API wrapper
# ---------------------------------------------------------------------------

MAX_RETRIES = int(os.getenv("MAX_RETRIES", "3"))
API_TIMEOUT = int(os.getenv("API_TIMEOUT", "120"))


def _get_client() -> Anthropic:
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key or api_key == "your_api_key_here":
        raise ValueError(
            "ANTHROPIC_API_KEY is not set. Please add it to your .env file."
        )
    return Anthropic(api_key=api_key)


def call_claude(
    prompt: str,
    system_prompt: Optional[str] = None,
    max_tokens: int = 32768,
) -> str:
    """Call the Anthropic API with streaming + retry logic.
    
    Uses streaming because Anthropic requires it for high max_tokens values.
    """
    client = _get_client()

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            kwargs: dict = {
                "model": "claude-sonnet-4-6",
                "max_tokens": max_tokens,
                "messages": [{"role": "user", "content": prompt}],
            }
            if system_prompt:
                kwargs["system"] = system_prompt

            # Use streaming to handle large token counts
            collected_text = []
            with client.messages.stream(**kwargs) as stream:
                for text in stream.text_stream:
                    collected_text.append(text)

            return "".join(collected_text)

        except Exception as exc:
            logger.warning(
                "Anthropic API call attempt %d/%d failed: %s",
                attempt,
                MAX_RETRIES,
                exc,
            )
            if attempt == MAX_RETRIES:
                raise
            time.sleep(2**attempt)  # exponential back-off

    return ""  # unreachable, keeps type-checker happy


def parse_json_response(text: str) -> dict:
    """Parse JSON from Claude response, stripping markdown fences if present.
    
    Handles common Claude issues:
    - ```json ... ``` wrappers
    - Unescaped control characters inside JSON strings (newlines, tabs)
    """
    import re

    cleaned = text.strip()

    # Strip ```json ... ``` wrappers
    if cleaned.startswith("```"):
        first_newline = cleaned.index("\n")
        cleaned = cleaned[first_newline + 1 :]
    if cleaned.endswith("```"):
        cleaned = cleaned[:-3]

    cleaned = cleaned.strip()

    # First try: strict=False tolerates control chars in many Python versions
    try:
        return json.loads(cleaned, strict=False)
    except json.JSONDecodeError:
        pass

    # Second try: sanitize control characters inside JSON string values
    # Replace raw control chars (except \n \r \t which we escape properly)
    def _sanitize(s: str) -> str:
        # Replace literal control chars that aren't already escaped
        s = s.replace('\r\n', '\\n').replace('\r', '\\n').replace('\t', '\\t')
        # Remove any remaining control chars (0x00-0x1F) except already-escaped ones
        s = re.sub(r'(?<!\\)[\x00-\x08\x0b\x0c\x0e-\x1f]', '', s)
        # Fix unescaped newlines inside JSON strings
        # This regex finds strings and escapes newlines within them
        s = re.sub(r'(?<=": ")(.*?)(?="[,}\]])', lambda m: m.group(0).replace('\n', '\\n'), s, flags=re.DOTALL)
        return s

    try:
        sanitized = _sanitize(cleaned)
        return json.loads(sanitized, strict=False)
    except json.JSONDecodeError as exc:
        logger.error("Failed to parse JSON from Claude response: %s", exc)
        logger.debug("Raw response:\n%s", text[:500])
        raise ValueError(f"Could not parse Claude response as JSON: {exc}") from exc


# ---------------------------------------------------------------------------
# LinkedIn System Generator
# ---------------------------------------------------------------------------


class LinkedInSystemGenerator:
    """Orchestrates the full generation pipeline."""

    def __init__(self):
        self.analysis: dict = {}
        self.sheet_data: dict = {}
        self._progress_callback = None

    def set_progress_callback(self, callback):
        """Set a callback function for progress updates: callback(step, total, message)"""
        self._progress_callback = callback

    def _report_progress(self, step: int, total: int, message: str):
        if self._progress_callback:
            self._progress_callback(step, total, message)
        logger.info("Progress [%d/%d]: %s", step, total, message)

    # -- helpers to build prompt context strings --
    def _icp_summary(self) -> str:
        profiles = self.analysis.get("icp_profiles", [])
        parts = []
        for p in profiles:
            parts.append(
                f"{p.get('name', 'N/A')}: {p.get('title', 'N/A')} at {p.get('org', 'N/A')}, "
                f"Size: {p.get('size_metric', 'N/A')}, Volume: {p.get('volume_metric', 'N/A')}"
            )
        return "; ".join(parts) if parts else "N/A"

    def _positioning_statement(self) -> str:
        return self.analysis.get("positioning", {}).get("statement", "N/A")

    def _content_pillars_str(self) -> str:
        pillars = self.analysis.get("content_pillars", [])
        parts = [f"{p['name']} ({p['percentage']}%)" for p in pillars]
        return ", ".join(parts) if parts else "N/A"

    def _pain_points_list(self) -> str:
        pps = self.analysis.get("pain_points", [])
        return "\n".join(f"- {pp['pain']}: {pp['solution']}" for pp in pps) or "N/A"

    def _pricing_tiers_str(self) -> str:
        p = self.analysis.get("pricing", {})
        parts = []
        for tier_key in ("tier1", "tier2", "tier3", "tier4"):
            tier = p.get(tier_key, {})
            parts.append(
                f"{tier.get('name', tier_key)}: {tier.get('price_range', 'N/A')}"
            )
        return ", ".join(parts)

    def _tier1_price(self) -> str:
        return (
            self.analysis.get("pricing", {})
            .get("tier1", {})
            .get("price_range", "N/A")
        )

    # ------------------------------------------------------------------
    # Step 1: Strategic Analysis (Sheet 0)
    # ------------------------------------------------------------------
    def run_strategic_analysis(
        self,
        business_name: str,
        services: str,
        target_industry: Optional[str] = None,
        additional_context: Optional[str] = None,
    ) -> dict:
        self._report_progress(1, 10, "🔍 Running strategic analysis…")

        extra = ""
        if target_industry:
            extra += f"\nTarget Industry: {target_industry}"
        if additional_context:
            extra += f"\nAdditional Context: {additional_context}"

        prompt = STRATEGIC_ANALYSIS_PROMPT.format(
            business_details=f"{business_name}: {services}",
            additional_context=extra,
        )

        raw = call_claude(
            prompt,
            system_prompt="You are a LinkedIn growth strategist. Return ONLY valid JSON.",
        )
        self.analysis = parse_json_response(raw)
        return self.analysis

    # ------------------------------------------------------------------
    # Steps 2-10: Individual Sheet Generation
    # ------------------------------------------------------------------
    def _generate_sheet(
        self,
        step: int,
        sheet_name: str,
        prompt_template: str,
        format_kwargs: dict,
    ) -> dict:
        self._report_progress(step, 10, f"📝 Generating {sheet_name}…")
        prompt = prompt_template.format(**format_kwargs)
        raw = call_claude(
            prompt,
            system_prompt="You are a LinkedIn growth strategist. Return ONLY valid JSON.",
        )
        data = parse_json_response(raw)
        self.sheet_data[sheet_name] = data
        return data

    def _common_kwargs(self, business_name: str, services: str) -> dict:
        return {
            "business_name": business_name,
            "services": services,
            "icp_summary": self._icp_summary(),
            "positioning_statement": self._positioning_statement(),
            "content_pillars": self._content_pillars_str(),
            "pain_points_list": self._pain_points_list(),
            "pricing_tiers": self._pricing_tiers_str(),
            "tier1_price": self._tier1_price(),
        }

    def generate_all_sheets(self, business_name: str, services: str) -> dict:
        """Generate data for all 9 AI-generated sheets sequentially.
        Sheet 10 (Upgrade Path) is static and handled by ExcelBuilder.
        """
        kw = self._common_kwargs(business_name, services)

        sheet_configs = [
            (2,  "dashboard",       DASHBOARD_PROMPT),
            (3,  "profile",         PROFILE_OPTIMIZATION_PROMPT),
            (4,  "content_calendar", CONTENT_CALENDAR_PROMPT),
            (5,  "outreach",        OUTREACH_SYSTEM_PROMPT),
            (6,  "sales",           SALES_SYSTEM_PROMPT),
            (7,  "lead_magnet",     LEAD_MAGNET_FUNNEL_PROMPT),
            (8,  "content_engine",  CONTENT_ENGINE_PROMPT),
            (9,  "implementation",  IMPLEMENTATION_TIMELINE_PROMPT),
            (10, "tracker",         RESULTS_TRACKER_PROMPT),
        ]

        for step, name, tmpl in sheet_configs:
            self._generate_sheet(step, name, tmpl, kw)

        return self.sheet_data

    # ------------------------------------------------------------------
    # Full pipeline
    # ------------------------------------------------------------------
    def generate(
        self,
        business_name: str,
        services: str,
        target_industry: Optional[str] = None,
        additional_context: Optional[str] = None,
    ) -> dict:
        """Run the full generation pipeline and return all data."""
        self.run_strategic_analysis(
            business_name, services, target_industry, additional_context
        )
        self.generate_all_sheets(business_name, services)

        return {
            "analysis": self.analysis,
            "sheets": self.sheet_data,
        }
