"""
All Claude API prompts for the LinkedIn COMPLETE SYSTEM ($199).
Each prompt maps to a sheet in the final Excel workbook and
returns structured JSON that the ExcelBuilder consumes directly.

COMPLETE SYSTEM generates 3-5× more content than the Free Starter Kit:
- 25 headlines (vs 3), 90-day calendar (vs 30-day), 8 CR templates (vs 2),
- 6 DM sequences (vs 1), 15 objection scripts (vs 3), etc.
"""

# ───────────────────────────────────────────────────────────
# SHEET 0 — Strategic Foundation (same as starter kit)
# ───────────────────────────────────────────────────────────
STRATEGIC_ANALYSIS_PROMPT = """
You are a LinkedIn growth strategist. Analyze the following business information and produce a comprehensive strategic foundation.

**BUSINESS/SERVICES INFORMATION:**
{business_details}

{additional_context}

Return ONLY valid JSON with this exact structure:
{{
  "icp_profiles": [
    {{
      "label": "ICP Profile A",
      "name": "Short name for this profile",
      "title": "Decision-maker title",
      "org": "Type of organization",
      "size_metric": "Revenue or asset range or employee count",
      "volume_metric": "Monthly volume / transactions / projects",
      "primary_pain": "1-2 sentence primary pain point",
      "full_description": "5-6 line detailed description with Title, Org, Size, Volume, Primary Pain, Secondary Pain"
    }},
    {{
      "label": "ICP Profile B",
      "name": "Short name for this profile",
      "title": "Decision-maker title",
      "org": "Type of organization",
      "size_metric": "Revenue or asset range",
      "volume_metric": "Monthly volume",
      "primary_pain": "1-2 sentence primary pain point",
      "full_description": "5-6 line detailed description"
    }}
  ],
  "pricing": {{
    "tier1": {{
      "name": "Tier 1 – [Name]",
      "description": "2-3 sentence description of what's included and delivery timeline",
      "price_range": "$X,XXX–$X,XXX"
    }},
    "tier2": {{
      "name": "Tier 2 – [Name]",
      "description": "2-3 sentence description",
      "price_range": "$X,XXX–$XX,XXX + $X,XXX/mo"
    }},
    "tier3": {{
      "name": "Tier 3 – [Name]",
      "description": "2-3 sentence description",
      "price_range": "$XX,XXX–$XX,XXX + $X,XXX/mo"
    }},
    "tier4": {{
      "name": "Tier 4 – Enterprise / Custom",
      "description": "2-3 sentence description",
      "price_range": "$XX,XXX+ Custom"
    }}
  }},
  "positioning": {{
    "statement": "One powerful positioning statement (the only X who Y so they Z)",
    "differentiators": [
      {{"label": "Key Differentiator 1", "text": "1-2 sentence differentiator"}},
      {{"label": "Key Differentiator 2", "text": "1-2 sentence differentiator"}},
      {{"label": "Key Differentiator 3", "text": "1-2 sentence differentiator"}}
    ],
    "core_value_proposition": "One sentence value proposition"
  }},
  "pain_points": [
    {{"pain": "Specific pain point the ICP feels", "solution": "How the business solves it"}},
    {{"pain": "...", "solution": "..."}},
    {{"pain": "...", "solution": "..."}},
    {{"pain": "...", "solution": "..."}},
    {{"pain": "...", "solution": "..."}},
    {{"pain": "...", "solution": "..."}},
    {{"pain": "...", "solution": "..."}},
    {{"pain": "...", "solution": "..."}},
    {{"pain": "...", "solution": "..."}},
    {{"pain": "...", "solution": "..."}}
  ],
  "content_pillars": [
    {{
      "name": "Pillar 1: EDUCATION",
      "percentage": 40,
      "sample_topics": "3 sample topic titles separated by semicolons"
    }},
    {{
      "name": "Pillar 2: PROOF & RESULTS",
      "percentage": 35,
      "sample_topics": "3 sample topic titles separated by semicolons"
    }},
    {{
      "name": "Pillar 3: ENGAGEMENT",
      "percentage": 25,
      "sample_topics": "3 sample topic titles separated by semicolons"
    }}
  ]
}}

IMPORTANT:
- Generate exactly 2 ICP profiles, 4 pricing tiers, 3 differentiators, 10 pain points, and 3 content pillars.
- All content must be highly specific to the business/services described. Use industry-specific language.
- Pricing should be realistic for the market described.
- Pain points should be visceral and specific — things the ICP literally says on calls.
"""

# ───────────────────────────────────────────────────────────
# SHEET 1 — Master Dashboard (same as starter)
# ───────────────────────────────────────────────────────────
DASHBOARD_PROMPT = """
You are a LinkedIn growth strategist. Generate a comprehensive Master Dashboard for a 90-Day LinkedIn Complete System.

**BUSINESS:** {business_name}
**SERVICES:** {services}
**ICP SUMMARY:** {icp_summary}
**POSITIONING:** {positioning_statement}

Return ONLY valid JSON:
{{
  "subtitle": "Custom-Built for [ICP niche] | [Core service] | [Business/Person Name]",
  "phases": [
    {{"phase": "Phase 1", "days": "Days 1–7", "name": "Profile Optimization", "description": "1-sentence description tailored to their niche"}},
    {{"phase": "Phase 2", "days": "Days 8–21", "name": "Content Calendar", "description": "..."}},
    {{"phase": "Phase 3", "days": "Days 22–35", "name": "Outreach System", "description": "..."}},
    {{"phase": "Phase 4", "days": "Days 36–50", "name": "Sales System", "description": "..."}},
    {{"phase": "Phase 5", "days": "Days 51–65", "name": "Lead Magnet Funnel", "description": "..."}},
    {{"phase": "Phase 6", "days": "Days 66–80", "name": "90-Day Content Engine", "description": "..."}},
    {{"phase": "Phase 7", "days": "Days 81–90", "name": "Full Implementation", "description": "..."}}
  ],
  "checklist_items": [
    "15 specific, niche-tailored 30-day checklist items that progressively build profile, content, outreach, and sales systems"
  ],
  "progress_milestones": [
    {{"day": "Day 7", "description": "Milestone description"}},
    {{"day": "Day 14", "description": "..."}},
    {{"day": "Day 21", "description": "..."}},
    {{"day": "Day 30", "description": "..."}},
    {{"day": "Day 45", "description": "..."}},
    {{"day": "Day 60", "description": "..."}},
    {{"day": "Day 75", "description": "..."}},
    {{"day": "Day 90", "description": "..."}}
  ],
  "why_this_works": [
    "4 reasons why this LinkedIn system works specifically for their niche (start each with →)"
  ],
  "metrics": [
    {{"metric": "Profile Views / Week", "week1": "50–100", "week4": "200–400", "day90": "500+"}},
    {{"metric": "Connection Acceptance Rate", "week1": "20–30%", "week4": "35–45%", "day90": "45%+"}},
    {{"metric": "Post Impressions / Post", "week1": "500–1,500", "week4": "2,000–5,000", "day90": "5,000+"}},
    {{"metric": "DM Reply Rate", "week1": "10–15%", "week4": "20–30%", "day90": "30%+"}},
    {{"metric": "Discovery Calls Booked / Month", "week1": "1–2", "week4": "3–5", "day90": "5–10"}},
    {{"metric": "LinkedIn → Lead Conversion", "week1": "1–2%", "week4": "3–5%", "day90": "5%+"}}
  ]
}}

Generate exactly 15 checklist items, 8 milestones, 4 why-this-works reasons, and 6 metrics.
All content must be deeply specific to the niche — reference their ICP titles, industry jargon, and specific pain points.
"""

