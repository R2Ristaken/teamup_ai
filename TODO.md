# 🚀 TaskPilot - Project Todo List

Based on the **PRD**, **Design Document**, and **Tech Stack**, here is the actionable roadmap for building TaskPilot.

---

## 🏗️ Phase 1: Foundation & Setup (Week 1)
**Goal:** core infrastructure, authentication, and business setup.

### 1.1 Project Initialization
- [ ] **Repo Setup**: Initialize Git repository.
- [ ] **Frontend Setup**:
    - [ ] Initialize Next.js app (`npx create-next-app@latest`).
    - [ ] Install Tailwind CSS and Shadcn/UI (or custom design tokens as per `design.md`).
    - [ ] Setup folder structure (`/components`, `/pages`, `/hooks`, `/lib`).
    - [ ] Configure `index.css` with valid design tokens (Color palette: Soft blues, muted teals, pastel greens).
- [ ] **Backend Setup** (Choose NestJS or FastAPI):
    - [ ] Initialize Backend project.
    - [ ] Setup Database ORM (Prisma/TypeORM/SQLAlchemy).
    - [ ] Configure environment variables.
- [ ] **Database**:
    - [ ] Provision PostgreSQL database (Supabase/Neon).
    - [ ] Define initial schema (Users, Businesses, Agents).
    - [ ] Provision Vector Database (Qdrant or Pinecone).

### 1.2 Authentication & User Management
- [ ] Implement Login/Signup pages (Email/Password).
- [ ] Integrate Google OAuth.
- [ ] Setup Clerk or NextAuth.
- [ ] Create strict route protection (Middleware).

### 1.3 Business Setup Wizard
- [ ] **UI**: Create multi-step wizard form.
    - [ ] Step 1: Business Name, Industry, Language.
    - [ ] Step 2: Products/Services details.
    - [ ] Step 3: Pricing and Offers.
    - [ ] Step 4: FAQs and Brand Tone.
- [ ] **Backend**:
    - [ ] API to save business profile.
    - [ ] API to store initial Knowledge Base entries.
- [ ] **Knowledge Base Engine**:
    - [ ] Text chunking logic.
    - [ ] Generate embeddings (OpenAI/HuggingFace).
    - [ ] Store in Vector DB.

---

## 🤖 Phase 2: AI Sales Agent (Week 2)
**Goal:** WhatsApp-based agent that qualifies leads and books calls.

### 2.1 WhatsApp Integration
- [ ] Set up Meta Developer App & WhatsApp Cloud API.
- [ ] Create Webhook endpoint to receive messages.
- [ ] Implement message parsing and validation.

### 2.2 Sales Agent Logic
- [ ] **Prompt Engineering**:
    - [ ] Define System Prompt (Tone, Rules, "Never hallucinate prices").
    - [ ] Implement Context Retrieval (RAG) for product queries.
- [ ] **Flow Control**:
    - [ ] Lead Qualification state machine.
    - [ ] Appointment Booking flow (Integration with Calendar).
    - [ ] Fallback logic (Escalate to human).

### 2.3 Lead Management
- [ ] Create `Leads` table in DB.
- [ ] Auto-save qualified leads from WhatsApp conversations.
- [ ] UI: "Leads & Contacts" screen (Table, Filters, Sort).

---

## 🛠️ Phase 3: Support Agent & Dashboard (Week 3)
**Goal:** Handle FAQs and visualize business metrics.

### 3.1 Support Agent
- [ ] **Logic**:
    - [ ] Strict RAG implementation (Only answer from KB).
    - [ ] Politeness and tone enforcement.
- [ ] **Integration**:
    - [ ] Enable specific WhatsApp numbers or channels for support.
    - [ ] Human handoff mechanism.

### 3.2 Dashboard UI (High Priority)
- [ ] **Overview Screen**:
    - [ ] KPI Cards (Total Leads, Tasks Completed, Active Convos).
    - [ ] Charts (Lead acquisition, Conversion funnel).
- [ ] **Conversations Screen**:
    - [ ] Chat interface (Left: Contacts, Right: Thread).
    - [ ] Ability to interfere/monitor AI chats.
- [ ] **Agent Task Overview**:
    - [ ] List of daily tasks performed by agents.
    - [ ] Status indicators (Completed, Pending).

---

## 📈 Phase 4: Marketing, Billing & Polish (Week 4)
**Goal:** Outbound marketing and monetization.

### 4.1 AI Marketing Agent
- [ ] **Content Generation**:
    - [ ] Prompt to generate post ideas/captions based on business context.
    - [ ] Integration with Image Gen API (DALL-E/Midjourney via API).
- [ ] **Scheduling**:
    - [ ] Basic scheduling logic (Mock or API integration).
    - [ ] Dashboard view for "Upcoming Posts".

### 4.2 Billing & Subscriptions
- [ ] Integrate Razorpay (India) / Stripe (Global).
- [ ] Create Pricing Page (Starter, Pro, Business).
- [ ] Handle subscription Webhooks (Active/Cancelled status).

### 4.3 Evaluation & Deployment
- [ ] **Testing**:
    - [ ] AI hallucinations check.
    - [ ] Load testing for Webhooks.
- [ ] **Deployment**:
    - [ ] Deploy Frontend (Vercel).
    - [ ] Deploy Backend (Railway/Render/AWS).
    - [ ] Domain setup.

---

## 📝 Documentation & Handoff
- [ ] Write API Documentation (Swagger/OpenAPI).
- [ ] Create User Guide for Business Setup.
