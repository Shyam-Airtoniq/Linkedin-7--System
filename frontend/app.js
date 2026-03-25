/* ═══════════════════════════════════════════════════════
   90-Day LinkedIn COMPLETE SYSTEM — App Logic
   Points at localhost:8001 for local use
   ═══════════════════════════════════════════════════════ */

// ─── Config ───
const API_BASE = "http://localhost:8001";

const STEPS = [
  { name: "analysis", label: "Strategic Analysis", step: 1 },
  { name: "dashboard", label: "Master Dashboard", step: 2 },
  { name: "profile", label: "Profile Optimization (25 Headlines)", step: 3 },
  { name: "content_calendar", label: "90-Day Content Calendar (36 Posts)", step: 4 },
  { name: "outreach", label: "Outreach System (8 CR + 6 DM)", step: 5 },
  { name: "sales", label: "Sales System (15 Objections)", step: 6 },
  { name: "lead_magnet", label: "Lead Magnet Funnel (10 Formats)", step: 7 },
  { name: "content_engine", label: "Content Engine (30 Topics)", step: 8 },
  { name: "implementation", label: "Implementation (Day-by-Day)", step: 9 },
  { name: "tracker", label: "Advanced Results Tracker", step: 10 },
  { name: "build", label: "Building Excel File", step: 11 },
];

// ─── DOM Elements ───
const form = document.getElementById("generateForm");
const btnGenerate = document.getElementById("btnGenerate");
const sheetsPreview = document.getElementById("sheetsPreview");
const progressCard = document.getElementById("progressCard");
const resultCard = document.getElementById("resultCard");
const errorCard = document.getElementById("errorCard");
const progressBar = document.getElementById("progressBar");
const progressPct = document.getElementById("progressPercent");
const progressStep = document.getElementById("progressStep");
const stepList = document.getElementById("stepList");
const timeEstimate = document.getElementById("timeEstimate");
const btnDownload = document.getElementById("btnDownload");
const btnNew = document.getElementById("btnNewGeneration");
const btnRetry = document.getElementById("btnRetry");
const insightsSection = document.getElementById("insightsSection");

// ─── State ───
let downloadBlob = null;
let downloadName = "";

// ─── Particles ───
function createParticles() {
  const container = document.getElementById("bgParticles");
  const colors = ["rgba(245,158,11,0.3)", "rgba(52,211,153,0.25)", "rgba(168,85,247,0.2)"];
  for (let i = 0; i < 30; i++) {
    const p = document.createElement("div");
    p.classList.add("particle");
    const size = Math.random() * 4 + 2;
    p.style.width = size + "px";
    p.style.height = size + "px";
    p.style.left = Math.random() * 100 + "%";
    p.style.background = colors[Math.floor(Math.random() * colors.length)];
    p.style.animationDuration = (Math.random() * 15 + 10) + "s";
    p.style.animationDelay = (Math.random() * 10) + "s";
    container.appendChild(p);
  }
}
createParticles();

// ─── Step List UI ───
function renderStepList(activeIndex = -1) {
  stepList.innerHTML = STEPS.map((s, i) => {
    let cls = "pending";
    let icon = "○";
    if (i < activeIndex) { cls = "done"; icon = "✓"; }
    else if (i === activeIndex) { cls = "active"; icon = "↻"; }
    return `<div class="step-item ${cls}">
      <span class="step-icon">${icon}</span>
      <span>Step ${s.step}: ${s.label}</span>
    </div>`;
  }).join("");
}

function updateProgress(stepIndex) {
  const pct = Math.round(((stepIndex + 1) / STEPS.length) * 100);
  progressBar.style.width = pct + "%";
  progressPct.textContent = pct + "%";
  progressStep.textContent = STEPS[stepIndex]?.label || "Processing...";
  renderStepList(stepIndex);

  // Complete System takes ~25s per step (richer content)
  const remaining = (STEPS.length - stepIndex - 1) * 25;
  if (remaining > 0) {
    const mins = Math.ceil(remaining / 60);
    timeEstimate.textContent = `⏱️ ~${mins} minute${mins > 1 ? "s" : ""} remaining`;
  } else {
    timeEstimate.textContent = "⏱️ Almost done...";
  }
}