# ───────────────────────────────────────────────────────────
# SHEET 2 — Profile Optimization (EXPANDED: 25 headlines,
#           story arc, featured section strategy)
# ───────────────────────────────────────────────────────────
PROFILE_OPTIMIZATION_PROMPT = """
You are a LinkedIn growth strategist. Generate a COMPLETE Profile Optimization guide for Phase 1 (Days 1–7).
This is the COMPLETE SYSTEM tier — generate much more content than a starter kit.

**BUSINESS:** {business_name}
**SERVICES:** {services}
**ICP SUMMARY:** {icp_summary}
**POSITIONING:** {positioning_statement}
**PAIN POINTS:** {pain_points_list}

Return ONLY valid JSON:
{{
  "audit_checklist": [
    {{"item": "Headline", "question": "Does it name your ICP and promise a quantified outcome?"}},
    {{"item": "Banner Image", "question": "..."}},
    {{"item": "Profile Photo", "question": "..."}},
    {{"item": "About Section", "question": "..."}},
    {{"item": "Featured Section", "question": "..."}},
    {{"item": "Experience", "question": "..."}},
    {{"item": "Skills", "question": "..."}},
    {{"item": "Recommendations", "question": "..."}},
    {{"item": "Creator Mode", "question": "..."}},
    {{"item": "Custom URL", "question": "..."}}
  ],
  "headline_options": [
    {{"label": "Option 1 – ROI Focus", "text": "Full headline text with ICP + quantified outcome"}},
    {{"label": "Option 2 – Pain Point First", "text": "Full headline text leading with their biggest pain"}},
    {{"label": "Option 3 – Authority Frame", "text": "Full headline text establishing niche authority"}},
    {{"label": "Option 4 – Challenge/Provoke", "text": "Headline that challenges a common assumption"}},
    {{"label": "Option 5 – Specific Number", "text": "Headline with a specific stat or number"}},
    {{"label": "Option 6 – Question Hook", "text": "Headline framed as a compelling question"}},
    {{"label": "Option 7 – Outcome Only", "text": "Headline that leads with the outcome"}},
    {{"label": "Option 8 – Niche + Method", "text": "Headline naming the exact method or system"}},
    {{"label": "Option 9 – Before/After", "text": "Headline contrasting before and after"}},
    {{"label": "Option 10 – Social Proof", "text": "Headline leveraging social proof or client results"}},
    {{"label": "Option 11", "text": "..."}},
    {{"label": "Option 12", "text": "..."}},
    {{"label": "Option 13", "text": "..."}},
    {{"label": "Option 14", "text": "..."}},
    {{"label": "Option 15", "text": "..."}},
    {{"label": "Option 16", "text": "..."}},
    {{"label": "Option 17", "text": "..."}},
    {{"label": "Option 18", "text": "..."}},
    {{"label": "Option 19", "text": "..."}},
    {{"label": "Option 20", "text": "..."}},
    {{"label": "Option 21", "text": "..."}},
    {{"label": "Option 22", "text": "..."}},
    {{"label": "Option 23", "text": "..."}},
    {{"label": "Option 24", "text": "..."}},
    {{"label": "Option 25 – Wild Card", "text": "Creative/unconventional headline approach"}}
  ],
  "about_section": [
    {{"section": "Hook (Lines 1–2)", "instruction": "Open with the exact problem...", "example": "Full example text for this section"}},
    {{"section": "Agitate (Lines 3–6)", "instruction": "Describe the pain vividly...", "example": "..."}},
    {{"section": "Credibility Bridge", "instruction": "State what you do and who for...", "example": "..."}},
    {{"section": "What You Automate/Deliver", "instruction": "List the core stages you handle...", "example": "..."}},
    {{"section": "Quantified Outcome", "instruction": "Include the key stat and revenue math...", "example": "..."}},
    {{"section": "Who You Work With", "instruction": "Name the ICP types explicitly...", "example": "..."}},
    {{"section": "Soft CTA", "instruction": "Close with If you're a [ICP] dealing with X...", "example": "..."}}
  ],
  "story_arc": {{
    "opening_hook": "2-3 sentences: the moment you realized there was a problem in the industry",
    "struggle_phase": "2-3 sentences: what you tried, what didn't work, what you learned",
    "breakthrough": "2-3 sentences: the insight or system you developed",
    "mission_statement": "1-2 sentences: why you do this work now",
    "full_story": "Complete 6-8 sentence story arc combining all elements above"
  }},
  "skills": [
    "12 niche-specific LinkedIn skills to add (formatted as short skill names)"
  ],
  "featured_section": [
    {{"type": "Pinned Post", "idea": "specific post idea with case study or stat", "why": "Why this builds credibility"}},
    {{"type": "Lead Magnet Link", "idea": "specific lead magnet idea", "why": "Why this converts"}},
    {{"type": "Video Testimonial", "idea": "specific video idea", "why": "Why this builds trust"}},
    {{"type": "Case Study", "idea": "specific case study format", "why": "Why this demonstrates expertise"}},
    {{"type": "Newsletter", "idea": "specific newsletter topic", "why": "Why this nurtures leads"}},
    {{"type": "Carousel", "idea": "specific carousel topic", "why": "Why this gets saved/shared"}},
    {{"type": "Article", "idea": "specific article topic", "why": "Why this establishes authority"}},
    {{"type": "External Link", "idea": "specific external content", "why": "Why this adds value"}},
    {{"type": "PDF Guide", "idea": "specific downloadable guide", "why": "Why this captures leads"}},
    {{"type": "Event/Webinar", "idea": "specific event idea", "why": "Why this generates leads"}}
  ]
}}

CRITICAL: Generate exactly 25 unique headline options, 10 featured section ideas, and the full story arc.
All content must be deeply specific to their niche — use their ICP titles, industry terms, and specific outcomes.
"""

