# 🚀 LinkedIn Complete System — Backend API

AI-powered LinkedIn growth system that generates a customized 11-sheet Excel workbook using Claude.

## Quick Start (Docker)

### 1. Clone & configure

```bash
git clone https://github.com/Shyam-Airtoniq/Linkedin-7--System.git
cd Linkedin-7--System
```

Create a `.env` file:

```env
ANTHROPIC_API_KEY=sk-ant-your-key-here

# Webhook — Excel + user info is POSTed here after generation
WEBHOOK_URL=https://vmi2632825.contaboserver.net/webhook/b02fb702-2d5c-42c6-8469-80059737e99e

# For CLI mode (run.py) — these are read from env vars
BUSINESS_NAME=My Business
NAME=John Doe
EMAIL=john@example.com
SERVICES=We help B2B service providers generate leads using LinkedIn automation and content strategy.
TARGET_INDUSTRY=B2B SaaS
LINKEDIN_STATUS=1
```

### 2. Run with Docker Compose

```bash
docker compose up -d --build
```

The API will be live at **http://your-server-ip:9000**

- Swagger docs: `http://your-server-ip:9000/docs`
- Health check: `http://your-server-ip:9000/api/health`

### 3. Check logs

```bash
docker compose logs -f
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/health` | Health check |
| POST | `/api/generate/analysis` | Step 1: Strategic analysis |
| POST | `/api/generate/sheet` | Steps 2-10: Generate individual sheets |
| POST | `/api/generate/build` | Step 11: Build Excel, POST to webhook, return file |

### Step-by-step flow:

```
1. POST /api/generate/analysis     → returns { analysis }
2. POST /api/generate/sheet        → { step_name: "dashboard", analysis, ... }
3. POST /api/generate/sheet        → { step_name: "profile", analysis, ... }
   ... repeat for all 9 sheets ...
10. POST /api/generate/sheet       → { step_name: "tracker", analysis, ... }
11. POST /api/generate/build       → returns Excel file + POSTs to webhook
```

### Request body for `/api/generate/analysis`:

```json
{
  "business_name": "9Gravity",
  "name": "Shyam",
  "email": "shyam@9gravity.io",
  "services": "We help B2B service providers generate leads...",
  "target_industry": "B2B SaaS",
  "additional_context": "LinkedIn Status: Have some presence"
}
```

### Request body for `/api/generate/sheet`:

```json
{
  "business_name": "9Gravity",
  "services": "We help B2B service providers generate leads...",
  "analysis": { "...from step 1..." },
  "step_name": "dashboard"
}
```

Valid `step_name` values: `dashboard`, `profile`, `content_calendar`, `outreach`, `sales`, `lead_magnet`, `content_engine`, `implementation`, `tracker`

### Request body for `/api/generate/build`:

```json
{
  "business_name": "9Gravity",
  "name": "Shyam",
  "email": "shyam@9gravity.io",
  "analysis": { "...from step 1..." },
  "sheets": { "dashboard": {...}, "profile": {...}, ... }
}
```

---

## CLI Mode (One-shot generation)

Instead of the API, you can run a one-shot generation via `run.py`. It reads all inputs from env vars:

```bash
# Using Docker
docker compose run --rm linkedin-system python run.py

# Without Docker
uv run python run.py
```

The Excel file is saved to `outputs/` and POSTed to the webhook.

---

## Webhook

After every Excel generation (both API and CLI), the system POSTs to the webhook URL with:

- `file` — the Excel file (multipart)
- `name` — user's name
- `email` — user's email
- `business_name` — the business name

Configure the URL via `WEBHOOK_URL` in `.env`.

---

## Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `ANTHROPIC_API_KEY` | ✅ | — | Claude API key |
| `WEBHOOK_URL` | No | (n8n webhook) | Webhook to POST Excel + user info |
| `BUSINESS_NAME` | CLI only | My Business | Business name |
| `NAME` | CLI only | — | User's name |
| `EMAIL` | CLI only | — | User's email |
| `SERVICES` | CLI only | — | Services description (min 20 chars) |
| `TARGET_INDUSTRY` | CLI only | — | Target industry |
| `LINKEDIN_STATUS` | CLI only | 1 | 1=Scratch, 2=Some presence, 3=Established |

---

## What's Generated (11 Sheets)

| Sheet | Content |
|-------|---------|
| 0. Strategic Foundation | ICP profiles, pricing, positioning, pain points |
| 1. Master Dashboard | 90-day timeline, checklist, milestones |
| 2. Profile Optimization | 25 headlines, story arc, 10 featured ideas |
| 3. Content Calendar | 36 posts, 50 hooks, 15 story templates |
| 4. Outreach System | 8 CR templates, 6 DM sequences, email seq, Sales Nav |
| 5. Sales System | Discovery script, 15 objections, meeting templates |
| 6. Lead Magnet Funnel | 10 formats, 5 landing pages, 7-email sequence |
| 7. Content Engine | 30 topics, engagement strategy |
| 8. Implementation | Day-by-day 90-day plan |
| 9. Results Tracker | A/B testing, benchmarks, testing calendar |
| 10. Upgrade Path | → Done-With-You ($1,999) |
