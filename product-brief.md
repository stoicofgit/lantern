# Lantern — Autonomous Infrastructure Watch

> **Tagline:** *Light in the dark. Never blinks.*

## What it is
A 24/7 autonomous monitoring service for small ops teams, homelabs, and
client infrastructure. Config-driven, Telegram-native, and — uniquely —
watched from **two independent vantage points** so a single failure can't
blind it.

## The core differentiator (the real selling point)
Most monitors watch from *one* place. If that place loses its tunnel,
you get false "all green" or silent blind spots. Lantern watches from:

1. **Cloud vantage** — the Lantern VPS probes your endpoints over the
   Twingate overlay (or direct IP). Catches internet-facing outages.
2. **On-prem vantage** — an optional Raspberry Pi sits *inside* your LAN
   and probes the same targets over the local network, alerting via its
   own outbound internet. Catches LAN/connector failures even when the
   tunnel is fully down.

Result: a drop is confirmed from two directions before it pages you.
No single point of failure in the monitoring itself.

## How it behaves (proven in MVP)
- Probes every 5 min via cron (tunable).
- **Alerts only on state transition** (up ↔ down) — no storm, no noise.
- Multi-channel routing: cloud alerts → ops group; LAN alerts → owner DM.
- Opt-in auto-remediation (runs a command, re-checks) — off by default.
- Zero external dependencies (Python stdlib). One YAML file = onboarding.

## Tiered offer

| Tier | Target | Targets | Vantage points | Alerts | Reports | Price/mo | Setup |
|------|--------|---------|----------------|--------|---------|----------|-------|
| **Spark** | Solopreneur / homelab | ≤ 10 | Cloud only | Telegram group | Weekly summary | **$149** | $0 |
| **Beacon** | Small ops team / 1 client | ≤ 50 | Cloud + on-prem Pi probe | Group + owner DM, per-target routing | Daily + weekly | **$499** | $299 |
| **Lighthouse** | MSP / multi-site | Unlimited | Multi-site, redundant connectors | Full routing + dashboard | Custom cadence + SLA | **$1,200** | $999 |

### Margins (why this is the right business)
- All tiers delivered by the same cron + Telegram engine. Marginal cost
  per client ≈ $0 compute (runs on existing VPS, Twingate free tier).
- Pi for Beacon/Lighthouse: one-time ~$50 hardware, or client supplies one.
- **10 Beacon clients = $4,990/mo** for an afternoon of config work each.
  The leverage is in automation, not labor — exactly the $3/day ceiling's
  intended discipline.

## Onboarding (the whole sales motion)
1. **Intro call (15 min):** "Here's your infra, lighting up in real time."
   Live demo of the dashboard/Telegram from the MVP.
2. **Config drop:** client sends target list (IPs/ports/services). You add
   `targets:` blocks to `watchdog.yaml`. That's the entire setup.
3. **Channel wiring:** client joins the Telegram group (or gives a DM id).
   `alert_to` routes per their preference.
4. **Optional on-prem probe:** ship/configure a Pi → second connector +
   LAN-local probe. Two-vantage confirmation live.
5. **Go live:** cron runs; first real outage proves the value in the
   client's own channel.

## Current MVP state (shipped, verified)
- ✅ 9 targets monitored (6 VPS/wiki + 3 LAN over Twingate)
- ✅ State-transition alerts to Telegram (group + owner DM split)
- ✅ Cron-installed, runs unattended
- ⏳ On-prem Pi probe (next build) → unlocks Beacon/Lighthouse
- ⏳ Weekly report generator (cron → markdown summary) → tier requirement
- ⏳ Auto-remediation commands (per-target, client-approved)

## Files
- Engine: `scripts/watchdog/watchdog.py`
- Config: `scripts/watchdog/watchdog.yaml`
- State: `scripts/watchdog/.watchdog_state.json`
- Log: `scripts/watchdog/watchdog.log`

---
*Not financial advice — operational strategy, not investment recommendation.*