# ───────────────────────────────────────────────────────────
# SHEET 3 — Content Calendar (EXPANDED: 90-day, 36 posts,
#           50 hooks library, 15 story templates)
# ───────────────────────────────────────────────────────────
CONTENT_CALENDAR_PROMPT = """
You are a LinkedIn growth strategist. Generate a FULL 90-Day Content Calendar for Phase 2 (Days 8–21).
This is the COMPLETE SYSTEM — generate the full 90-day calendar with 36 posts.

**BUSINESS:** {business_name}
**SERVICES:** {services}
**ICP SUMMARY:** {icp_summary}
**CONTENT PILLARS:** {content_pillars}
**PAIN POINTS:** {pain_points_list}

Return ONLY valid JSON:
{{
  "pillars": [
    {{
      "name": "Pillar 1 – EDUCATION (40%)",
      "description": "1-2 sentence description of what this pillar covers for their niche",
      "examples": "3 example topic titles"
    }},
    {{
      "name": "Pillar 2 – PROOF & RESULTS (35%)",
      "description": "...",
      "examples": "3 example titles"
    }},
    {{
      "name": "Pillar 3 – ENGAGEMENT & OUTREACH (25%)",
      "description": "...",
      "examples": "3 example titles"
    }}
  ],
  "calendar": [
    {{
      "week": 1,
      "day": "Day 1",
      "pillar": "Education",
      "hook": "Full post hook (1-2 sentences that stop the scroll)",
      "key_points": "3 bullet points separated by newlines starting with →",
      "format": "Carousel / Text + Image / Poll / Long-form / Video",
      "cta": "Specific call-to-action for this post"
    }},
    {{
      "week": 1,
      "day": "Day 3",
      "pillar": "Proof",
      "hook": "...",
      "key_points": "...",
      "format": "...",
      "cta": "..."
    }}
  ],
  "hooks_library": [
    {{"category": "Pain Point Hooks", "hooks": ["Hook 1 text", "Hook 2 text", "Hook 3 text", "Hook 4 text", "Hook 5 text"]}},
    {{"category": "Curiosity Hooks", "hooks": ["Hook 1", "Hook 2", "Hook 3", "Hook 4", "Hook 5"]}},
    {{"category": "Contrarian Hooks", "hooks": ["Hook 1", "Hook 2", "Hook 3", "Hook 4", "Hook 5"]}},
    {{"category": "Story Hooks", "hooks": ["Hook 1", "Hook 2", "Hook 3", "Hook 4", "Hook 5"]}},
    {{"category": "Data/Number Hooks", "hooks": ["Hook 1", "Hook 2", "Hook 3", "Hook 4", "Hook 5"]}},
    {{"category": "Question Hooks", "hooks": ["Hook 1", "Hook 2", "Hook 3", "Hook 4", "Hook 5"]}},
    {{"category": "Bold Claim Hooks", "hooks": ["Hook 1", "Hook 2", "Hook 3", "Hook 4", "Hook 5"]}},
    {{"category": "Before/After Hooks", "hooks": ["Hook 1", "Hook 2", "Hook 3", "Hook 4", "Hook 5"]}},
    {{"category": "Mistake/Warning Hooks", "hooks": ["Hook 1", "Hook 2", "Hook 3", "Hook 4", "Hook 5"]}},
    {{"category": "Personal Story Hooks", "hooks": ["Hook 1", "Hook 2", "Hook 3", "Hook 4", "Hook 5"]}}
  ],
  "story_templates": [
    {{"name": "Template 1: The Origin Story", "structure": "Line by line structure with placeholders", "example": "Full example using their niche"}},
    {{"name": "Template 2: The Client Win", "structure": "...", "example": "..."}},
    {{"name": "Template 3: The Contrarian Take", "structure": "...", "example": "..."}},
    {{"name": "Template 4: The How-To Breakdown", "structure": "...", "example": "..."}},
    {{"name": "Template 5: The Painful Mistake", "structure": "...", "example": "..."}},
    {{"name": "Template 6: The Industry Myth", "structure": "...", "example": "..."}},
    {{"name": "Template 7: The Day-In-The-Life", "structure": "...", "example": "..."}},
    {{"name": "Template 8: The Framework Reveal", "structure": "...", "example": "..."}},
    {{"name": "Template 9: The Before/After", "structure": "...", "example": "..."}},
    {{"name": "Template 10: The Prediction", "structure": "...", "example": "..."}},
    {{"name": "Template 11: The Question Poll", "structure": "...", "example": "..."}},
    {{"name": "Template 12: The Listicle", "structure": "...", "example": "..."}},
    {{"name": "Template 13: The Hot Take", "structure": "...", "example": "..."}},
    {{"name": "Template 14: The Mini Case Study", "structure": "...", "example": "..."}},
    {{"name": "Template 15: The Challenge Post", "structure": "...", "example": "..."}}
  ],
  "post_frameworks": [
    {{
      "name": "Framework 1: PROBLEM → CAUSE → SOLUTION",
      "template": "Line 1: State the problem...\\nLine 2-3: Explain the real cause...\\nLine 4-5: Reveal your solution...\\nCTA: Ask a question or invite DMs"
    }},
    {{
      "name": "Framework 2: BEFORE → AFTER → BRIDGE",
      "template": "Before: Describe the painful state...\\nAfter: Show the transformed state...\\nBridge: What changed — your method"
    }},
    {{
      "name": "Framework 3: INSIGHT POST",
      "template": "Line 1: Counterintuitive hook...\\nLines 2-4: Expand with data or logic...\\nLines 5-7: Connect to ICP's world...\\nCTA: Invite engagement"
    }}
  ]
}}

CRITICAL INSTRUCTIONS:
- Generate exactly 36 calendar entries (3 posts/week × 12 weeks) with COMPLETE hooks and key points for every post.
- Generate exactly 50 hooks across 10 categories (5 per category).
- Generate exactly 15 story templates with full examples.
- All hooks must be scroll-stopping and deeply niche-specific.
- Vary formats across posts: Text, Carousel, Poll, Video, Image+Text, Document.
"""

