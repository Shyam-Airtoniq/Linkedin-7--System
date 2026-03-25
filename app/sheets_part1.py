"""Sheet builders for Sheets 0-4 of the LinkedIn COMPLETE SYSTEM."""
from templates.excel_template import (
    FILLS, FONTS, ALIGN_LEFT, ALIGN_CENTER, ALIGN_LEFT_CENTER,
    style_cell, style_range, style_merged_block, set_column_widths,
    alternating_row_fill,
)


def build_sheet0_strategic(wb, analysis, business_name):
    """Sheet 0: Strategic Foundation (same as starter kit)."""
    ws = wb.create_sheet("0. Strategic Foundation", 0)
    set_column_widths(ws, {"A": 3, "B": 40, "C": 45, "D": 31, "E": 8.3})

    style_range(ws, 1, 2, 4,
        f"STRATEGIC FOUNDATION  |  Custom Analysis for {business_name}",
        FONTS["title_14_white"], FILLS["dark_navy"], ALIGN_LEFT_CENTER)

    # A) ICP PROFILES
    style_range(ws, 3, 2, 4, "A)  TARGET ICP PROFILES",
        FONTS["section_12_white"], FILLS["dark_navy"], ALIGN_LEFT_CENTER)
    profiles = analysis.get("icp_profiles", [])
    row = 4
    colors = [("medium_blue", "light_blue_bg"), ("medium_blue", "light_green_bg")]
    for i, p in enumerate(profiles[:2]):
        header_c, body_c = colors[i]
        style_range(ws, row, 2, 4, f"  {p.get('label', f'ICP Profile {chr(65+i)}')}",
            FONTS["subsection_10_white"], FILLS[header_c], ALIGN_LEFT_CENTER)
        row += 1
        style_merged_block(ws, row, row + 3, 2, 4, p.get("full_description", ""),
            FONTS["body_9"], FILLS[body_c], ALIGN_LEFT)
        row += 5

    # B) PRICING
    style_range(ws, row, 2, 4, "B)  PRICING STRATEGY (4 Tiers)",
        FONTS["section_12_white"], FILLS["medium_blue"], ALIGN_LEFT_CENTER)
    row += 1
    pricing = analysis.get("pricing", {})
    for i, key in enumerate(["tier1", "tier2", "tier3", "tier4"]):
        t = pricing.get(key, {})
        fill = FILLS["light_yellow_bg"] if i % 2 == 0 else FILLS["white"]
        style_cell(ws, row, 2, t.get("name", key),
            FONTS["body_9_bold_navy"], fill, ALIGN_LEFT)
        style_cell(ws, row, 3, t.get("description", ""),
            FONTS["body_9"], fill, ALIGN_LEFT)
        style_cell(ws, row, 4, t.get("price_range", ""),
            FONTS["body_9_bold_orange"], fill, ALIGN_LEFT)
        row += 1

    # C) UNIQUE POSITIONING
    row += 1
    style_range(ws, row, 2, 4, "C)  UNIQUE POSITIONING",
        FONTS["section_12_white"], FILLS["orange"], ALIGN_LEFT_CENTER)
    row += 1
    pos = analysis.get("positioning", {})
    style_cell(ws, row, 2, "Positioning Statement",
        FONTS["body_9_bold_orange"], FILLS["light_orange_bg"], ALIGN_LEFT)
    style_range(ws, row, 3, 4, pos.get("statement", ""),
        FONTS["body_9"], FILLS["light_orange_bg"], ALIGN_LEFT)
    row += 1
    for i, d in enumerate(pos.get("differentiators", [])):
        fill = FILLS["white"] if i % 2 == 0 else FILLS["light_orange_bg"]
        style_cell(ws, row, 2, d.get("label", ""),
            FONTS["body_9_bold_orange"], fill, ALIGN_LEFT)
        style_range(ws, row, 3, 4, d.get("text", ""),
            FONTS["body_9"], fill, ALIGN_LEFT)
        row += 1
    style_cell(ws, row, 2, "Core Value Proposition",
        FONTS["body_9_bold_orange"], FILLS["light_orange_bg"], ALIGN_LEFT)
    style_range(ws, row, 3, 4, pos.get("core_value_proposition", ""),
        FONTS["body_9"], FILLS["light_orange_bg"], ALIGN_LEFT)
    row += 1

    # D) PAIN POINTS
    row += 1
    style_range(ws, row, 2, 4, "D)  ICP PAIN POINTS + HOW YOU SOLVE EACH",
        FONTS["section_12_white"], FILLS["dark_red"], ALIGN_LEFT_CENTER)
    row += 1
    style_cell(ws, row, 2, "Pain Point",
        FONTS["body_9_white"], FILLS["dark_red"], ALIGN_LEFT)
    style_range(ws, row, 3, 4, f"How {business_name}'s Systems Solve It",
        FONTS["body_9_white"], FILLS["dark_red"], ALIGN_LEFT)
    row += 1
    for i, pp in enumerate(analysis.get("pain_points", [])):
        fill = FILLS["light_red_bg"] if i % 2 == 0 else FILLS["white"]
        style_cell(ws, row, 2, pp.get("pain", ""),
            FONTS["body_9"], fill, ALIGN_LEFT)
        style_range(ws, row, 3, 4, pp.get("solution", ""),
            FONTS["body_9_green"], fill, ALIGN_LEFT)
        row += 1

    # E) CONTENT PILLARS
    row += 1
    style_range(ws, row, 2, 4, "E)  CONTENT PILLARS (3 Pillars + % Distribution)",
        FONTS["section_12_white"], FILLS["purple"], ALIGN_LEFT_CENTER)
    row += 1
    for i, cp in enumerate(analysis.get("content_pillars", [])):
        fill = FILLS["light_purple_bg"] if i % 2 == 0 else FILLS["white"]
        style_cell(ws, row, 2, cp.get("name", ""),
            FONTS["body_9_bold_purple"], fill, ALIGN_LEFT)
        style_cell(ws, row, 3, f"{cp.get('percentage', '')}%",
            FONTS["body_12_bold_purple"], fill, ALIGN_CENTER)
        style_cell(ws, row, 4, cp.get("sample_topics", ""),
            FONTS["small_8"], fill, ALIGN_LEFT)
        row += 1


