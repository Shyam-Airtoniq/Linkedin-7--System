"""Sheet builders for Sheets 5-8 of the LinkedIn COMPLETE SYSTEM."""
from templates.excel_template import (
    FILLS, FONTS, ALIGN_LEFT, ALIGN_CENTER, ALIGN_LEFT_CENTER,
    style_cell, style_range, style_merged_block, set_column_widths,
)


def build_sheet5_sales(wb, sales_data):
    """Sheet 5: Sales System — EXPANDED (complete discovery script, 15 objections, meeting templates, value calc)."""
    ws = wb.create_sheet("5. Sales System")
    set_column_widths(ws, {"A": 3, "B": 28, "C": 16, "D": 13, "E": 13, "F": 13, "G": 13, "H": 33})

    style_range(ws, 1, 2, 8,
        "PHASE 4: SALES SYSTEM  |  Days 36–50  |  Complete System",
        FONTS["title_14_white"], FILLS["dark_navy"], ALIGN_LEFT_CENTER)

    # 3-Tier Packaging
    style_range(ws, 3, 2, 8, "💰  3-TIER SERVICE PACKAGING",
        FONTS["section_12_white"], FILLS["dark_navy"], ALIGN_LEFT_CENTER)
    tiers = sales_data.get("service_tiers", [])
    tier_colors = ["medium_blue", "orange", "dark_green"]
    tier_bg = ["light_blue_bg", "light_green_bg", "light_yellow_bg"]
    r = 4
    style_cell(ws, r, 2, "", FONTS["body_9"], FILLS["white"], ALIGN_LEFT)
    for i, t in enumerate(tiers[:3]):
        col = 4 + i * 2
        style_range(ws, r, col, col + 1 if i < 2 else col, t.get("name", ""),
            FONTS["body_9_white"], FILLS[tier_colors[i]], ALIGN_CENTER)
    fields = ["price", "delivery", "included", "best_for", "guarantee"]
    labels = ["Price", "Delivery", "What's Included", "Best For", "Guarantee"]
    r = 5
    for fi, field in enumerate(fields):
        style_cell(ws, r, 2, labels[fi], FONTS["body_9_bold_navy"], FILLS["off_white"], ALIGN_LEFT)
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
        for i, t in enumerate(tiers[:3]):
            col = 4 + i * 2
            style_cell(ws, r, col, t.get(field, ""), FONTS["body_9"], FILLS[tier_bg[i]], ALIGN_LEFT)
            if i < 2:
                ws.merge_cells(start_row=r, start_column=col, end_row=r, end_column=col + 1)
        r += 1

    # Complete Discovery Call Script
    r += 1
    script = sales_data.get("discovery_script", {})
    style_range(ws, r, 2, 8, "📞  COMPLETE DISCOVERY CALL SCRIPT (Word-for-Word)",
        FONTS["section_12_white"], FILLS["medium_blue"], ALIGN_LEFT_CENTER)
    r += 1
    stages = [
        ("🟢 OPENING", "opening"),
        ("🔍 DIAGNOSIS", "diagnosis"),
        ("💊 PRESCRIPTION", "prescription"),
        ("🤝 CLOSE", "close"),
    ]
    stage_fills = ["light_blue_bg", "light_green_bg", "light_orange_bg", "light_purple_bg"]
    for si, (label, key) in enumerate(stages):
        stage = script.get(key, {})
        style_range(ws, r, 2, 8,
            f"{label} ({stage.get('duration', '')})",
            FONTS["subsection_10_white"], FILLS["medium_blue"], ALIGN_LEFT_CENTER)
        r += 1
        style_merged_block(ws, r, r + 3, 2, 8, stage.get("script", ""),
            FONTS["body_9"], FILLS[stage_fills[si]], ALIGN_LEFT)
        r += 5
        # Discovery questions in diagnosis
        if key == "diagnosis":
            for qi, q in enumerate(stage.get("questions", [])):
                fill = FILLS["light_green_bg"] if qi % 2 == 0 else FILLS["white"]
                style_cell(ws, r, 2, f"Q{qi+1}", FONTS["body_10_bold_green"], fill, ALIGN_CENTER)
                style_range(ws, r, 3, 8, q, FONTS["body_9"], fill, ALIGN_LEFT)
                r += 1
            r += 1
        if key == "close":
            ns = stage.get("next_steps", "")
            if ns:
                style_range(ws, r, 2, 8, f"Next Steps: {ns}",
                    FONTS["body_9"], FILLS["light_purple_bg"], ALIGN_LEFT)
                r += 1

    # 15 Objections
    r += 1
    style_range(ws, r, 2, 8, "🛡️  15 OBJECTION RESPONSE SCRIPTS",
        FONTS["section_12_white"], FILLS["dark_red"], ALIGN_LEFT_CENTER)
    r += 1
    for i, obj in enumerate(sales_data.get("objections", [])):
        style_range(ws, r, 2, 8, f"#{i+1}: \"{obj.get('objection', '')}\"",
            FONTS["body_9_bold_red"], FILLS["light_red_bg"], ALIGN_LEFT)
        r += 1
        style_merged_block(ws, r, r + 1, 2, 8, obj.get("response", ""),
            FONTS["body_9"], FILLS["light_green_bg"], ALIGN_LEFT)
        r += 3

    # Meeting Templates
    r += 1
    style_range(ws, r, 2, 8, "📧  3 MEETING BOOKING TEMPLATES",
        FONTS["section_12_white"], FILLS["dark_navy"], ALIGN_LEFT_CENTER)
    r += 1
    for mt in sales_data.get("meeting_templates", []):
        style_range(ws, r, 2, 8, mt.get("name", ""),
            FONTS["body_9_bold_navy"], FILLS["light_yellow_bg"], ALIGN_LEFT)
        r += 1
        style_cell(ws, r, 2, f"Subject: {mt.get('subject', '')}",
            FONTS["body_9_bold_orange"], FILLS["white"], ALIGN_LEFT)
        style_range(ws, r, 3, 8, mt.get("body", ""),
            FONTS["body_9"], FILLS["white"], ALIGN_LEFT)
        r += 1
        style_range(ws, r, 2, 8, f"📎 {mt.get('calendar_link_note', '')}",
            FONTS["small_8_grey"], FILLS["off_white"], ALIGN_LEFT)
        r += 2

    # Value Calculator
    r += 1
    vc = sales_data.get("value_calculator", {})
    style_range(ws, r, 2, 8, "🧮  VALUE CALCULATOR TOOL",
        FONTS["section_12_white"], FILLS["dark_green"], ALIGN_LEFT_CENTER)
    r += 1
    for ci in vc.get("current_cost_items", []):
        fill = FILLS["light_green_bg"]
        style_cell(ws, r, 2, ci.get("item", ""), FONTS["body_9"], fill, ALIGN_LEFT)
        style_range(ws, r, 3, 8, ci.get("typical_range", ""),
            FONTS["body_9_bold_green"], fill, ALIGN_LEFT)
        r += 1
    r += 1
    style_range(ws, r, 2, 8, f"ROI Formula: {vc.get('roi_formula', '')}",
        FONTS["body_9_bold_navy"], FILLS["light_green_bg"], ALIGN_LEFT)
    r += 1
    for tp in vc.get("talking_points", []):
        style_range(ws, r, 2, 8, f"→ {tp}",
            FONTS["body_9"], FILLS["white"], ALIGN_LEFT)
        r += 1