# ───────────────────────────────────────────────────────────
# SHEET 4 — Outreach System (EXPANDED: 8 CR templates,
#           6 DM sequences, email sequence, Sales Nav guide)
# ───────────────────────────────────────────────────────────
OUTREACH_SYSTEM_PROMPT = """
You are a LinkedIn growth strategist. Generate a COMPLETE Outreach System for Phase 3 (Days 22–35).
This is the COMPLETE SYSTEM — generate significantly more templates and sequences.

**BUSINESS:** {business_name}
**SERVICES:** {services}
**ICP SUMMARY:** {icp_summary}
**POSITIONING:** {positioning_statement}
**PAIN POINTS:** {pain_points_list}

Return ONLY valid JSON:
{{
  "icp_worksheet": [
    {{
      "label": "ICP Profile A",
      "type": "ICP type name",
      "decision_maker": "Title",
      "org_type": "Organization type",
      "size": "Size metric",
      "volume": "Volume metric",
      "pain_points": "Top 3 pain points comma-separated",
      "search_filters": "LinkedIn Sales Navigator search filters to find this ICP"
    }},
    {{
      "label": "ICP Profile B",
      "type": "...",
      "decision_maker": "...",
      "org_type": "...",
      "size": "...",
      "volume": "...",
      "pain_points": "...",
      "search_filters": "..."
    }}
  ],
  "daily_quotas": [
    {{"activity": "Connection Requests Sent", "daily": "10–15", "weekly": "70–105", "notes": "Target specific titles at..."}},
    {{"activity": "Profile Views (Intentional)", "daily": "20–30", "weekly": "140–210", "notes": "View ICP profiles to trigger..."}},
    {{"activity": "Content Comments Left", "daily": "5–10", "weekly": "35–70", "notes": "Comment on niche posts..."}},
    {{"activity": "DMs Sent to Accepted Connections", "daily": "3–5", "weekly": "21–35", "notes": "Only after 48hr+ connection..."}},
    {{"activity": "Follow-Ups on Active Leads", "daily": "2–3", "weekly": "14–21", "notes": "Based on DM reply or post..."}}
  ],
  "connection_templates": [
    {{"label": "Template 1 – Pain Point Opener", "scenario": "Cold outreach to [ICP title]", "text": "Full connection request (under 300 chars)"}},
    {{"label": "Template 2 – Post Engagement", "scenario": "After they liked/commented", "text": "..."}},
    {{"label": "Template 3 – Mutual Connection", "scenario": "Shared connection reference", "text": "..."}},
    {{"label": "Template 4 – Event/Conference", "scenario": "After an industry event", "text": "..."}},
    {{"label": "Template 5 – Content Compliment", "scenario": "After reading their post", "text": "..."}},
    {{"label": "Template 6 – Industry News", "scenario": "Referencing a trending topic", "text": "..."}},
    {{"label": "Template 7 – Job Change Trigger", "scenario": "They recently changed roles", "text": "..."}},
    {{"label": "Template 8 – Company Growth", "scenario": "Their company hit a milestone", "text": "..."}}
  ],
  "dm_sequences": [
    {{
      "sequence_name": "Sequence 1 – Standard Nurture",
      "trigger": "After connection accepted",
      "messages": [
        {{"day": "Day 2", "label": "Soft Intro", "text": "Full DM (3-4 sentences)"}},
        {{"day": "Day 5", "label": "Value Drop", "text": "Full DM offering value"}},
        {{"day": "Day 9", "label": "Soft CTA", "text": "Full DM with call-to-action"}}
      ]
    }},
    {{
      "sequence_name": "Sequence 2 – Post Engager Follow-Up",
      "trigger": "After they engaged with your post",
      "messages": [
        {{"day": "Day 1", "label": "Thank + Connect", "text": "..."}},
        {{"day": "Day 3", "label": "Deeper Value", "text": "..."}},
        {{"day": "Day 7", "label": "Offer", "text": "..."}}
      ]
    }},
    {{
      "sequence_name": "Sequence 3 – Content Consumer",
      "trigger": "After they downloaded a lead magnet or viewed profile 3+ times",
      "messages": [
        {{"day": "Day 1", "label": "Acknowledge Interest", "text": "..."}},
        {{"day": "Day 3", "label": "Case Study Drop", "text": "..."}},
        {{"day": "Day 6", "label": "Direct CTA", "text": "..."}}
      ]
    }},
    {{
      "sequence_name": "Sequence 4 – Referral Ask",
      "trigger": "After a successful engagement or client win",
      "messages": [
        {{"day": "Day 1", "label": "Thank + Ask", "text": "..."}},
        {{"day": "Day 5", "label": "Make It Easy", "text": "..."}}
      ]
    }},
    {{
      "sequence_name": "Sequence 5 – Re-engagement",
      "trigger": "For cold connections who never replied",
      "messages": [
        {{"day": "Day 1", "label": "New Value Hook", "text": "..."}},
        {{"day": "Day 5", "label": "Direct Question", "text": "..."}},
        {{"day": "Day 10", "label": "Last Touch", "text": "..."}}
      ]
    }},
    {{
      "sequence_name": "Sequence 6 – Event/Webinar Invite",
      "trigger": "When promoting an event or workshop",
      "messages": [
        {{"day": "Day 1", "label": "Invite", "text": "..."}},
        {{"day": "Day 3", "label": "Reminder + Social Proof", "text": "..."}},
        {{"day": "Day 5", "label": "Last Chance", "text": "..."}}
      ]
    }}
  ],
  "email_sequence": [
    {{"label": "Email 1 – Day 1 (Intro)", "subject": "Subject line", "body": "Full 4-6 sentence email with CTA"}},
    {{"label": "Email 2 – Day 3 (Value)", "subject": "...", "body": "..."}},
    {{"label": "Email 3 – Day 5 (Case Study)", "subject": "...", "body": "..."}},
    {{"label": "Email 4 – Day 7 (Insight)", "subject": "...", "body": "..."}},
    {{"label": "Email 5 – Day 10 (Soft CTA)", "subject": "...", "body": "..."}}
  ],
  "sales_nav_guide": {{
    "search_filters": [
      {{"filter": "Job Title", "value": "Specific titles to search for this ICP"}},
      {{"filter": "Industry", "value": "..."}},
      {{"filter": "Company Size", "value": "..."}},
      {{"filter": "Geography", "value": "..."}},
      {{"filter": "Seniority Level", "value": "..."}},
      {{"filter": "Keywords", "value": "..."}}
    ],
    "saved_searches": [
      {{"name": "Search 1 – [ICP A] Active", "description": "Description and expected results"}},
      {{"name": "Search 2 – [ICP B] Growth", "description": "..."}},
      {{"name": "Search 3 – Trigger Events", "description": "..."}}
    ],
    "optimization_tips": [
      "5 specific tips for optimizing Sales Navigator for their niche"
    ]
  }}
}}

CRITICAL: Generate exactly 8 connection templates, 6 DM sequences, 5 email sequences, and complete Sales Nav guide.
All messages must feel personal and niche-specific — never generic.
"""

