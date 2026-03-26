"""
CLI runner for the LinkedIn Complete System.
Run: uv run python run.py
Reads business details from environment variables (Docker-friendly).
Saves the Excel file to outputs/
"""
import sys
import os
import httpx
from app.generator import LinkedInSystemGenerator
from app.excel_builder import ExcelBuilder

WEBHOOK_URL = os.getenv(
    "WEBHOOK_URL",
    "https://vmi2632825.contaboserver.net/webhook/b02fb702-2d5c-42c6-8469-80059737e99e",
)


def post_to_webhook(filepath: str, name: str, email: str, business_name: str):
    """POST the generated Excel + user info to the n8n webhook."""
    try:
        with open(filepath, "rb") as f:
            file_bytes = f.read()
        filename = os.path.basename(filepath)
        files = {"file": (filename, file_bytes, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")}
        data = {"name": name, "email": email, "business_name": business_name}
        resp = httpx.post(WEBHOOK_URL, files=files, data=data, timeout=30)
        print(f"📤  Webhook POST → {resp.status_code}")
    except Exception as exc:
        print(f"⚠️  Webhook POST failed: {exc}")


def main():
    print("\n" + "=" * 60)
    print("🚀  90-DAY LINKEDIN COMPLETE SYSTEM  ($199 Tier)")
    print("=" * 60)
 
    # ── Gather inputs from env vars ──
    print("\nReading business details from environment variables...\n")
 
    business_name = os.getenv("BUSINESS_NAME", "").strip()
    if not business_name:
        business_name = "My Business"

    name = os.getenv("NAME", "").strip()
    email = os.getenv("EMAIL", "").strip()
 
    services = os.getenv("SERVICES", "").strip()
    if len(services) < 20:
        print("❌  SERVICES env var must be at least 20 characters.")
        print("    Set it in your .env file and rerun.")
        sys.exit(1)
 
    target_industry = os.getenv("TARGET_INDUSTRY", "").strip() or None
 
    status_choice = os.getenv("LINKEDIN_STATUS", "1").strip()
    status_map = {
        "1": "Starting from scratch",
        "2": "Have some presence",
        "3": "Established but inconsistent"
    }
    linkedin_status = status_map.get(status_choice, "Starting from scratch")
    additional_context = f"LinkedIn Status: {linkedin_status}"
 
    print(f"  Business Name    : {business_name}")
    print(f"  Name             : {name or 'Not specified'}")
    print(f"  Email            : {email or 'Not specified'}")
    print(f"  Target Industry  : {target_industry or 'Not specified'}")
    print(f"  LinkedIn Status  : {linkedin_status}")
    print(f"  Services Preview : {services[:80]}...")
 
    # ── Generate ──
    print("\n" + "-" * 60)
    print("⏳  Starting generation... This takes 3-5 minutes.")
    print("-" * 60 + "\n")
 
    generator = LinkedInSystemGenerator()
    generator.set_progress_callback(
        lambda step, total, msg: print(f"  [{step}/{total}] {msg}")
    )
 
    result = generator.generate(
        business_name=business_name,
        services=services,
        target_industry=target_industry,
        additional_context=additional_context,
    )
 
    # ── Build Excel ──
    print("\n📊  Building Excel workbook...")
    builder = ExcelBuilder(business_name=business_name)
    builder.build_all(result["analysis"], result["sheets"])
    filepath = builder.save()
 
    print("\n" + "=" * 60)
    print(f"✅  DONE! File saved to: {filepath}")
    print("=" * 60)

    # ── POST to webhook ──
    print("\n📤  Sending to webhook...")
    post_to_webhook(filepath, name, email, business_name)

    print("\nOpen the file in Excel to see your complete 11-sheet system.")
 
 
if __name__ == "__main__":
    main()