def build_sheet1_dashboard(wb, analysis, dashboard_data, business_name):
    """Sheet 1: Master Dashboard."""
    ws = wb.create_sheet("1. Master Dashboard")
    set_column_widths(ws, {"A": 3, "B": 28, "C": 16, "D": 13, "E": 13, "F": 13, "G": 20, "H": 16})

    # Title — says "COMPLETE SYSTEM"
    style_range(ws, 1, 2, 8, "🚀  90-DAY LINKEDIN COMPLETE SYSTEM",
        FONTS["title_18_white"], FILLS["dark_navy"], ALIGN_LEFT_CENTER)
    style_range(ws, 2, 2, 8, dashboard_data.get("subtitle", ""),
        FONTS["subtitle_11_gold"], FILLS["dark_navy"], ALIGN_LEFT_CENTER)

    # 7-Phase Timeline
    style_range(ws, 4, 2, 8, "📅  7-PHASE 90-DAY TIMELINE",
        FONTS["section_12_white"], FILLS["medium_blue"], ALIGN_LEFT_CENTER)
    phase_colors = ["dark_navy", "medium_blue", "orange", "dark_green", "purple", "gold", "dark_red"]
    phases = dashboard_data.get("phases", [])
    for i, ph in enumerate(phases[:7]):
        r = 5 + i
        color = phase_colors[i] if i < len(phase_colors) else "medium_blue"
        style_cell(ws, r, 2, ph.get("phase", ""),
            FONTS["subsection_10_white"], FILLS[color], ALIGN_CENTER)
        style_cell(ws, r, 3, ph.get("days", ""),
            FONTS["body_9_bold_navy"], FILLS["light_yellow_bg"], ALIGN_CENTER)
        style_range(ws, r, 4, 6, ph.get("name", ""),
            FONTS["subsection_10_navy"], FILLS["off_white"], ALIGN_LEFT_CENTER)
        style_range(ws, r, 7, 8, ph.get("description", ""),
            FONTS["body_9_grey"], FILLS["white"], ALIGN_LEFT)

    # 30-Day Checklist
    r = 13
    style_range(ws, r, 2, 8, "✅  30-DAY QUICK START CHECKLIST",
        FONTS["section_12_white"], FILLS["dark_navy"], ALIGN_LEFT_CENTER)
    r += 1
    for i, item in enumerate(dashboard_data.get("checklist_items", [])):
        fill = FILLS["off_white"] if i % 2 == 0 else FILLS["white"]
        style_cell(ws, r, 2, "☐", FONTS["checkbox_11_navy"], fill, ALIGN_CENTER)
        style_range(ws, r, 3, 8, item, FONTS["body_9"], fill, ALIGN_LEFT)
        r += 1

    # Progress Milestones
    r += 1
    style_range(ws, r, 2, 8, "📊  PROGRESS TRACKER – KEY MILESTONES",
        FONTS["section_12_white"], FILLS["purple"], ALIGN_LEFT_CENTER)
    r += 1
    for i, m in enumerate(dashboard_data.get("progress_milestones", [])):
        fill = FILLS["light_purple_bg"] if i % 2 == 0 else FILLS["white"]
        style_cell(ws, r, 2, "☐", FONTS["checkbox_11_purple"], fill, ALIGN_CENTER)
        style_cell(ws, r, 3, m.get("day", ""), FONTS["body_9_bold_navy"], fill, ALIGN_LEFT)
        style_range(ws, r, 4, 8, m.get("description", ""), FONTS["body_9"], fill, ALIGN_LEFT)
        r += 1

    # Why This Works
    r += 1
    style_range(ws, r, 2, 8, "💡  WHY THIS WORKS",
        FONTS["section_12_white"], FILLS["dark_green"], ALIGN_LEFT_CENTER)
    r += 1
    for i, reason in enumerate(dashboard_data.get("why_this_works", [])):
        fill = FILLS["light_green_bg"] if i % 2 == 0 else FILLS["white"]
        style_range(ws, r, 2, 8, reason, FONTS["body_9_green"], fill, ALIGN_LEFT)
        r += 1

    # Key Metrics
    r += 1
    style_range(ws, r, 2, 8, "📈  KEY METRICS TO TRACK",
        FONTS["section_12_white"], FILLS["orange"], ALIGN_LEFT_CENTER)
    r += 1
    for col, hdr in [(2, "Metric"), (4, "Week 1 Benchmark"), (6, "Week 4 Target"), (8, "90-Day Goal")]:
        style_cell(ws, r, col, hdr, FONTS["body_9_bold_navy"], FILLS["light_orange_bg"], ALIGN_LEFT)
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
    ws.merge_cells(start_row=r, start_column=4, end_row=r, end_column=5)
    ws.merge_cells(start_row=r, start_column=6, end_row=r, end_column=7)
    r += 1
    for i, m in enumerate(dashboard_data.get("metrics", [])):
        fill = FILLS["off_white"] if i % 2 == 0 else FILLS["white"]
        style_cell(ws, r, 2, m.get("metric", ""), FONTS["body_9"], fill, ALIGN_LEFT)
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
        style_cell(ws, r, 4, m.get("week1", ""), FONTS["body_9_blue"], fill, ALIGN_CENTER)
        ws.merge_cells(start_row=r, start_column=4, end_row=r, end_column=5)
        style_cell(ws, r, 6, m.get("week4", ""), FONTS["body_9_bold_orange"], fill, ALIGN_CENTER)
        ws.merge_cells(start_row=r, start_column=6, end_row=r, end_column=7)
        style_cell(ws, r, 8, m.get("day90", ""), FONTS["body_9_bold_green"], fill, ALIGN_CENTER)
        for c in range(2, 9):
            ws.cell(row=r, column=c).fill = fill
        r += 1