# ───────────────────────────────────────────────────────────
# SHEET 5 — Sales System (EXPANDED: complete discovery
#           script, 15 objections, meeting templates)
# ───────────────────────────────────────────────────────────
SALES_SYSTEM_PROMPT = """
You are a LinkedIn growth strategist. Generate a COMPLETE Sales System for Phase 4 (Days 36–50).
This is the COMPLETE SYSTEM — include full discovery scripts and 15 objection responses.

**BUSINESS:** {business_name}
**SERVICES:** {services}
**ICP SUMMARY:** {icp_summary}
**POSITIONING:** {positioning_statement}
**PRICING TIERS:** {pricing_tiers}

Return ONLY valid JSON:
{{
  "service_tiers": [
    {{
      "name": "TIER 1 – [NAME]",
      "price": "$X,XXX – $X,XXX\\n(One-Time)",
      "delivery": "X–X weeks",
      "included": "Item 1\\nItem 2\\nItem 3\\nItem 4",
      "best_for": "Who this tier is best for",
      "guarantee": "Specific guarantee statement"
    }},
    {{
      "name": "TIER 2 – [NAME]",
      "price": "...",
      "delivery": "...",
      "included": "...",
      "best_for": "...",
      "guarantee": "..."
    }},
    {{
      "name": "TIER 3 – [NAME]",
      "price": "...",
      "delivery": "...",
      "included": "...",
      "best_for": "...",
      "guarantee": "..."
    }}
  ],
  "discovery_script": {{
    "opening": {{
      "duration": "5 min",
      "script": "Word-for-word opening script: Hi [Name], thanks for taking the time... (5-8 sentences)"
    }},
    "diagnosis": {{
      "duration": "15 min",
      "script": "Word-for-word diagnosis section with transition phrases and probing questions (8-10 sentences with question marks)",
      "questions": [
        "10 specific discovery questions that uncover pain and frame the solution"
      ]
    }},
    "prescription": {{
      "duration": "10 min",
      "script": "Word-for-word prescription: Based on what you've shared... here's what I'd recommend... (6-8 sentences)"
    }},
    "close": {{
      "duration": "10 min",
      "script": "Word-for-word close: The investment for this is... (5-7 sentences including pricing transition)",
      "next_steps": "What to say when they say yes vs when they need to think about it"
    }}
  }},
  "objections": [
    {{"objection": "Common objection #1 in quotes", "response": "Full reframe response (4-5 sentences with acknowledge/reframe/proof/redirect)"}},
    {{"objection": "...", "response": "..."}},
    {{"objection": "...", "response": "..."}},
    {{"objection": "...", "response": "..."}},
    {{"objection": "...", "response": "..."}},
    {{"objection": "...", "response": "..."}},
    {{"objection": "...", "response": "..."}},
    {{"objection": "...", "response": "..."}},
    {{"objection": "...", "response": "..."}},
    {{"objection": "...", "response": "..."}},
    {{"objection": "...", "response": "..."}},
    {{"objection": "...", "response": "..."}},
    {{"objection": "...", "response": "..."}},
    {{"objection": "...", "response": "..."}},
    {{"objection": "...", "response": "..."}}
  ],
  "meeting_templates": [
    {{
      "name": "Template 1 – Discovery Call Booking",
      "subject": "Email subject line",
      "body": "Full booking email (4-6 sentences)",
      "calendar_link_note": "Where to place the Calendly/calendar link"
    }},
    {{
      "name": "Template 2 – Follow-Up After Discovery",
      "subject": "...",
      "body": "...",
      "calendar_link_note": "..."
    }},
    {{
      "name": "Template 3 – Proposal Send",
      "subject": "...",
      "body": "...",
      "calendar_link_note": "..."
    }}
  ],
  "value_calculator": {{
    "current_cost_items": [
      {{"item": "Current cost area 1", "typical_range": "$X,XXX–$XX,XXX/year"}},
      {{"item": "Current cost area 2", "typical_range": "..."}},
      {{"item": "Current cost area 3", "typical_range": "..."}},
      {{"item": "Current cost area 4", "typical_range": "..."}}
    ],
    "roi_formula": "Step-by-step ROI calculation specific to their service",
    "talking_points": [
      "3 specific ROI-focused talking points to use on calls"
    ]
  }}
}}

CRITICAL: Generate complete word-for-word discovery script with all 4 stages, exactly 15 objection responses,
3 meeting templates, and a value calculator. All content must use their industry language.
"""