def build_sheet6_lead_magnet(wb, lead_data):
    """Sheet 6: Lead Magnet Funnel — EXPANDED (10 formats, 5 landing pages, 7 emails)."""
    ws = wb.create_sheet("6. Lead Magnet Funnel")
    set_column_widths(ws, {"A": 3, "B": 28, "C": 16, "D": 13, "E": 13, "F": 13, "G": 13, "H": 18})

    style_range(ws, 1, 2, 8,
        "PHASE 5: LEAD MAGNET FUNNEL  |  Days 51–65  |  Complete System",
        FONTS["title_14_white"], FILLS["dark_navy"], ALIGN_LEFT_CENTER)

    # 10 Lead Magnet Formats
    style_range(ws, 3, 2, 8, "🧲  10 PROVEN LEAD MAGNET FORMATS",
        FONTS["section_12_white"], FILLS["dark_navy"], ALIGN_LEFT_CENTER)
    r = 4
    headers = ["#", "Format", "Description", "Type", "Value", "Difficulty", "Conv. Rate"]
    for j, h in enumerate(headers):
        style_cell(ws, r, 2 + j, h, FONTS["small_8_white"], FILLS["medium_blue"], ALIGN_LEFT)
    r += 1
    for i, fmt in enumerate(lead_data.get("lead_magnet_formats", [])):
        fill = FILLS["light_blue_bg"] if i % 2 == 0 else FILLS["white"]
        style_cell(ws, r, 2, str(fmt.get("number", i+1)), FONTS["body_9_bold_navy"], fill, ALIGN_CENTER)
        style_cell(ws, r, 3, fmt.get("name", ""), FONTS["body_9_bold_navy"], fill, ALIGN_LEFT)
        style_cell(ws, r, 4, fmt.get("description", ""), FONTS["small_8"], fill, ALIGN_LEFT)
        style_cell(ws, r, 5, fmt.get("format_type", ""), FONTS["small_8"], fill, ALIGN_CENTER)
        style_cell(ws, r, 6, fmt.get("estimated_value", ""), FONTS["body_9_bold_green"], fill, ALIGN_CENTER)
        style_cell(ws, r, 7, fmt.get("difficulty", ""), FONTS["small_8"], fill, ALIGN_CENTER)
        style_cell(ws, r, 8, fmt.get("conversion_rate", ""), FONTS["body_9_bold_orange"], fill, ALIGN_CENTER)
        r += 1

    # 5 Landing Pages
    r += 1
    style_range(ws, r, 2, 8, "📄  5 CONVERSION-OPTIMIZED LANDING PAGE OUTLINES",
        FONTS["section_12_white"], FILLS["purple"], ALIGN_LEFT_CENTER)
    r += 1
    for i, lp in enumerate(lead_data.get("landing_pages", [])):
        style_range(ws, r, 2, 8, lp.get("name", f"Landing Page {i+1}"),
            FONTS["body_9_bold_purple"], FILLS["light_purple_bg"], ALIGN_LEFT)
        r += 1
        pairs = [
            ("Headline", lp.get("headline", "")),
            ("Sub-headline", lp.get("sub_headline", "")),
            ("Bullet Points", lp.get("bullet_points", "")),
            ("Social Proof", lp.get("social_proof", "")),
            ("CTA Button", lp.get("cta_button", "")),
            ("Post-CTA", lp.get("post_cta", "")),
            ("Urgency", lp.get("urgency_element", "")),
        ]
        for label, val in pairs:
            fill = FILLS["white"]
            style_cell(ws, r, 2, label, FONTS["body_9_bold_navy"], fill, ALIGN_LEFT)
            style_range(ws, r, 3, 8, val, FONTS["body_9"], fill, ALIGN_LEFT)
            r += 1
        r += 1

    # 7-Email Welcome Sequence
    r += 1
    style_range(ws, r, 2, 8, "📧  7-EMAIL WELCOME SEQUENCE",
        FONTS["section_12_white"], FILLS["dark_navy"], ALIGN_LEFT_CENTER)
    r += 1
    for i, em in enumerate(lead_data.get("email_sequence", [])):
        fill = FILLS["light_yellow_bg"] if i % 2 == 0 else FILLS["white"]
        style_cell(ws, r, 2, em.get("label", ""),
            FONTS["body_9_bold_navy"], fill, ALIGN_LEFT)
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
        style_cell(ws, r, 4, f"Subject: {em.get('subject', '')}",
            FONTS["body_9_bold_orange"], fill, ALIGN_LEFT)
        ws.merge_cells(start_row=r, start_column=4, end_row=r, end_column=5)
        style_range(ws, r, 6, 8, em.get("body", ""),
            FONTS["body_9"], fill, ALIGN_LEFT)
        r += 1
        style_range(ws, r, 2, 8, f"Goal: {em.get('goal', '')}",
            FONTS["small_8_grey"], FILLS["off_white"], ALIGN_LEFT)
        r += 1

    # Ad Targeting
    r += 1
    ad = lead_data.get("ad_targeting", {})
    style_range(ws, r, 2, 8, "🎯  AD TARGETING PARAMETERS",
        FONTS["section_12_white"], FILLS["medium_blue"], ALIGN_LEFT_CENTER)
    r += 1
    for key in ["job_titles", "industries", "company_types", "company_size", "geography", "additional_signal"]:
        label = key.replace("_", " ").title()
        style_cell(ws, r, 2, label, FONTS["body_9_bold_navy"], FILLS["light_blue_bg"], ALIGN_LEFT)
        style_range(ws, r, 3, 8, ad.get(key, ""), FONTS["body_9"], FILLS["light_blue_bg"], ALIGN_LEFT)
        r += 1

    # Distribution Plan
    r += 1
    style_range(ws, r, 2, 8, "📢  DISTRIBUTION PLAN",
        FONTS["section_12_white"], FILLS["orange"], ALIGN_LEFT_CENTER)
    r += 1
    for dp in lead_data.get("distribution_plan", []):
        fill = FILLS["light_orange_bg"]
        style_cell(ws, r, 2, dp.get("channel", ""), FONTS["body_9_bold_navy"], fill, ALIGN_LEFT)
        style_range(ws, r, 3, 6, dp.get("action", ""), FONTS["body_9"], fill, ALIGN_LEFT)
        style_range(ws, r, 7, 8, dp.get("frequency", ""), FONTS["small_8"], fill, ALIGN_CENTER)
        r += 1


