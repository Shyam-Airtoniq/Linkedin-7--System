"""
CLI runner for the LinkedIn Complete System.
Run: uv run python run.py

Prompts for business details, generates all 11 sheets via Claude,
and saves the Excel file to outputs/
"""

import sys
from app.generator import LinkedInSystemGenerator
from app.excel_builder import ExcelBuilder


def main():
    print("\n" + "=" * 60)
    print("🚀  90-DAY LINKEDIN COMPLETE SYSTEM  ($199 Tier)")
    print("=" * 60)

    # ── Gather inputs ──
    print("\nPlease provide your business details:\n")

    business_name = input("Business Name: ").strip()
    if not business_name:
        business_name = "My Business"

    print("\nDescribe your services in detail (what you do, who you serve,")
    print("what makes you different). Press Enter twice when done:\n")
    lines = []
    while True:
        line = input()
        if line == "" and lines and lines[-1] == "":
            break
        lines.append(line)
    services = "\n".join(lines).strip()

    if len(services) < 20:
        print("❌  Please provide at least 20 characters describing your services.")
        sys.exit(1)

    target_industry = input("\nTarget Industry (optional, press Enter to skip): ").strip() or None

    print("\nLinkedIn Status:")
    print("  1. Starting from scratch")
    print("  2. Have some presence")
    print("  3. Established but inconsistent")
    status_choice = input("Choose (1/2/3): ").strip()
    status_map = {"1": "Starting from scratch", "2": "Have some presence", "3": "Established but inconsistent"}
    linkedin_status = status_map.get(status_choice, "Starting from scratch")

    additional_context = f"LinkedIn Status: {linkedin_status}"

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
