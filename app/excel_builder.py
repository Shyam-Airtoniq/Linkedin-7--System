"""
Excel workbook builder – assembles all 11 sheets for the COMPLETE SYSTEM.
Delegates each sheet to the modular builders in sheets_part1, sheets_part2, and sheets_part3.
"""

import os
import uuid
from datetime import datetime
from openpyxl import Workbook
from dotenv import load_dotenv

from app.sheets_part1 import (
    build_sheet0_strategic,
    build_sheet1_dashboard,
    build_sheet2_profile,
    build_sheet3_content_calendar,
    build_sheet4_outreach,
)
from app.sheets_part2 import (
    build_sheet5_sales,
    build_sheet6_lead_magnet,
    build_sheet7_content_engine,
    build_sheet8_implementation,
)
from app.sheets_part3 import (
    build_sheet9_results_tracker,
    build_sheet10_upgrade,
)

load_dotenv()


class ExcelBuilder:
    """Build the 11-sheet LinkedIn Complete System workbook."""

    def __init__(self, business_name: str, logo_path: str | None = None):
        self.business_name = business_name
        self.logo_path = logo_path or os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "assets", "ninegravity_logo.png"
        )
        self.wb = Workbook()
        if "Sheet" in self.wb.sheetnames:
            del self.wb["Sheet"]

    def build_all(self, analysis: dict, sheets: dict):
        """Build all 11 sheets from the analysis and sheet data."""
        build_sheet0_strategic(self.wb, analysis, self.business_name)
        build_sheet1_dashboard(self.wb, analysis, sheets.get("dashboard", {}), self.business_name)
        build_sheet2_profile(self.wb, sheets.get("profile", {}))
        build_sheet3_content_calendar(self.wb, sheets.get("content_calendar", {}))
        build_sheet4_outreach(self.wb, sheets.get("outreach", {}))
        build_sheet5_sales(self.wb, sheets.get("sales", {}))
        build_sheet6_lead_magnet(self.wb, sheets.get("lead_magnet", {}))
        build_sheet7_content_engine(self.wb, sheets.get("content_engine", {}))
        build_sheet8_implementation(self.wb, sheets.get("implementation", {}))
        build_sheet9_results_tracker(self.wb, sheets.get("tracker", {}))
        build_sheet10_upgrade(self.wb, self.logo_path)

    def save(self, output_dir: str | None = None) -> str:
        """Save the workbook and return the file path."""
        output_dir = output_dir or os.getenv("OUTPUT_DIR", "outputs")
        os.makedirs(output_dir, exist_ok=True)

        safe_name = "".join(c if c.isalnum() or c in (" ", "_", "-") else "_"
                           for c in self.business_name).strip().replace(" ", "_").lower()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_id = uuid.uuid4().hex[:8]
        filename = f"{safe_name}_90day_linkedin_complete_system_{timestamp}_{file_id}.xlsx"
        filepath = os.path.join(output_dir, filename)

        self.wb.save(filepath)
        return filepath