# ───────────────────────────────────────────────────────────
# SHEET 6 — Lead Magnet Funnel (EXPANDED: 10 formats,
#           5 landing pages, 7-email sequence)
# ───────────────────────────────────────────────────────────
LEAD_MAGNET_FUNNEL_PROMPT = """
You are a LinkedIn growth strategist. Generate a COMPLETE Lead Magnet Funnel for Phase 5 (Days 51–65).
This is the COMPLETE SYSTEM — include 10 lead magnet formats, 5 landing pages, and 7 emails.

**BUSINESS:** {business_name}
**SERVICES:** {services}
**ICP SUMMARY:** {icp_summary}
**POSITIONING:** {positioning_statement}
**PAIN POINTS:** {pain_points_list}
**TIER 1 PRICE:** {tier1_price}

Return ONLY valid JSON:
{{
  "lead_magnet_formats": [
    {{
      "number": 1,
      "name": "Format Name",
      "description": "2-3 sentence description of this lead magnet idea",
      "format_type": "PDF / Checklist / Video / Template / Calculator / etc",
      "estimated_value": "$XX–$XXX",
      "difficulty": "Easy / Medium / Hard",
      "conversion_rate": "Expected opt-in rate estimate"
    }},
    ... (generate exactly 10)
  ],
  "landing_pages": [
    {{
      "name": "Landing Page 1 – [Primary Offer]",
      "headline": "Compelling headline with promise and timeframe",
      "sub_headline": "1-2 sentence supporting statement",
      "bullet_points": "✓ Bullet 1\\n✓ Bullet 2\\n✓ Bullet 3\\n✓ Bullet 4\\n✓ Bullet 5",
      "social_proof": "Testimonial quote with role and org type",
      "cta_button": "→ CTA button text",
      "post_cta": "Trust-building note about delivery",
      "urgency_element": "Scarcity or urgency trigger"
    }},
    ... (generate exactly 5)
  ],
  "email_sequence": [
    {{
      "label": "Email 1 – Immediate (Deliver)",
      "subject": "Subject line",
      "body": "Full 5-8 sentence email with clear CTA",
      "goal": "What this email is designed to achieve"
    }},
    {{
      "label": "Email 2 – Day 1 (Quick Win)",
      "subject": "...",
      "body": "...",
      "goal": "..."
    }},
    {{
      "label": "Email 3 – Day 2 (Deep Insight)",
      "subject": "...", "body": "...", "goal": "..."
    }},
    {{
      "label": "Email 4 – Day 4 (Case Study)",
      "subject": "...", "body": "...", "goal": "..."
    }},
    {{
      "label": "Email 5 – Day 6 (Objection Buster)",
      "subject": "...", "body": "...", "goal": "..."
    }},
    {{
      "label": "Email 6 – Day 8 (Social Proof + Offer)",
      "subject": "...", "body": "...", "goal": "..."
    }},
    {{
      "label": "Email 7 – Day 10 (Last Call)",
      "subject": "...", "body": "...", "goal": "..."
    }}
  ],
  "ad_targeting": {{
    "job_titles": "8+ specific titles comma-separated",
    "industries": "5+ industries comma-separated",
    "company_types": "5+ company types comma-separated",
    "company_size": "Employee range",
    "geography": "Geographic scope",
    "additional_signal": "LinkedIn groups or pages they follow"
  }},
  "distribution_plan": [
    {{"channel": "LinkedIn Profile Featured", "action": "Specific action to take", "frequency": "How often"}},
    {{"channel": "LinkedIn Posts", "action": "...", "frequency": "..."}},
    {{"channel": "DM Sequences", "action": "...", "frequency": "..."}},
    {{"channel": "Email Signature", "action": "...", "frequency": "..."}},
    {{"channel": "LinkedIn Articles", "action": "...", "frequency": "..."}}
  ]
}}

CRITICAL: Generate exactly 10 lead magnet formats, 5 landing page outlines, and 7 emails.
All content must be niche-specific and conversion-focused.
"""

# ───────────────────────────────────────────────────────────
# SHEET 7 — 90-Day Content Engine (EXPANDED: more topics,
#           advanced workflow)
# ───────────────────────────────────────────────────────────
CONTENT_ENGINE_PROMPT = """
You are a LinkedIn growth strategist. Generate a COMPLETE 90-Day Content Engine for Phase 6 (Days 66–80).
This is the COMPLETE SYSTEM — generate comprehensive content topics and advanced workflow.

**BUSINESS:** {business_name}
**SERVICES:** {services}
**ICP SUMMARY:** {icp_summary}
**CONTENT PILLARS:** {content_pillars}
**PAIN POINTS:** {pain_points_list}

Return ONLY valid JSON:
{{
  "research_methods": [
    {{"source": "LinkedIn Search", "instruction": "How to use this source for their niche specifically"}},
    {{"source": "Industry Publications / Regulatory Bodies", "instruction": "..."}},
    {{"source": "Reddit / Quora", "instruction": "..."}},
    {{"source": "Your Own Pipeline", "instruction": "..."}},
    {{"source": "Competitor Analysis", "instruction": "..."}}
  ],
  "content_topics": [
    {{
      "number": 1,
      "pillar": "Education",
      "topic": "Full topic/hook — scroll-stopping and niche-specific",
      "format": "Carousel / Long-form text / Poll / etc",
      "goal": "Awareness / Trust / Conversion / Reach / etc"
    }},
    ... (generate exactly 30 topics with good pillar distribution: 12 education, 10 proof, 8 engagement)
  ],
  "production_workflow": [
    {{"step": "Step 1 – Research", "day": "Monday", "time": "30 min", "action": "Identify 3 topics for the week..."}},
    {{"step": "Step 2 – Draft", "day": "Tuesday", "time": "60 min", "action": "Write all 3 posts..."}},
    {{"step": "Step 3 – Review", "day": "Wednesday", "time": "30 min", "action": "Edit for clarity..."}},
    {{"step": "Step 4 – Design", "day": "Wednesday", "time": "30 min", "action": "Create visuals if needed..."}},
    {{"step": "Step 5 – Schedule", "day": "Wednesday", "time": "15 min", "action": "Schedule posts..."}},
    {{"step": "Step 6 – Engage", "day": "Daily", "time": "20 min", "action": "Reply to all comments..."}}
  ],
  "engagement_strategy": {{
    "daily_routine": [
      {{"time": "Morning (15 min)", "action": "Specific engagement action"}},
      {{"time": "After Posting (10 min)", "action": "..."}},
      {{"time": "Evening (10 min)", "action": "..."}}
    ],
    "comment_templates": [
      "5 high-value comment templates for engaging on other people's posts"
    ],
    "engagement_targets": [
      "5 types of accounts to strategically engage with"
    ]
  }}
}}

CRITICAL: Generate exactly 30 content topics with scroll-stopping hooks specific to their niche.
Include the engagement strategy section with daily routine and comment templates.
"""

