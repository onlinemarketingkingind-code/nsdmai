# NSDM AI — Eva Website Intelligence Agent

> Google for Startups AI Agents Challenge — Track 3: Refactor for Google Cloud Marketplace

## 🔗 Live Links
- **Platform:** https://nsdmai.com
- **Cloud Run API:** https://eva-api-244525299670.asia-south1.run.app
- **Reports API:** https://eva-api-244525299670.asia-south1.run.app/eva/reports

## 🤖 What is Eva?
Eva is an autonomous AI agent that takes a single input — a website URL — and independently:
- Crawls the full website (not just homepage)
- Analyses SEO + AEO + GEO visibility simultaneously
- Checks Google Search Console for real traffic data
- Identifies competitor gaps and opportunities
- Generates a 360 audit report (PDF + JSON)
- Stores reports on Google Cloud Storage automatically
- Delivers findings via Google Cloud TTS voice
- Answers follow-up questions by voice in real time

Eva doesn't just respond. **Eva acts.**

## ☁️ Google Cloud Services Used
| Service | Purpose |
|---|---|
| Google Cloud Run | Eva API Gateway — deployed asia-south1 |
| Google Cloud Storage | Audit report storage PDF + JSON |
| Google Cloud Text-to-Speech | Eva voice output |
| Google Cloud Speech-to-Text | Eva voice input |
| Google Search Console API | Real traffic data in audits |

## 🏗️ Architecture
## 📊 What Makes Eva Different
| Traditional SEO Tools | Eva Agent |
|---|---|
| Homepage scan only | Full site crawl |
| SEO only | SEO + AEO + GEO |
| Text reports | Voice consultation |
| Generic advice | Business direction |
| No AI visibility | AI search optimisation |
| $99-149/mo each | All-in-one $49-149/mo |

## 🚀 Cloud Run API Endpoints
```bash
# Health check — shows all Google services
GET https://eva-api-244525299670.asia-south1.run.app/

# List all stored audit reports from GCS
GET https://eva-api-244525299670.asia-south1.run.app/eva/reports
```

## 🛠️ Tech Stack
- **Frontend:** React PWA (Convex backend)
- **AI Intelligence:** Claude API (Anthropic)
- **Voice Input:** Google Cloud Speech-to-Text
- **Voice Output:** Google Cloud Text-to-Speech
- **Report Storage:** Google Cloud Storage
- **API Gateway:** Google Cloud Run (Python/Flask)
- **SEO Data:** Google Search Console API

## 💰 Pricing
| Tier | Price | Features |
|---|---|---|
| Free | $0 | Basic audit, limited scans |
| Pro | $49/month | Full SEO+AEO+GEO, Eva voice |
| Agency | $149/month | Multi-site, white label reports |

## 👤 Founder
**Narayan Shukla** — Founder, NSDM AI
- 11 years digital marketing experience
- 500+ clients — UK, US, UAE, Australia, India
- Pune, Maharashtra, India
- nsdmai.com