// ─── API Helpers ───
async function postJSON(endpoint, body) {
  const res = await fetch(`${API_BASE}${endpoint}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  if (!res.ok) {
    const errBody = await res.text();
    throw new Error(`API error ${res.status}: ${errBody.slice(0, 300)}`);
  }
  return res;
}

async function fetchAnalysis(businessInfo) {
  const res = await postJSON("/api/generate/analysis", businessInfo);
  return res.json();
}

async function fetchSheet(businessInfo, analysis, stepName) {
  const res = await postJSON("/api/generate/sheet", {
    ...businessInfo,
    analysis: analysis,
    step_name: stepName,
  });
  return res.json();
}

async function fetchBuild(businessName, name, email, analysis, sheets) {
  const res = await postJSON("/api/generate/build", {
    business_name: businessName,
    name: name,
    email: email,
    analysis: analysis,
    sheets: sheets,
  });
  return res.blob();
}

// ─── Insights Preview ───
function showInsights(analysis) {
  if (!analysis) return;
  const icpEl = document.getElementById("insightICP");
  const pricingEl = document.getElementById("insightPricing");
  const posEl = document.getElementById("insightPositioning");

  const icps = analysis.icp_profiles || [];
  icpEl.innerHTML = icps.slice(0, 2).map(p =>
    `<p><strong>${p.name || p.label}</strong> — ${p.title || ""} at ${p.org || ""}</p>
     <p style="font-size:0.82rem;color:var(--text-muted);margin-bottom:0.8rem;">${p.primary_pain || ""}</p>`
  ).join("");

  const pr = analysis.pricing || {};
  pricingEl.innerHTML = Object.values(pr).slice(0, 3).map(t =>
    `<p><strong>${t.name || ""}</strong></p>
     <p style="font-size:0.82rem;color:var(--accent-green);margin-bottom:0.6rem;">${t.price_range || ""}</p>`
  ).join("");

  const pos = analysis.positioning || {};
  posEl.innerHTML = `<p style="font-style:italic;color:var(--text-secondary);margin-bottom:0.8rem;">"${pos.statement || ""}"</p>`;
  const diffs = pos.differentiators || [];
  posEl.innerHTML += diffs.map(d =>
    `<p><strong>${d.label}</strong>: ${d.text}</p>`
  ).join("");

  insightsSection.classList.remove("hidden");
}

// ─── Main Generation Flow ───
async function runGeneration(businessInfo) {
  sheetsPreview.classList.add("hidden");
  resultCard.classList.add("hidden");
  errorCard.classList.add("hidden");
  insightsSection.classList.add("hidden");
  progressCard.classList.remove("hidden");
  btnGenerate.disabled = true;
  btnGenerate.classList.add("loading");
  updateProgress(0);

  let analysis = null;
  const sheets = {};

  try {
    // Step 1: Analysis
    updateProgress(0);
    const analysisRes = await fetchAnalysis(businessInfo);
    analysis = analysisRes.analysis;

    // Steps 2-10: Individual sheets
    const sheetSteps = STEPS.slice(1, -1);
    for (let i = 0; i < sheetSteps.length; i++) {
      updateProgress(i + 1);
      const sheetRes = await fetchSheet(businessInfo, analysis, sheetSteps[i].name);
      sheets[sheetSteps[i].name] = sheetRes.data;
    }

    // Step 11: Build Excel
    updateProgress(STEPS.length - 1);
    const blob = await fetchBuild(
      businessInfo.business_name || "My Business",
      businessInfo.name || "",
      businessInfo.email || "",
      analysis, sheets
    );

    // Done!
    downloadBlob = blob;
    const safeName = (businessInfo.business_name || "LinkedIn_Complete_System")
      .replace(/[^a-zA-Z0-9_-]/g, "_");
    downloadName = `${safeName}_90Day_LinkedIn_Complete_System.xlsx`;

    progressCard.classList.add("hidden");
    resultCard.classList.remove("hidden");
    showInsights(analysis);

  } catch (err) {
    console.error("Generation failed:", err);
    progressCard.classList.add("hidden");
    errorCard.classList.remove("hidden");
    document.getElementById("errorMessage").textContent = err.message || "Something went wrong. Please try again.";
  } finally {
    btnGenerate.disabled = false;
    btnGenerate.classList.remove("loading");
  }
}

// ─── Event Listeners ───
form.addEventListener("submit", (e) => {
  e.preventDefault();

  const services = document.getElementById("services").value.trim();
  if (services.length < 20) {
    document.getElementById("services").focus();
    return;
  }

  const linkedinStatus = document.getElementById("linkedinStatus").value;
  if (!linkedinStatus) {
    document.getElementById("linkedinStatus").focus();
    return;
  }

  const additionalCtx = document.getElementById("additionalContext").value.trim();
  const contextParts = [`Current LinkedIn Status: ${linkedinStatus}`];
  if (additionalCtx) contextParts.push(additionalCtx);

  const businessInfo = {
    business_name: document.getElementById("businessName").value.trim() || "My Business",
    name: document.getElementById("userName").value.trim(),
    email: document.getElementById("userEmail").value.trim(),
    services: services,
    target_industry: document.getElementById("targetIndustry").value.trim() || null,
    additional_context: contextParts.join(". "),
  };

  runGeneration(businessInfo);
});

btnDownload.addEventListener("click", () => {
  if (!downloadBlob) return;
  const url = URL.createObjectURL(downloadBlob);
  const a = document.createElement("a");
  a.href = url;
  a.download = downloadName;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
});

function resetUI() {
  resultCard.classList.add("hidden");
  errorCard.classList.add("hidden");
  progressCard.classList.add("hidden");
  insightsSection.classList.add("hidden");
  sheetsPreview.classList.remove("hidden");
  downloadBlob = null;
  downloadName = "";
}

btnNew.addEventListener("click", resetUI);
btnRetry.addEventListener("click", () => {
  resetUI();
  form.dispatchEvent(new Event("submit"));
});