def build_sheet7_content_engine(wb, engine_data):
    """Sheet 7: 90-Day Content Engine — EXPANDED (30 topics, engagement strategy)."""
    ws = wb.create_sheet("7. Content Engine")
    set_column_widths(ws, {"A": 3, "B": 6, "C": 16, "D": 40, "E": 16, "F": 16, "G": 16})

    style_range(ws, 1, 2, 7,
        "PHASE 6: 90-DAY CONTENT ENGINE  |  Days 66–80  |  Complete System",
        FONTS["title_14_white"], FILLS["dark_navy"], ALIGN_LEFT_CENTER)

    # Research Methods
    style_range(ws, 3, 2, 7, "🔬  CONTENT RESEARCH METHODS",
        FONTS["section_12_white"], FILLS["dark_navy"], ALIGN_LEFT_CENTER)
    r = 4
    for i, rm in enumerate(engine_data.get("research_methods", [])):
        fill = FILLS["light_blue_bg"] if i % 2 == 0 else FILLS["white"]
        style_cell(ws, r, 2, rm.get("source", ""),
            FONTS["body_9_bold_navy"], fill, ALIGN_LEFT)
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
        style_range(ws, r, 4, 7, rm.get("instruction", ""),
            FONTS["body_9"], fill, ALIGN_LEFT)
        r += 1

    # 30 Content Topics
    r += 1
    style_range(ws, r, 2, 7, "📋  30 PRE-RESEARCHED CONTENT TOPICS",
        FONTS["section_12_white"], FILLS["medium_blue"], ALIGN_LEFT_CENTER)
    r += 1
    headers = ["#", "Pillar", "Topic / Hook", "Format", "Goal"]
    col_starts = [2, 3, 4, 6, 7]
    for j, h in enumerate(headers):
        style_cell(ws, r, col_starts[j], h, FONTS["small_8_white"], FILLS["dark_navy"], ALIGN_LEFT)
    r += 1
    pillar_fill = {"Education": "medium_blue", "Proof": "dark_green", "Engagement": "orange"}
    for i, t in enumerate(engine_data.get("content_topics", [])):
        fill = FILLS["off_white"] if i % 2 == 0 else FILLS["white"]
        style_cell(ws, r, 2, str(t.get("number", i+1)), FONTS["body_9"], fill, ALIGN_CENTER)
        pname = t.get("pillar", "Education")
        pfill = pillar_fill.get(pname, "medium_blue")
        style_cell(ws, r, 3, pname, FONTS["small_8_white"], FILLS[pfill], ALIGN_CENTER)
        style_range(ws, r, 4, 5, t.get("topic", ""), FONTS["small_8"], fill, ALIGN_LEFT)
        style_cell(ws, r, 6, t.get("format", ""), FONTS["small_8"], fill, ALIGN_CENTER)
        style_cell(ws, r, 7, t.get("goal", ""), FONTS["small_8"], fill, ALIGN_CENTER)
        r += 1

    # Production Workflow
    r += 1
    style_range(ws, r, 2, 7, "⚙️  WEEKLY PRODUCTION WORKFLOW",
        FONTS["section_12_white"], FILLS["purple"], ALIGN_LEFT_CENTER)
    r += 1
    for i, step in enumerate(engine_data.get("production_workflow", [])):
        fill = FILLS["light_purple_bg"] if i % 2 == 0 else FILLS["white"]
        style_cell(ws, r, 2, step.get("step", ""),
            FONTS["body_9_bold_purple"], fill, ALIGN_LEFT)
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
        style_cell(ws, r, 4, step.get("day", ""), FONTS["body_9"], fill, ALIGN_LEFT)
        style_cell(ws, r, 5, step.get("time", ""), FONTS["body_9_bold_navy"], fill, ALIGN_CENTER)
        style_range(ws, r, 6, 7, step.get("action", ""), FONTS["small_8"], fill, ALIGN_LEFT)
        r += 1

    # Engagement Strategy
    r += 1
    eng = engine_data.get("engagement_strategy", {})
    style_range(ws, r, 2, 7, "🤝  DAILY ENGAGEMENT STRATEGY",
        FONTS["section_12_white"], FILLS["dark_green"], ALIGN_LEFT_CENTER)
    r += 1
    for dr in eng.get("daily_routine", []):
        fill = FILLS["light_green_bg"]
        style_cell(ws, r, 2, dr.get("time", ""), FONTS["body_9_bold_navy"], fill, ALIGN_LEFT)
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
        style_range(ws, r, 4, 7, dr.get("action", ""), FONTS["body_9"], fill, ALIGN_LEFT)
        r += 1
    r += 1
    style_range(ws, r, 2, 7, "💬  Comment Templates",
        FONTS["body_9_bold_green"], FILLS["light_green_bg"], ALIGN_LEFT)
    r += 1
    for ct in eng.get("comment_templates", []):
        style_range(ws, r, 2, 7, f"→ {ct}", FONTS["body_9"], FILLS["white"], ALIGN_LEFT)
        r += 1
    r += 1
    style_range(ws, r, 2, 7, "🎯  Engagement Targets",
        FONTS["body_9_bold_green"], FILLS["light_green_bg"], ALIGN_LEFT)
    r += 1
    for et in eng.get("engagement_targets", []):
        style_range(ws, r, 2, 7, f"→ {et}", FONTS["body_9"], FILLS["white"], ALIGN_LEFT)
        r += 1


