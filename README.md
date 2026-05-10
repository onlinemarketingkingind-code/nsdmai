# Eva by NSDM AI - Self-Learning Marketing Consultant AI

[![Google Cloud](https://img.shields.io/badge/Google%20Cloud-Production-4285F4?logo=google-cloud)](https://cloud.google.com)
[![Product Hunt](https://img.shields.io/badge/Product%20Hunt-%235-DA552F?logo=product-hunt)](https://producthunt.com)
[![Status](https://img.shields.io/badge/Status-Live-success)](https://nsdmai.com)
[![Hackathon](https://img.shields.io/badge/Hackathon-Google%20Cloud%20Rapid%20Agent%202026-orange)]()

> **Google Cloud Rapid Agent Hackathon 2026**  
> Building autonomous AI agents for real-world marketing challenges

---

## 🎯 Try Eva Now

**🌐 Live Demo:** [nsdmai.com](https://nsdmai.com)  
**⚡ Quick Start:** Click "Eva Scan" → Enter any website URL → Get full audit in 45 seconds

**Cloud Infrastructure:**
- **Main API:** https://eva-api-244525299670.asia-south1.run.app
- **Reports API:** https://eva-api-244525299670.asia-south1.run.app/eva/reports
- **GCS Storage:** https://storage.googleapis.com/nsdmai-audit-reports

**📹 Demo Video:** [YouTube Link - Coming Soon]

---

## 🤖 What is Eva?

Eva is an **autonomous AI marketing consultant** that takes a single input — a website URL — and independently executes a comprehensive visibility analysis across 10 dimensions.

### **Eva doesn't just respond. Eva acts.**

**Single Input:** Website URL  
**Autonomous Output:** 
- ✅ Full-site crawl (not just homepage)
- ✅ SEO + AEO + GEO visibility analysis simultaneously
- ✅ Google Search Console integration for real traffic data
- ✅ Competitor gap analysis and benchmarking
- ✅ 360° audit report (PDF + JSON) stored on Google Cloud Storage
- ✅ Voice-narrated findings via Google Cloud Text-to-Speech
- ✅ Real-time follow-up Q&A with conversational memory

**Zero human intervention. 45 seconds average execution time.**

---

## 🏆 Challenge Context

**Hackathon:** Google Cloud Rapid Agent Hackathon 2026  
**Track:** Machine Learning/AI + Real-World Challenges  
**Challenge Question:** How can AI agents solve real business problems autonomously?

### **Eva's Answer:**

Replace $5,000+ marketing consultant audits with a 45-second autonomous AI agent that analyzes, reports, and consults via voice—powered entirely by Google Cloud infrastructure.

### **Why Eva is a Real-World Agent:**

✅ **Truly Autonomous** - Takes one input (URL), executes 10+ complex tasks independently  
✅ **Production Deployment** - Serving 50+ real users, not a hackathon demo  
✅ **Enterprise Security** - 27 security layers from day one  
✅ **Google Cloud Native** - Speech-to-Text, Text-to-Speech, Cloud Run, Storage, Search Console API  
✅ **Real Business Impact** - Replaces $5K audits, saves 2-3 weeks of consultant time  
✅ **Self-Learning** - Improves from every scan and conversation  
✅ **Market Validation** - Product Hunt #5, featured on Wired Business, twelve.tools  

---

## ☁️ Google Cloud Services Used

| Service | Purpose | Implementation |
|---------|---------|----------------|
| **Google Cloud Run** | Eva API Gateway | Deployed: `asia-south1` - Auto-scaling containerized backend |
| **Google Cloud Storage** | Audit Report Storage | PDF + JSON reports, publicly accessible via signed URLs |
| **Google Cloud Text-to-Speech** | Eva Voice Output | Natural voice narration of findings in 20+ languages |
| **Google Cloud Speech-to-Text** | Eva Voice Input | Real-time voice command processing |
| **Google Search Console API** | Real Traffic Data | Live website performance metrics in audits |
| **Google Cloud IAM** | Security & Access Control | Role-based permissions, service account isolation |

---

## 🏗️ Architecture
User → nsdmai.com (React PWA)
↓
Eva AI Agent (Orchestrator)
↓
├─→ Google Cloud Speech-to-Text → Voice Input
├─→ Google Cloud Text-to-Speech → Voice Output
├─→ Google Search Console API → Traffic Data
├─→ Claude API (Anthropic) → AI Intelligence & Synthesis
└─→ Custom Analysis Engines
├─→ Full-Site Crawler
├─→ SEO Scoring (200+ signals)
├─→ AEO Analysis (Answer Engine Optimization)
├─→ GEO Analysis (Generative Engine Optimization)
├─→ Semantic Understanding (NLP)
└─→ Entity Extraction
↓
Google Cloud Storage → Reports Saved (PDF + JSON)
↓
Google Cloud Run API Gateway
eva-api-244525299670.asia-south1.run.app

---

## 🤖 Agent Workflow (Autonomous Execution)

**Input:** Website URL (voice or text)  
**Output:** Complete audit report + voice consultation + strategic action plan

### **Eva's 7-Step Autonomous Process:**

**1. Domain Validation** (2-3 seconds)
- Verify URL accessibility
- DNS resolution check
- SSL certificate validation
- Robots.txt compliance check

**2. Full-Site Crawl** (10-15 seconds)
- Discover all pages (intelligent depth limiting)
- Respect rate limits and politeness delays
- Extract content, metadata, structure
- Duplicate detection and deduplication

**3. Parallel Analysis Pipelines** (15-20 seconds)

Eva runs **10 analysis dimensions simultaneously**:

| Dimension | What Eva Analyzes |
|-----------|-------------------|
| **SEO** | 200+ ranking signals, technical health, on-page optimization |
| **AEO** | Structured data quality, featured snippet eligibility, FAQ formatting |
| **GEO** | AI search readiness, content citability for ChatGPT/Perplexity/Gemini |
| **Semantic** | Topic modeling, content depth, relevance scoring |
| **Entity** | Knowledge graph positioning, brand entity strength, schema markup |
| **Technical** | Site speed, mobile-friendliness, Core Web Vitals, accessibility |
| **Competitor** | Gap analysis against top-ranking sites in niche |
| **Keywords** | Opportunity discovery, search intent matching |
| **Traffic** | Google Search Console data (impressions, clicks, CTR, position) |
| **Action Plan** | Prioritized recommendations with impact estimates |

**4. AI Synthesis** (5-7 seconds)
- Claude API processes all findings
- Generates strategic recommendations
- Creates conversational insights
- Prioritizes action items by impact

**5. Report Generation** (2-3 seconds)
- PDF report with branding
- JSON structured data export
- Executive summary
- Detailed findings per dimension

**6. Cloud Storage** (1-2 seconds)
- Save to Google Cloud Storage bucket
- Generate signed URLs for access
- Index in reports database

**7. Voice Delivery** (Real-time streaming)
- Google Cloud TTS narrates key findings
- User can ask follow-up questions
- Eva maintains conversational context
- Answers in natural language

**Total Time:** ~45 seconds average  
**Human Intervention:** Zero (fully autonomous)

---

## 📊 Production Metrics (Live Stats)

| Metric | Value | Verification |
|--------|-------|--------------|
| **🚀 Launched** | April 2026 (1 month live) | Production deployment |
| **👥 Real Users** | 50+ organic signups | Zero paid marketing |
| **⚡ Average Speed** | 45 seconds | Full-site audit completion |
| **🎯 Accuracy** | 100+ validation scans | Cross-checked vs SEOSiteCheckup |
| **🏆 Recognition** | Product Hunt #5 | Featured on Wired Business, twelve.tools |
| **🔒 Security** | 27-layer architecture | Zero incidents in production |
| **📈 Uptime** | 100% | Survived Product Hunt traffic spike |
| **🌍 Global Reach** | 5 countries | India, US, UK, UAE, Australia |
| **💬 Self-Learning** | Active | Learns from every scan + conversation |

---

## 💡 What Makes Eva Different

### **Traditional SEO Tools vs Eva Agent:**

| Feature | Traditional SEO Tools | Eva Agent |
|---------|----------------------|-----------|
| **Autonomy** | Manual tool operation required | **Autonomous: URL → analysis → report → consultation** |
| **Crawling** | Homepage scan only | **Full-site crawl (hundreds of pages)** |
| **Analysis Scope** | SEO only | **SEO + AEO + GEO + AI Search + Semantic + Entity** |
| **Delivery** | Text reports, data dumps | **Voice consultation with conversational Q&A** |
| **Insights** | Generic recommendations | **Business-specific strategic direction** |
| **AI Search** | Not addressed | **ChatGPT/Perplexity/Gemini optimization** |
| **Learning** | Static tool | **Self-learning from scans + conversations** |
| **Speed** | Minutes to hours | **45 seconds average** |
| **Cost** | $99-149/month per tool | **All-in-one $49-149/month** |
| **Integration** | Separate dashboards | **Unified voice + visual interface** |

---

## 🔒 Security Architecture (27 Layers)

Eva implements enterprise-grade security for production deployment serving agencies with sensitive client data:

### **AI Safety:**
- ✅ Prompt injection defense with input sanitization
- ✅ AI hallucination containment via rule-based validation
- ✅ Voice command validation before execution
- ✅ AI tool permission boundaries (scoped capabilities)
- ✅ Sanitized inputs/outputs at every layer
- ✅ Confidence scoring for recommendations

### **Infrastructure Protection:**
- ✅ Google Cloud IAM role-based access control
- ✅ Encrypted storage (GCS encryption at rest/transit)
- ✅ Secure crawl sandboxing (isolated execution)
- ✅ Domain validation before crawling
- ✅ Cloudflare/WAF-style DDoS protection
- ✅ API key isolation (environment variables only)
- ✅ Server-side execution for sensitive operations

### **Rate Limiting & Abuse Prevention:**
- ✅ Request throttling per user/session
- ✅ Crawl restriction policies (depth limits, politeness)
- ✅ Anti-automation abuse controls
- ✅ Action confirmation layers for high-impact operations
- ✅ Multi-step approval flows for sensitive automations

### **Monitoring & Compliance:**
- ✅ Comprehensive logging of all actions
- ✅ Audit trail system for debugging/compliance
- ✅ Real-time alerting for suspicious activity
- ✅ Read-only vs write-action separation
- ✅ Limited execution scopes for agents
- ✅ Secure webhook handling for integrations

**Production Record:** Zero security incidents serving 50+ users.

---

## 🚀 Cloud Run API Endpoints

### **Health Check - Shows All Google Services:**
```bash
GET https://eva-api-244525299670.asia-south1.run.app/
```

**Response:**
```json
{
  "status": "healthy",
  "services": {
    "cloud_run": "active",
    "cloud_storage": "connected",
    "speech_to_text": "available",
    "text_to_speech": "available",
    "search_console": "authenticated"
  },
  "region": "asia-south1",
  "version": "1.0.0"
}
```

### **List All Stored Reports from GCS:**
```bash
GET https://eva-api-244525299670.asia-south1.run.app/eva/reports
```

**Response:**
```json
{
  "reports": [
    {
      "url": "https://storage.googleapis.com/nsdmai-audit-reports/report_xyz.pdf",
      "domain": "example.com",
      "created_at": "2026-05-10T12:34:56Z",
      "format": "pdf"
    }
  ]
}
```

---

## 🛠️ Tech Stack

### **Core AI & Cloud:**
- **Claude API (Anthropic)** - Conversational intelligence, semantic analysis, insight synthesis
- **Google Cloud Run** - Auto-scaling containerized deployment (asia-south1)
- **Google Cloud Speech-to-Text** - Real-time voice input processing
- **Google Cloud Text-to-Speech** - Natural voice output generation (20+ languages)
- **Google Cloud Storage** - Audit report persistence (PDF + JSON)
- **Google Cloud IAM** - Security, permissions, service account isolation
- **Google Search Console API** - Real website traffic data integration

### **Analysis Engines (Proprietary):**
- Custom full-site crawler (Python)
- SEO scoring algorithm (200+ signals)
- AEO analysis engine (structured data validation)
- GEO readiness checker (AI search optimization)
- NLP semantic understanding pipeline
- Entity extraction & knowledge graph analysis
- Competitor benchmarking system
- Keyword opportunity discovery

### **Frontend & Platform:**
- **React** - Progressive Web App (PWA)
- **Convex** - Real-time state management
- **Hercules Platform** - Development framework
- **Tailwind CSS** - UI styling

### **Backend & Infrastructure:**
- **Python** - Crawler, analysis pipelines, API gateway
- **Node.js** - Frontend API layer
- **Flask** - Cloud Run API framework
- **Docker** - Containerization for Cloud Run
- **Git/GitHub** - Version control

### **Security Stack:**
- 27-layer security architecture
- Cloudflare WAF protection
- Rate limiting engine
- Prompt injection defense
- Audit trail system
- RBAC (Role-Based Access Control)

---

## 🎯 10 Visibility Dimensions Eva Analyzes

| # | Dimension | What It Measures | Why It Matters |
|---|-----------|------------------|----------------|
| 1 | **SEO** | Traditional search engine ranking factors | Google still drives 90%+ of organic traffic |
| 2 | **AEO** | Answer Engine Optimization (featured snippets, FAQ) | 50% of searches end with zero clicks (direct answers) |
| 3 | **GEO** | Generative Engine Optimization (ChatGPT, Perplexity, Gemini) | AI search engines are the future of discovery |
| 4 | **AI Search** | Content structure for AI consumption | Websites invisible to AI won't exist in 5 years |
| 5 | **Semantic** | Topic modeling, content depth, relevance | Search engines understand meaning, not just keywords |
| 6 | **Entity** | Knowledge graph positioning, brand entity strength | Entities rank higher than keywords in AI search |
| 7 | **Technical** | Site speed, mobile, Core Web Vitals, accessibility | Google's ranking factors, user experience metrics |
| 8 | **Competitor** | Gap analysis vs top-ranking sites | Know what leaders do differently |
| 9 | **Keywords** | Opportunity discovery, search intent matching | Find low-competition, high-value opportunities |
| 10 | **Traffic** | Google Search Console real data | Validate analysis with actual performance |

---

## 💰 Pricing

| Tier | Price | Features |
|------|-------|----------|
| **Free** | $0/month | • 3 basic audits/month<br>• SEO analysis only<br>• PDF reports<br>• Community support |
| **Pro** | $49/month | • Unlimited full audits<br>• SEO + AEO + GEO analysis<br>• Eva voice consultation<br>• Google Search Console integration<br>• Priority support |
| **Agency** | $149/month | • Multi-site management<br>• White-label reports<br>• Custom branding<br>• Reseller commission tracking<br>• API access<br>• Dedicated account manager |

**🎁 Hackathon Special:** Try Pro free for 30 days with code `GOOGLECLOUD2026`

---

## 🛠️ Local Development Setup

### **Prerequisites:**
- Node.js 18+
- Python 3.9+
- Google Cloud Account with billing enabled
- Claude API Key ([get here](https://console.anthropic.com))

### **Environment Variables:**

Create `.env` file:
```bash
# Claude AI
CLAUDE_API_KEY=your_claude_api_key_here

# Google Cloud
GOOGLE_CLOUD_PROJECT=your_project_id
GCS_BUCKET=nsdmai-audit-reports
GOOGLE_APPLICATION_CREDENTIALS=path/to/service-account.json

# Google Search Console
SEARCH_CONSOLE_CLIENT_ID=your_client_id
SEARCH_CONSOLE_CLIENT_SECRET=your_client_secret

# API Configuration
API_BASE_URL=http://localhost:8080
FRONTEND_URL=http://localhost:3000
```

### **Installation:**

```bash
# Clone repository
git clone https://github.com/onlinemarketingkingind-code/nsdmai.git
cd nsdmai

# Install frontend dependencies
npm install

# Install backend dependencies
cd api
pip install -r requirements.txt
cd ..

# Set up Google Cloud credentials
gcloud auth application-default login
gcloud config set project your_project_id
```

### **Run Locally:**

```bash
# Terminal 1 - Frontend (React)
npm run dev
# Runs on http://localhost:3000

# Terminal 2 - Backend API (Python/Flask)
cd api
python app.py
# Runs on http://localhost:8080
```

### **Deploy to Google Cloud Run:**

```bash
# Build container
gcloud builds submit --tag gcr.io/your_project_id/eva-api

# Deploy to Cloud Run
gcloud run deploy eva-api \
  --image gcr.io/your_project_id/eva-api \
  --platform managed \
  --region asia-south1 \
  --allow-unauthenticated \
  --set-env-vars CLAUDE_API_KEY=your_key
```

**Full deployment guide:** See `docs/deployment.md`

---

## 📚 Documentation

- **Architecture Overview:** `docs/architecture.md`
- **API Reference:** `docs/api.md`
- **Deployment Guide:** `docs/deployment.md`
- **Security Model:** `docs/security.md`
- **Contributing:** `CONTRIBUTING.md`

---

## 🗺️ Roadmap

### **Phase 1: Agency Enablement (Q3 2026)**
- [ ] White-label deployment
- [ ] Multi-site voice switching
- [ ] Branded PDF reports
- [ ] Reseller analytics dashboard
- [ ] Sales pipeline & CRM integration

### **Phase 2: Intelligence Upgrades (Q4 2026)**
- [ ] Eva conversation tagging
- [ ] Auto-knowledge extraction
- [ ] Regional knowledge packs (India/US/UK SEO)
- [ ] Semantic long-term memory
- [ ] Weekly learning analysis reports
- [ ] Thumbs up/down feedback UI

### **Phase 3: Platform Expansion (2027)**
- [ ] Arena integration (gamified marketing certification)
- [ ] ExcelQueen connection (automated report generation)
- [ ] Hindi voice interface (500M+ potential users)
- [ ] Multi-language support (Spanish, French, Mandarin)
- [ ] Mobile apps (iOS/Android)
- [ ] Real-time AI search monitoring

### **Long-Term Vision (2028):**
Transform Eva from **analysis tool** to **autonomous execution platform**:
- Auto-fix technical SEO issues
- Write and publish optimized content
- Manage schema markup dynamically
- Build entity relationships in knowledge graphs
- Coordinate with human teams like a real marketing director

---

## 👥 Team

### **Narayan Shukla** - Founder & Lead Developer
- 11 years digital marketing consulting experience
- 500+ client projects across UK, US, UAE, Australia, India
- Founder: Call Digital Fire LLP (Pune, India)
- Founder: NSDM AI ecosystem
- **For this hackathon:** Solo builder demonstrating production AI agent deployment

### **Hercules** - Technical Collaborator
- Platform development and implementation
- Convex/React architecture
- Cloud infrastructure optimization

**🇮🇳 Built in:** Pune, Maharashtra, India  
**🌍 Serving:** Global markets  
**☁️ Powered by:** Google Cloud

---

## 🏆 Recognition & Media

- 🥇 **Product Hunt** - #5 Featured Product
- 📰 **Wired Business** - Featured AI Startup
- 🛠️ **twelve.tools** - Featured Tool
- 🚀 **Startup Fame** - Featured Startup
- 📱 **NG.tools** - Launching (19 upvotes pre-launch)

---

## 📧 Contact

**Email:** narayan.shukla@calldigitalfire.com  
**Website:** [nsdmai.com](https://nsdmai.com)  
**Company:** Call Digital Fire LLP, Pune, India  

**For Hackathon Judges:**
- GitHub: [github.com/onlinemarketingkingind-code/nsdmai](https://github.com/onlinemarketingkingind-code/nsdmai)
- Live Demo: [nsdmai.com](https://nsdmai.com)
- Cloud Run API: https://eva-api-244525299670.asia-south1.run.app

---

## 📄 License

Proprietary - © 2026 NSDM AI, Call Digital Fire LLP. All rights reserved.

---

## 🙏 Acknowledgments

- **Anthropic** - Claude API for conversational intelligence
- **Google Cloud** - Infrastructure, AI services, and hackathon opportunity
- **Early Users** - 50+ users who provided feedback and validation
- **Open Source Community** - Libraries and tools that made this possible

---

**⭐ Star this repo if Eva helps your marketing visibility!**

---

*Built with ❤️ in Pune, India 🇮🇳 | Serving the world 🌍 | Powered by Google Cloud ☁️*
