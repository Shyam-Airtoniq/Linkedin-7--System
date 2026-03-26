"""
CLI runner for the LinkedIn Complete System.
Run: uv run python run.py
Reads business details from environment variables (Docker-friendly).
Saves the Excel file to outputs/
"""
import sys
import os
from app.generator import LinkedInSystemGenerator
from app.excel_builder import ExcelBuilder
 
 
def main():
    print("\n" + "=" * 60)
    print("🚀  90-DAY LINKEDIN COMPLETE SYSTEM  ($199 Tier)")
    print("=" * 60)
 
    # ── Gather inputs from env vars ──
    print("\nReading business details from environment variables...\n")
 
    business_name = os.getenv("BUSINESS_NAME", "").strip()
    if not business_name:
        business_name = "My Business"
 
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
    print("\nOpen the file in Excel to see your complete 11-sheet system.")
 
 
if __name__ == "__main__":
    main()