def build_sheet8_implementation(wb, impl_data):
    """Sheet 8: Implementation Timeline — EXPANDED (day-by-day 90-day plan)."""
    ws = wb.create_sheet("8. Implementation Timeline")
    set_column_widths(ws, {"A": 3, "B": 12, "C": 24, "D": 50, "E": 12, "F": 8.3})

    style_range(ws, 1, 2, 5,
        "PHASE 7: FULL 90-DAY IMPLEMENTATION TIMELINE  |  Complete System",
        FONTS["title_14_white"], FILLS["dark_navy"], ALIGN_LEFT_CENTER)

    # Day-by-day weeks
    r = 3
    week_keys = ["week1_days", "week2_days", "week3_days", "week4_days"]
    week_labels = ["WEEK 1 (Days 1–7)", "WEEK 2 (Days 8–14)", "WEEK 3 (Days 15–21)", "WEEK 4 (Days 22–28)"]
    week_colors = ["medium_blue", "dark_green", "orange", "purple"]

    for wi, (wkey, wlabel) in enumerate(zip(week_keys, week_labels)):
        style_range(ws, r, 2, 5, f"📅  {wlabel}",
            FONTS["section_12_white"], FILLS[week_colors[wi]], ALIGN_LEFT_CENTER)
        r += 1
        headers = ["Day", "Focus", "Actions", "Time"]
        for j, h in enumerate(headers):
            style_cell(ws, r, 2 + j, h, FONTS["small_8_white"], FILLS["dark_navy"], ALIGN_LEFT)
        r += 1
        for i, day in enumerate(impl_data.get(wkey, [])):
            fill = FILLS["off_white"] if i % 2 == 0 else FILLS["white"]
            style_cell(ws, r, 2, day.get("day", ""), FONTS["body_9_bold_navy"], fill, ALIGN_LEFT)
            style_cell(ws, r, 3, day.get("focus", ""), FONTS["body_9_bold_navy"], fill, ALIGN_LEFT)
            style_cell(ws, r, 4, day.get("actions", ""), FONTS["small_8"], fill, ALIGN_LEFT)
            style_cell(ws, r, 5, day.get("time", ""), FONTS["body_9"], fill, ALIGN_CENTER)
            r += 1
        r += 1

    # Month 2 (weekly)
    style_range(ws, r, 2, 5, "📅  MONTH 2 (Days 29–56) — Weekly Plans",
        FONTS["section_12_white"], FILLS["dark_navy"], ALIGN_LEFT_CENTER)
    r += 1
    for i, wk in enumerate(impl_data.get("month2_weeks", [])):
        fill = FILLS["light_blue_bg"] if i % 2 == 0 else FILLS["white"]
        style_cell(ws, r, 2, wk.get("week", ""), FONTS["body_9_bold_navy"], fill, ALIGN_LEFT)
        style_cell(ws, r, 3, wk.get("theme", ""), FONTS["body_9_bold_orange"], fill, ALIGN_LEFT)
        style_cell(ws, r, 4, wk.get("daily_actions", ""), FONTS["small_8"], fill, ALIGN_LEFT)
        style_cell(ws, r, 5, wk.get("key_milestone", ""), FONTS["small_8_grey"], fill, ALIGN_LEFT)
        r += 1

    # Month 3 (weekly)
    r += 1
    style_range(ws, r, 2, 5, "📅  MONTH 3 (Days 57–90) — Weekly Plans",
        FONTS["section_12_white"], FILLS["dark_navy"], ALIGN_LEFT_CENTER)
    r += 1
    for i, wk in enumerate(impl_data.get("month3_weeks", [])):
        fill = FILLS["light_green_bg"] if i % 2 == 0 else FILLS["white"]
        style_cell(ws, r, 2, wk.get("week", ""), FONTS["body_9_bold_navy"], fill, ALIGN_LEFT)
        style_cell(ws, r, 3, wk.get("theme", ""), FONTS["body_9_bold_green"], fill, ALIGN_LEFT)
        style_cell(ws, r, 4, wk.get("daily_actions", ""), FONTS["small_8"], fill, ALIGN_LEFT)
        style_cell(ws, r, 5, wk.get("key_milestone", ""), FONTS["small_8_grey"], fill, ALIGN_LEFT)
        r += 1

    # Month 1 Goals
    r += 1
    style_range(ws, r, 2, 5, "🎯  MONTH 1 GOALS",
        FONTS["section_12_white"], FILLS["orange"], ALIGN_LEFT_CENTER)
    r += 1
    for i, g in enumerate(impl_data.get("month1_goals", [])):
        fill = FILLS["light_orange_bg"] if i % 2 == 0 else FILLS["white"]
        style_cell(ws, r, 2, g.get("goal", ""), FONTS["body_9_bold_orange"], fill, ALIGN_LEFT)
        style_cell(ws, r, 3, g.get("description", ""), FONTS["body_9"], fill, ALIGN_LEFT)
        style_range(ws, r, 4, 5, g.get("target", ""), FONTS["body_9_bold_green"], fill, ALIGN_LEFT)
        r += 1

    # 90-Day Milestones
    r += 1
    style_range(ws, r, 2, 5, "📊  90-DAY MILESTONES",
        FONTS["section_12_white"], FILLS["purple"], ALIGN_LEFT_CENTER)
    r += 1
    for i, m in enumerate(impl_data.get("milestones_90day", [])):
        fill = FILLS["light_purple_bg"] if i % 2 == 0 else FILLS["white"]
        style_cell(ws, r, 2, m.get("period", ""), FONTS["body_9_bold_navy"], fill, ALIGN_LEFT)
        style_range(ws, r, 3, 5, m.get("milestone", ""), FONTS["body_9"], fill, ALIGN_LEFT)
        r += 1
