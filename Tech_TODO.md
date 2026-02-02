# 🚀 TaskPilot - Project Todo List

Based on the **PRD**, **Design Document**, and **Tech Stack**.

---

## 💻 Tech Todo (Implementation & Engineering)

### Phase 1: Foundation & Setup (Week 1)
- [x] **Repo Initialization**:
    - [x] Initialize Git repository.
    - [x] Create Next.js app (`npx create-next-app@latest`) with Tailwind CSS.
    - [x] Configure `index.css` with Design Tokens (Pastel colors, fonts).
- [ ] **Backend Infrastructure**:
    - [x] Setup Node.js/FastAPI backend.
    - [x] Configure PostgreSQL Database (Supabase/Neon).
    - [x] Configure PostgreSQL Database (Supabase/Neon).
    - [x] Configure Qdrant/Pinecone Vector DB.
    - [x] **Infrastructure**: Configure Redis (Caching & Job Queue).
    - [x] **Infrastructure**: Setup Async Workers (Arq/Celery).
- [ ] **Authentication**:
    - [ ] Implement Clerk or NextAuth.
    - [ ] Create Protected Routes Middleware.
- [ ] **Core Features**:
    - [ ] Build **Business Setup Wizard** (Frontend Forms).
    - [ ] Build **Onboarding API** (Save business profile).
    - [ ] Build **Onboarding API** (Save business profile).
    - [ ] Implement **Knowledge Base Engine** (Text chunking + Embedding generation).
    - [ ] Set up **LLM Router** (Model Cascading: Llama 3 <-> GPT-4o).

### Phase 2: Sales Agent (Week 2)
- [ ] **WhatsApp Integration**:
    - [ ] Create Webhook endpoint for WhatsApp Cloud API.
    - [ ] Implement message validation and parsing.
- [ ] **AI Logic**:
    - [ ] Develop "Sales Agent" System Prompt.
    - [ ] Implement RAG pipeline (Retrieve KB context -> Generate via LLM).
    - [ ] Build Tool calling for "Check Calendar" and "Book Appointment".
- [ ] **Data Layer**:
    - [ ] Create `Leads` table schema.
    - [ ] Implement logic to save qualified leads to DB.

### Phase 3: Support Agent & Dashboard (Week 3)
- [ ] **Support Agent**:
    - [ ] Implement strict "Knowledge Base Only" response logic.
    - [ ] Build "Human Handoff" trigger.
- [ ] **Dashboard Development**:
    - [ ] Build **Overview Page** (KPI Cards, Charts using Recharts).
    - [ ] Build **Conversations View** (Chat UI for monitoring).
    - [ ] Build **Agent Activity Log** (Task history).

### Phase 4: Marketing & Billing (Week 4)
- [ ] **Marketing Tools**:
    - [ ] Integrate OpenAI/DALL-E for content generation.
    - [ ] Build "Post Scheduler" UI.
- [ ] **Monetization**:
    - [ ] Integrate Stripe/Razorpay Payment Gateway.
    - [ ] Implement Subscription Webhooks (Upgrade/Downgrade logic).
- [ ] **Deployment**:
    - [ ] Deploy Frontend to Vercel/Netlify.
    - [ ] Deploy Backend to Railway/Render.

- [ ] **Reliability & Scale**:
    - [ ] Implement Rate Limiting (Token Bucket).
    - [ ] Configure Semantic Caching for LLM responses.
    - [ ] Setup Dead Letter Queues (DLQ) for failed jobs.

---