# ───────────────────────────────────────────────────────────
# SHEET 8 — Implementation Timeline (EXPANDED: day-by-day
#           full 90-day plan)
# ───────────────────────────────────────────────────────────
IMPLEMENTATION_TIMELINE_PROMPT = """
You are a LinkedIn growth strategist. Generate a COMPLETE Implementation Timeline for Phase 7 (Days 81–90) and the FULL 90-day day-by-day roadmap.
This is the COMPLETE SYSTEM — provide the complete day-by-day action plan.

**BUSINESS:** {business_name}
**SERVICES:** {services}
**ICP SUMMARY:** {icp_summary}
**POSITIONING:** {positioning_statement}

Return ONLY valid JSON:
{{
  "week1_days": [
    {{"day": "Day 1", "focus": "Profile Audit", "actions": "Specific actions for this day (reference sheets)", "time": "1.5 hrs"}},
    {{"day": "Day 2", "focus": "Profile Rewrite", "actions": "...", "time": "2 hrs"}},
    {{"day": "Day 3", "focus": "Profile Polish", "actions": "...", "time": "1 hr"}},
    {{"day": "Day 4", "focus": "ICP Research", "actions": "...", "time": "1.5 hrs"}},
    {{"day": "Day 5", "focus": "Outreach Launch", "actions": "...", "time": "45 min"}},
    {{"day": "Day 6", "focus": "First Post", "actions": "...", "time": "1 hr"}},
    {{"day": "Day 7", "focus": "Review & Plan", "actions": "...", "time": "30 min"}}
  ],
  "week2_days": [
    {{"day": "Day 8", "focus": "Content Batch", "actions": "...", "time": "..."}},
    {{"day": "Day 9", "focus": "...", "actions": "...", "time": "..."}},
    {{"day": "Day 10", "focus": "...", "actions": "...", "time": "..."}},
    {{"day": "Day 11", "focus": "...", "actions": "...", "time": "..."}},
    {{"day": "Day 12", "focus": "...", "actions": "...", "time": "..."}},
    {{"day": "Day 13", "focus": "...", "actions": "...", "time": "..."}},
    {{"day": "Day 14", "focus": "Week 2 Review", "actions": "...", "time": "..."}}
  ],
  "week3_days": [
    {{"day": "Day 15", "focus": "...", "actions": "...", "time": "..."}},
    {{"day": "Day 16", "focus": "...", "actions": "...", "time": "..."}},
    {{"day": "Day 17", "focus": "...", "actions": "...", "time": "..."}},
    {{"day": "Day 18", "focus": "...", "actions": "...", "time": "..."}},
    {{"day": "Day 19", "focus": "...", "actions": "...", "time": "..."}},
    {{"day": "Day 20", "focus": "...", "actions": "...", "time": "..."}},
    {{"day": "Day 21", "focus": "Week 3 Review", "actions": "...", "time": "..."}}
  ],
  "week4_days": [
    {{"day": "Day 22", "focus": "...", "actions": "...", "time": "..."}},
    {{"day": "Day 23", "focus": "...", "actions": "...", "time": "..."}},
    {{"day": "Day 24", "focus": "...", "actions": "...", "time": "..."}},
    {{"day": "Day 25", "focus": "...", "actions": "...", "time": "..."}},
    {{"day": "Day 26", "focus": "...", "actions": "...", "time": "..."}},
    {{"day": "Day 27", "focus": "...", "actions": "...", "time": "..."}},
    {{"day": "Day 28", "focus": "Month 1 Review", "actions": "...", "time": "..."}}
  ],
  "month2_weeks": [
    {{"week": "Week 5 (Days 29–35)", "theme": "Theme for this week", "daily_actions": "Daily actions summary", "key_milestone": "What should be achieved"}},
    {{"week": "Week 6 (Days 36–42)", "theme": "...", "daily_actions": "...", "key_milestone": "..."}},
    {{"week": "Week 7 (Days 43–49)", "theme": "...", "daily_actions": "...", "key_milestone": "..."}},
    {{"week": "Week 8 (Days 50–56)", "theme": "...", "daily_actions": "...", "key_milestone": "..."}}
  ],
  "month3_weeks": [
    {{"week": "Week 9 (Days 57–63)", "theme": "...", "daily_actions": "...", "key_milestone": "..."}},
    {{"week": "Week 10 (Days 64–70)", "theme": "...", "daily_actions": "...", "key_milestone": "..."}},
    {{"week": "Week 11 (Days 71–77)", "theme": "...", "daily_actions": "...", "key_milestone": "..."}},
    {{"week": "Week 12 (Days 78–84)", "theme": "...", "daily_actions": "...", "key_milestone": "..."}},
    {{"week": "Week 13 (Days 85–90)", "theme": "Final Sprint", "daily_actions": "...", "key_milestone": "..."}}
  ],
  "month1_goals": [
    {{"goal": "Profile Optimization", "description": "Specific niche-tailored goal description", "target": "✓ Complete by Day 7"}},
    {{"goal": "Network Growth", "description": "...", "target": "✓ Complete by Day 21"}},
    {{"goal": "Content Published", "description": "...", "target": "✓ Ongoing from Day 8"}},
    {{"goal": "Outreach Started", "description": "...", "target": "✓ Complete by Day 30"}},
    {{"goal": "First Discovery Calls", "description": "...", "target": "✓ Target by Day 30"}},
    {{"goal": "Lead Magnet Ready", "description": "...", "target": "✓ Complete by Day 28"}}
  ],
  "milestones_90day": [
    {{"period": "Days 1–7", "milestone": "Profile fully optimized"}},
    {{"period": "Days 8–14", "milestone": "..."}},
    {{"period": "Days 15–21", "milestone": "..."}},
    {{"period": "Days 22–30", "milestone": "..."}},
    {{"period": "Days 31–40", "milestone": "..."}},
    {{"period": "Days 41–50", "milestone": "..."}},
    {{"period": "Days 51–65", "milestone": "..."}},
    {{"period": "Days 66–80", "milestone": "..."}},
    {{"period": "Days 81–90", "milestone": "..."}}
  ]
}}

CRITICAL: Generate the complete day-by-day plan for all 28 days of Month 1,
plus weekly plans for Months 2-3 (9 more weeks). Include all milestones and goals.
"""

