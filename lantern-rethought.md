# Lantern — Re-thought MVP (Pi-free)

> **Tagline:** *Light in the dark. Never blinks.*
> **New one-liner:** *Your AI operations, lit up — set up by an expert, run by Hermes, controlled by you.*

## The reframe (Pi is gone, permanently)
Lantern is **no longer** "a watchdog with a Raspberry Pi inside your LAN giving a second vantage point." That idea is deleted from the mental model.

Lantern is now:

> **A beautiful, client-facing control plane for the Hermes automations you set up per business — plus your own operator console to run them all.**

The *product* is **visibility + control**, delivered turnkey. Hermes does the automation work in the background (watchdog, reports, cron jobs — already running today). Lantern is the face the client actually opens, trusts, and renews for.

## Why this is the right product (and why no Pi was ever needed)
- The watchdog + cron automations **already run** (9 targets live, split-channel Telegram alerts, unattended cron). The missing layer was never hardware — it was the **interface**. That is the fastest, cheapest, highest-perceived-value thing to build.
- SMB buyers don't want to read a Telegram bot or edit `watchdog.yaml`. They want a console that says *"your business is lit"* or *"here's what needs you."*
- You sell the **setup** ("I'll set it up"), bill a recurring fee, and own the relationship. Lantern is what makes the monthly fee feel inevitable instead of "what am I paying for?"

## The two surfaces
**1. Client Console** (per business — what each client logs into)
- **Overview** — glow rings per automation, aggregate "all lit" status, last activity, next run.
- **Automations** — what's set up for them: run history, schedule, on/off toggle, **Run now**.
- **Activity** — human-readable chronological log ("Lantern checked 9 endpoints · all green").
- **Incidents** — alerts surfaced as a clean panel (ack/resolve), not scattered chat noise.
- **Reports** — generated digests, viewable + downloadable in-app.
- **Requests** — "Ask Lantern to automate something new" → lands in your operator queue.
- **Settings** — notification prefs, accent color.

**2. Operator Console** (overall — what you use to run the fleet)
- **Fleet** — every client, aggregate health, "who needs attention" triage.
- **Client detail** — drill into any client's console.
- **Intake wizard** — onboarding: business info → pick template(s) → writes config → provision login.
- **Templates** — reusable automation blueprints (watchdog, weekly report, etc.) you clone per client.
- **Request queue** — incoming client "automate this" asks, fulfilled here.

## Instantly-sellable features (priority order — what closes deals fastest)
1. **The live console itself** — watching their automations light up in real time. Pure demo gravity.
2. **Run-now + activity log** — makes the product feel *alive* and tangible, not a black box.
3. **In-app incidents panel** — replaces scattered Telegram alerts with one clean "here's what broke, here's what I did."
4. **Weekly report, in-app** — the artifact they screenshot to their boss / show peers.
5. **Request-a-new-automation** — turns software into a relationship and an upsell engine.
6. *(later)* Multi-client fleet view, intake wizard, per-client branding, recommendations/upsell nudges.

## Aesthetic direction (cinematic, cohesive, "the site was great" bar)
- Dark, cinematic base (reuse the SMB-page palette: bg `#0a0a0f`, indigo `#6366f1`, green `#22c55e`, amber `#f59e0b`).
- **Lantern-glow motif as the core metaphor:** health = *light*. A lit lantern = healthy; dim/red = needs attention. Status isn't a checkbox — it's luminosity. Overview screen = a row of glowing lanterns.
- Smooth fade-up / pulse-glow motion language (already proven on the landing page). Generous whitespace, Inter type, rounded surfaces.
- Mobile-responsive — clients check it on phones.

## Architecture (practical & realistic — leverages what exists)
- **Frontend:** Next.js + Tailwind + shadcn/ui. (Fast path: a Vite React SPA or static prototype if we want zero-build first.) Talks to the API over JSON.
- **Backend:** FastAPI (already proven on VPS at `127.0.0.1:9301` for File Vault). Exposes `/fleet`, `/client/{id}/overview`, `/automations`, `/run`, `/activity`, `/incidents`, `/reports`, `/requests`.
- **Data:** SQLite for MVP (clients, users, requests, reports, run-history). The backend reads existing Hermes state (`.watchdog_state.json`, cron logs) and normalizes it.
- **Auth:** App-level, per-client logins with roles (`client` vs `operator`). bcrypt + session cookies. (Not Cloudflare Access — that's per-user GitHub OAuth, wrong model for per-org client logins. Keep CF Access only for any publicly-indexed marketing property.)
- **Realtime:** polling (5–15s) or SSE. Polling is simplest and realistic for MVP.
- **Deploy:** VPS behind nginx + Cloudflare (same pattern as File Vault). Bound to loopback + Twingate, never described by public IP.

## Build sequence (see To-do list)
Concept lock → Backend API + data model → Auth (operator/client) → Operator Console → Client Console → Wire real Hermes automations → Aesthetic/UX polish → Deploy secure → End-to-end onboarding → First pilot client.

---
*Not financial advice — operational strategy, not investment recommendation.*