def build_sheet2_profile(wb, profile_data):
    """Sheet 2: Profile Optimization — EXPANDED (25 headlines, story arc, 10 featured ideas)."""
    ws = wb.create_sheet("2. Profile Optimization")
    set_column_widths(ws, {"A": 3, "B": 32, "C": 14, "D": 13, "E": 13, "F": 13, "G": 13, "H": 13})

    style_range(ws, 1, 2, 8,
        "PHASE 1: PROFILE OPTIMIZATION  |  Days 1–7  |  Complete System",
        FONTS["title_14_white"], FILLS["dark_navy"], ALIGN_LEFT_CENTER)

    # Audit Checklist
    style_range(ws, 3, 2, 8, "🔍  PROFILE AUDIT CHECKLIST (10 Items)",
        FONTS["section_12_white"], FILLS["dark_navy"], ALIGN_LEFT_CENTER)
    r = 4
    for i, item in enumerate(profile_data.get("audit_checklist", [])):
        fill = FILLS["light_blue_bg"] if i % 2 == 0 else FILLS["white"]
        style_cell(ws, r, 2, f"☐  {item.get('item', '')}",
            FONTS["subsection_10_navy"], fill, ALIGN_LEFT)
        style_range(ws, r, 3, 8, item.get("question", ""),
            FONTS["body_9"], fill, ALIGN_LEFT)
        r += 1

    # 25 Headlines
    r += 1
    style_range(ws, r, 2, 8, "✍️  25 INDUSTRY-SPECIFIC HEADLINE OPTIONS",
        FONTS["section_12_white"], FILLS["medium_blue"], ALIGN_LEFT_CENTER)
    r += 1
    for i, hl in enumerate(profile_data.get("headline_options", [])):
        fill = FILLS["light_yellow_bg"] if i % 2 == 0 else FILLS["off_white"]
        style_cell(ws, r, 2, hl.get("label", f"Option {i+1}"),
            FONTS["body_9_bold_navy"], fill, ALIGN_LEFT)
        style_range(ws, r, 3, 8, hl.get("text", ""),
            FONTS["body_9"], fill, ALIGN_LEFT)
        r += 1

    # About Section with examples
    r += 1
    style_range(ws, r, 2, 8, "📝  ABOUT SECTION STRUCTURE + EXAMPLES",
        FONTS["section_12_white"], FILLS["dark_navy"], ALIGN_LEFT_CENTER)
    r += 1
    for i, sec in enumerate(profile_data.get("about_section", [])):
        fill = FILLS["light_green_bg"] if i % 2 == 0 else FILLS["white"]
        style_cell(ws, r, 2, sec.get("section", ""),
            FONTS["body_9_bold_green"], fill, ALIGN_LEFT)
        style_range(ws, r, 3, 5, sec.get("instruction", ""),
            FONTS["body_9"], fill, ALIGN_LEFT)
        style_range(ws, r, 6, 8, sec.get("example", ""),
            FONTS["small_8_grey"], fill, ALIGN_LEFT)
        r += 1

    # Story Arc Framework
    r += 1
    story = profile_data.get("story_arc", {})
    style_range(ws, r, 2, 8, "📖  STORY ARC FRAMEWORK",
        FONTS["section_12_white"], FILLS["purple"], ALIGN_LEFT_CENTER)
    r += 1
    arc_items = [
        ("Opening Hook", story.get("opening_hook", "")),
        ("Struggle Phase", story.get("struggle_phase", "")),
        ("Breakthrough", story.get("breakthrough", "")),
        ("Mission Statement", story.get("mission_statement", "")),
    ]
    for i, (label, text) in enumerate(arc_items):
        fill = FILLS["light_purple_bg"] if i % 2 == 0 else FILLS["white"]
        style_cell(ws, r, 2, label, FONTS["body_9_bold_purple"], fill, ALIGN_LEFT)
        style_range(ws, r, 3, 8, text, FONTS["body_9"], fill, ALIGN_LEFT)
        r += 1
    # Full story
    r += 1
    style_range(ws, r, 2, 8, "Complete Story:",
        FONTS["body_9_bold_purple"], FILLS["light_purple_bg"], ALIGN_LEFT)
    r += 1
    style_merged_block(ws, r, r + 3, 2, 8, story.get("full_story", ""),
        FONTS["body_9"], FILLS["off_white"], ALIGN_LEFT)
    r += 5

    # Skills
    style_range(ws, r, 2, 8, "🎯  12 RECOMMENDED SKILLS",
        FONTS["section_12_white"], FILLS["medium_blue"], ALIGN_LEFT_CENTER)
    r += 1
    skills = profile_data.get("skills", [])
    for i in range(0, len(skills), 3):
        fill = FILLS["light_blue_bg"] if (i // 3) % 2 == 0 else FILLS["white"]
        for j in range(3):
            idx = i + j
            if idx < len(skills):
                col = 2 + j * 3
                style_cell(ws, r, col, f"✓  {skills[idx]}",
                    FONTS["body_9_navy"], fill, ALIGN_LEFT)
        for c in range(2, 9):
            ws.cell(row=r, column=c).fill = fill
        r += 1

    # 10 Featured Section Ideas
    r += 1
    style_range(ws, r, 2, 8, "⭐  10 FEATURED SECTION IDEAS",
        FONTS["section_12_white"], FILLS["dark_navy"], ALIGN_LEFT_CENTER)
    r += 1
    style_cell(ws, r, 2, "Type", FONTS["body_9_white"], FILLS["dark_navy"], ALIGN_LEFT)
    style_range(ws, r, 3, 5, "Content Idea", FONTS["body_9_white"], FILLS["dark_navy"], ALIGN_LEFT)
    style_range(ws, r, 6, 8, "Why It Works", FONTS["body_9_white"], FILLS["dark_navy"], ALIGN_LEFT)
    r += 1
    for i, feat in enumerate(profile_data.get("featured_section", [])):
        fill = FILLS["light_yellow_bg"] if i % 2 == 0 else FILLS["white"]
        if isinstance(feat, dict):
            style_cell(ws, r, 2, feat.get("type", ""), FONTS["body_9_bold_navy"], fill, ALIGN_LEFT)
            style_range(ws, r, 3, 5, feat.get("idea", ""), FONTS["body_9"], fill, ALIGN_LEFT)
            style_range(ws, r, 6, 8, feat.get("why", ""), FONTS["small_8_grey"], fill, ALIGN_LEFT)
        else:
            style_range(ws, r, 2, 8, feat, FONTS["body_9"], fill, ALIGN_LEFT)
        r += 1


def build_sheet3_content_calendar(wb, calendar_data):
    """Sheet 3: 90-Day Content Calendar — EXPANDED (36 posts, 50 hooks, 15 story templates)."""
    ws = wb.create_sheet("3. 90-Day Content Calendar")
    set_column_widths(ws, {"A": 3, "B": 8, "C": 10, "D": 18, "E": 35, "F": 30, "G": 14, "H": 14})

    style_range(ws, 1, 2, 8,
        "PHASE 2: 90-DAY CONTENT CALENDAR  |  36 Posts  |  Complete System",
        FONTS["title_14_white"], FILLS["dark_navy"], ALIGN_LEFT_CENTER)

    # Pillars
    style_range(ws, 3, 2, 8, "📌  YOUR 3 CONTENT PILLARS",
        FONTS["section_12_white"], FILLS["dark_navy"], ALIGN_LEFT_CENTER)
    r = 4
    pillar_colors = ["medium_blue", "dark_green", "orange"]
    for i, p in enumerate(calendar_data.get("pillars", [])):
        hc = pillar_colors[i] if i < len(pillar_colors) else "medium_blue"
        style_range(ws, r, 2, 8, p.get("name", ""),
            FONTS["subsection_10_white"], FILLS[hc], ALIGN_LEFT_CENTER)
        r += 1
        style_range(ws, r, 2, 8, p.get("description", ""),
            FONTS["body_9"], FILLS["off_white"], ALIGN_LEFT)
        r += 1

    # Full 90-Day Calendar
    r += 1
    style_range(ws, r, 2, 8, "📅  FULL 90-DAY CONTENT CALENDAR (36 Posts)",
        FONTS["section_12_white"], FILLS["medium_blue"], ALIGN_LEFT_CENTER)
    r += 1
    headers = ["Wk", "Day", "Pillar", "Post Hook", "Key Points", "Format", "CTA"]
    for i, h in enumerate(headers):
        style_cell(ws, r, 2 + i, h, FONTS["small_8_white"], FILLS["dark_navy"], ALIGN_LEFT)
    r += 1

    pillar_fill = {"Education": "medium_blue", "Proof": "dark_green", "Engagement": "orange"}
    for i, entry in enumerate(calendar_data.get("calendar", [])):
        fill = FILLS["light_blue_bg"] if i % 2 == 0 else FILLS["white"]
        style_cell(ws, r, 2, str(entry.get("week", "")), FONTS["small_8"], fill, ALIGN_CENTER)
        style_cell(ws, r, 3, entry.get("day", ""), FONTS["body_9_bold_navy"], fill, ALIGN_LEFT)
        pname = entry.get("pillar", "Education")
        pfill = pillar_fill.get(pname, "medium_blue")
        style_cell(ws, r, 4, pname, FONTS["small_8_white"], FILLS[pfill], ALIGN_CENTER)
        style_cell(ws, r, 5, entry.get("hook", ""), FONTS["small_8"], fill, ALIGN_LEFT)
        style_cell(ws, r, 6, entry.get("key_points", ""), FONTS["small_8_grey"], fill, ALIGN_LEFT)
        style_cell(ws, r, 7, entry.get("format", ""), FONTS["small_8"], fill, ALIGN_CENTER)
        style_cell(ws, r, 8, entry.get("cta", ""), FONTS["small_8_grey"], fill, ALIGN_LEFT)
        r += 1

    # 50 Hooks Library
    r += 1
    style_range(ws, r, 2, 8, "🎣  50 SCROLL-STOPPING HOOKS LIBRARY (by Category)",
        FONTS["section_12_white"], FILLS["purple"], ALIGN_LEFT_CENTER)
    r += 1
    for cat in calendar_data.get("hooks_library", []):
        style_range(ws, r, 2, 8, cat.get("category", ""),
            FONTS["body_9_bold_purple"], FILLS["light_purple_bg"], ALIGN_LEFT)
        r += 1
        for hook in cat.get("hooks", []):
            style_range(ws, r, 2, 8, f"→  {hook}",
                FONTS["body_9"], FILLS["white"], ALIGN_LEFT)
            r += 1
        r += 1  # spacing between categories

    # 15 Story Templates
    r += 1
    style_range(ws, r, 2, 8, "📖  15 STORY TEMPLATES WITH EXAMPLES",
        FONTS["section_12_white"], FILLS["dark_navy"], ALIGN_LEFT_CENTER)
    r += 1
    for i, tmpl in enumerate(calendar_data.get("story_templates", [])):
        fill = FILLS["light_yellow_bg"] if i % 2 == 0 else FILLS["off_white"]
        style_range(ws, r, 2, 8, tmpl.get("name", ""),
            FONTS["body_9_bold_navy"], fill, ALIGN_LEFT)
        r += 1
        style_range(ws, r, 2, 4, tmpl.get("structure", ""),
            FONTS["small_8"], FILLS["white"], ALIGN_LEFT)
        style_range(ws, r, 5, 8, tmpl.get("example", ""),
            FONTS["small_8_grey"], FILLS["white"], ALIGN_LEFT)
        r += 1

    # Post Frameworks
    r += 1
    style_range(ws, r, 2, 8, "📋  POST TEMPLATE FRAMEWORKS",
        FONTS["section_12_white"], FILLS["orange"], ALIGN_LEFT_CENTER)
    r += 1
    for fw in calendar_data.get("post_frameworks", []):
        style_range(ws, r, 2, 8, fw.get("name", ""),
            FONTS["body_9_bold_orange"], FILLS["light_orange_bg"], ALIGN_LEFT)
        r += 1
        style_merged_block(ws, r, r + 2, 2, 8, fw.get("template", ""),
            FONTS["body_9"], FILLS["white"], ALIGN_LEFT)
        r += 4


def build_sheet4_outreach(wb, outreach_data):
    """Sheet 4: Outreach System — EXPANDED (8 CR templates, 6 DM sequences, email seq, Sales Nav)."""
    ws = wb.create_sheet("4. Outreach System")
    set_column_widths(ws, {"A": 3, "B": 25, "C": 18, "D": 13, "E": 13, "F": 13, "G": 13, "H": 13, "I": 9})

    style_range(ws, 1, 2, 8,
        "PHASE 3: OUTREACH SYSTEM  |  Days 22–35  |  Complete System",
        FONTS["title_14_white"], FILLS["dark_navy"], ALIGN_LEFT_CENTER)

    # ICP Worksheet
    style_range(ws, 3, 2, 8, "🎯  ICP DEFINITION WORKSHEET",
        FONTS["section_12_white"], FILLS["dark_navy"], ALIGN_LEFT_CENTER)
    icp_hdrs = ["ICP Profile", "Type", "Decision-Maker", "Org Type", "Size", "Volume", "Pain Points"]
    for i, h in enumerate(icp_hdrs):
        style_cell(ws, 4, 2 + i, h, FONTS["small_8_white"], FILLS["medium_blue"], ALIGN_LEFT)
    for i, icp in enumerate(outreach_data.get("icp_worksheet", [])):
        r = 5 + i
        fill = FILLS["light_blue_bg"] if i % 2 == 0 else FILLS["white"]
        vals = [icp.get("label",""), icp.get("type",""), icp.get("decision_maker",""),
                icp.get("org_type",""), icp.get("size",""), icp.get("volume",""), icp.get("pain_points","")]
        for j, v in enumerate(vals):
            font = FONTS["small_8_bold_navy"] if j == 0 else FONTS["small_8"]
            style_cell(ws, r, 2 + j, v, font, fill, ALIGN_LEFT)

    # Daily Quotas
    r = 8
    style_range(ws, r, 2, 8, "📊  DAILY OUTREACH QUOTAS",
        FONTS["section_12_white"], FILLS["orange"], ALIGN_LEFT_CENTER)
    r += 1
    for col, hdr in [(2, "Activity"), (4, "Daily"), (6, "Weekly"), (8, "Notes")]:
        style_cell(ws, r, col, hdr, FONTS["small_8_bold_navy"], FILLS["light_orange_bg"], ALIGN_LEFT)
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
    ws.merge_cells(start_row=r, start_column=4, end_row=r, end_column=5)
    ws.merge_cells(start_row=r, start_column=6, end_row=r, end_column=7)
    r += 1
    for i, q in enumerate(outreach_data.get("daily_quotas", [])):
        fill = FILLS["light_orange_bg"] if i % 2 == 0 else FILLS["white"]
        style_cell(ws, r, 2, q.get("activity", ""), FONTS["small_8"], fill, ALIGN_LEFT)
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
        style_cell(ws, r, 4, q.get("daily", ""), FONTS["body_9_bold_orange"], fill, ALIGN_CENTER)
        ws.merge_cells(start_row=r, start_column=4, end_row=r, end_column=5)
        style_cell(ws, r, 6, q.get("weekly", ""), FONTS["body_9_bold_orange"], fill, ALIGN_CENTER)
        ws.merge_cells(start_row=r, start_column=6, end_row=r, end_column=7)
        style_cell(ws, r, 8, q.get("notes", ""), FONTS["small_8_grey"], fill, ALIGN_LEFT)
        for c in range(2, 9):
            ws.cell(row=r, column=c).fill = fill
        r += 1

    # 8 Connection Templates
    r += 1
    style_range(ws, r, 2, 8, "📨  8 CONNECTION REQUEST TEMPLATES (By Scenario)",
        FONTS["section_12_white"], FILLS["dark_navy"], ALIGN_LEFT_CENTER)
    r += 1
    for t in outreach_data.get("connection_templates", []):
        scenario = t.get("scenario", t.get("context", ""))
        style_range(ws, r, 2, 8, f"{t.get('label', '')} — {scenario}",
            FONTS["body_9_bold_navy"], FILLS["light_yellow_bg"], ALIGN_LEFT)
        r += 1
        style_merged_block(ws, r, r + 1, 2, 8, t.get("text", ""),
            FONTS["body_9"], FILLS["off_white"], ALIGN_LEFT)
        r += 3

    # 6 DM Sequences
    style_range(ws, r, 2, 8, "💬  6 COMPLETE DM SEQUENCES",
        FONTS["section_12_white"], FILLS["purple"], ALIGN_LEFT_CENTER)
    r += 1
    dm_fills = ["light_purple_bg", "light_green_bg", "light_orange_bg",
                "light_blue_bg", "light_yellow_bg", "light_red_bg"]
    for si, seq in enumerate(outreach_data.get("dm_sequences", [])):
        style_range(ws, r, 2, 8,
            f"🔹 {seq.get('sequence_name', '')} — Trigger: {seq.get('trigger', '')}",
            FONTS["body_9_white"], FILLS["purple"], ALIGN_LEFT)
        r += 1
        df = dm_fills[si % len(dm_fills)]
        for msg in seq.get("messages", []):
            style_cell(ws, r, 2, f"{msg.get('day', '')} - {msg.get('label', '')}",
                FONTS["small_8_bold_navy"], FILLS[df], ALIGN_LEFT)
            style_range(ws, r, 3, 8, msg.get("text", ""),
                FONTS["body_9"], FILLS[df], ALIGN_LEFT)
            r += 1
        r += 1

    # Email Sequence
    r += 1
    style_range(ws, r, 2, 8, "📧  5-EMAIL OUTREACH SEQUENCE",
        FONTS["section_12_white"], FILLS["dark_navy"], ALIGN_LEFT_CENTER)
    r += 1
    for i, em in enumerate(outreach_data.get("email_sequence", [])):
        fill = FILLS["light_blue_bg"] if i % 2 == 0 else FILLS["white"]
        style_range(ws, r, 2, 3, em.get("label", ""),
            FONTS["body_9_bold_navy"], fill, ALIGN_LEFT)
        style_cell(ws, r, 4, f"Subject: {em.get('subject', '')}",
            FONTS["body_9_bold_orange"], fill, ALIGN_LEFT)
        ws.merge_cells(start_row=r, start_column=4, end_row=r, end_column=5)
        style_range(ws, r, 6, 8, em.get("body", ""),
            FONTS["body_9"], fill, ALIGN_LEFT)
        r += 1

    # Sales Navigator Guide
    r += 1
    nav = outreach_data.get("sales_nav_guide", {})
    style_range(ws, r, 2, 8, "🔎  LINKEDIN SALES NAVIGATOR SETUP GUIDE",
        FONTS["section_12_white"], FILLS["medium_blue"], ALIGN_LEFT_CENTER)
    r += 1
    # Search Filters
    for sf in nav.get("search_filters", []):
        fill = FILLS["light_blue_bg"]
        style_cell(ws, r, 2, sf.get("filter", ""), FONTS["body_9_bold_navy"], fill, ALIGN_LEFT)
        style_range(ws, r, 3, 8, sf.get("value", ""), FONTS["body_9"], fill, ALIGN_LEFT)
        r += 1
    # Saved Searches
    r += 1
    style_range(ws, r, 2, 8, "📁  Recommended Saved Searches",
        FONTS["body_9_bold_blue"], FILLS["light_blue_bg"], ALIGN_LEFT)
    r += 1
    for ss in nav.get("saved_searches", []):
        style_cell(ws, r, 2, ss.get("name", ""), FONTS["body_9_bold_navy"], FILLS["white"], ALIGN_LEFT)
        style_range(ws, r, 3, 8, ss.get("description", ""), FONTS["body_9"], FILLS["white"], ALIGN_LEFT)
        r += 1
    # Tips
    for tip in nav.get("optimization_tips", []):
        style_range(ws, r, 2, 8, f"💡 {tip}", FONTS["body_9"], FILLS["off_white"], ALIGN_LEFT)
        r += 1
