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