# ───────────────────────────────────────────────────────────
# SHEET 9 — Results Tracker (EXPANDED: advanced analytics,
#           A/B testing, benchmark comparison)
# ───────────────────────────────────────────────────────────
RESULTS_TRACKER_PROMPT = """
You are a LinkedIn growth strategist. Generate an ADVANCED Results Tracker with benchmarks, A/B testing framework, and testing calendar for their specific niche.
This is the COMPLETE SYSTEM — include advanced analytics and testing frameworks.

**BUSINESS:** {business_name}
**SERVICES:** {services}
**ICP SUMMARY:** {icp_summary}

Return ONLY valid JSON:
{{
  "benchmarks": [
    {{"metric": "Profile Views / Week", "good": "50–100", "great": "100–300", "exceptional": "300+"}},
    {{"metric": "Post Impressions / Post", "good": "500–2K", "great": "2K–7K", "exceptional": "7K+"}},
    {{"metric": "Engagement Rate (Likes+Comments/Impressions)", "good": "2–4%", "great": "4–8%", "exceptional": "8%+"}},
    {{"metric": "Connection Requests Sent / Week", "good": "50–70", "great": "70–100", "exceptional": "100+"}},
    {{"metric": "Connection Acceptance Rate", "good": "20–30%", "great": "30–45%", "exceptional": "45%+"}},
    {{"metric": "New Connections / Week", "good": "15–25", "great": "25–50", "exceptional": "50+"}},
    {{"metric": "DM Reply Rate", "good": "10–20%", "great": "20–35%", "exceptional": "35%+"}},
    {{"metric": "Discovery Calls Booked / Month", "good": "1–2", "great": "3–5", "exceptional": "5+"}},
    {{"metric": "LinkedIn → Booked Call Conv. Rate", "good": "1–2%", "great": "2–4%", "exceptional": "4%+"}},
    {{"metric": "Lead Magnet Sales / Month", "good": "2–5", "great": "5–15", "exceptional": "15+"}}
  ],
  "ab_testing_framework": [
    {{
      "test_name": "Headline Test",
      "variable_a": "Current headline",
      "variable_b": "New headline variant",
      "metric_to_track": "Profile views / week, connection acceptance rate",
      "duration": "2 weeks",
      "how_to_measure": "Compare profile views before/after changing headline"
    }},
    {{
      "test_name": "Hook Style Test",
      "variable_a": "...",
      "variable_b": "...",
      "metric_to_track": "...",
      "duration": "...",
      "how_to_measure": "..."
    }},
    {{
      "test_name": "Post Format Test",
      "variable_a": "...", "variable_b": "...",
      "metric_to_track": "...", "duration": "...", "how_to_measure": "..."
    }},
    {{
      "test_name": "Connection Request Style Test",
      "variable_a": "...", "variable_b": "...",
      "metric_to_track": "...", "duration": "...", "how_to_measure": "..."
    }},
    {{
      "test_name": "DM Opening Test",
      "variable_a": "...", "variable_b": "...",
      "metric_to_track": "...", "duration": "...", "how_to_measure": "..."
    }},
    {{
      "test_name": "CTA Test",
      "variable_a": "...", "variable_b": "...",
      "metric_to_track": "...", "duration": "...", "how_to_measure": "..."
    }}
  ],
  "testing_calendar": [
    {{"week": "Week 1-2", "test": "Headline A/B Test", "action": "Change headline, measure profile views"}},
    {{"week": "Week 3-4", "test": "Hook Style Test", "action": "..."}},
    {{"week": "Week 5-6", "test": "Post Format Test", "action": "..."}},
    {{"week": "Week 7-8", "test": "Connection Request Test", "action": "..."}},
    {{"week": "Week 9-10", "test": "DM Opening Test", "action": "..."}},
    {{"week": "Week 11-12", "test": "CTA Test", "action": "..."}}
  ],
  "benchmark_comparison": {{
    "industry_avg": [
      {{"metric": "LinkedIn Engagement Rate", "industry_avg": "1.5–2.5%", "your_target": "4–8%", "multiplier": "2-4x better"}},
      {{"metric": "Connection Acceptance", "industry_avg": "15–20%", "your_target": "30–45%", "multiplier": "2x better"}},
      {{"metric": "DM Response Rate", "industry_avg": "5–10%", "your_target": "20–35%", "multiplier": "3-4x better"}},
      {{"metric": "Cost Per Lead (vs. LinkedIn Ads)", "industry_avg": "$150–$300", "your_target": "$7–$13", "multiplier": "15-30x cheaper"}},
      {{"metric": "Content Reach", "industry_avg": "500–1K", "your_target": "2K–7K", "multiplier": "3-5x more"}}
    ]
  }}
}}

CRITICAL: Generate benchmarks, 6 A/B testing frameworks, 6-period testing calendar,
and industry benchmark comparison. All metrics should be realistic for their B2B niche.
"""
