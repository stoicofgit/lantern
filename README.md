# Lantern — Light in the dark. Never blinks.

Marketing brochure for **Lantern**, an AI operations control plane:
*set up by an expert, run by Hermes, controlled by you.*

Single-page interactive site, deployed free on Vercel (git push → auto-deploy).

## Local preview
```bash
python3 -m http.server 8765
# open http://127.0.0.1:8765
```

## Deploy
Push to `main` on `github.com/cwitherow/lantern`; Vercel builds the static `index.html` automatically.

> Deploy key: `~/.ssh/lantern-deploy` (repo-scoped). Remote uses the `github-lantern` SSH alias.
