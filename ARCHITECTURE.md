# 🏗️ TeamUp AI – System Architecture & Scalability Strategy

## 1. Architecture Overview
**TeamUp AI ("TaskPilot")** is built as a **Event-Driven, Multi-Tenant SaaS** designed to handle high-concurrency real-time inputs (WhatsApp) while managing long-running AI workflows. 

The architecture follows a **Modern Modular Monolith** approach (for the backend) that can split into microservices as specific domains (e.g., The AI Inference Engine) scale.

### High-Level Diagram
```mermaid
graph TD
    User[Business User] -->|HTTPS| CDN[Cloudflare CDN]
    CDN --> FE[Next.js Frontend Vercel]
    
    Lead[WhatsApp/Lead] -->|Webhook| API_GW[API Gateway / Load Balancer]
    API_GW --> BE[FastAPI Backend Cluster]
    
    subgraph "Data Layer"
        BE --> PG[(PostgreSQL - Primary DB)]
        BE --> REDIS[(Redis - Cache & Queues)]
        BE --> QDRANT[(Qdrant - Vector DB)]
    end
    
    subgraph "AI & Automation Layer"
        BE --> WORKER[Async Workers (Celery/Arq)]
        WORKER --> LLM[LLM Provider (OpenAI/Groq)]
        WORKER --> TOOLS[External Tools (GCal, Stripe)]
        WORKER --> N8N[n8n Automation Engine]
    end
```

---

## 2. Component Breakdown

### 🖥️ Frontend (Client Layer)
- **Tech**: Next.js 15 (App Router), Tailwind CSS, React Query.
- **Responsibility**: 
  - Business Onboarding Wizards.
  - Real-time "Command Center" Dashboard.
  - Analytics Visualization (Recharts).
- **Hosting**: Vercel (Edge Network).

### ⚙️ Backend (Core Logic Layer)
- **Tech**: Python FastAPI (Async).
- **Responsibility**:
  - **API Gateway**: REST endpoints for Frontend & Webhooks.
  - **Auth Service**: Validating Clerk/NextAuth tokens.
  - **Orchestration**: Routing requests between DB, Vector Store, and AI Agents.
- **Performance**: Fully AsyncIO to handle thousands of concurrent WhatsApp Webhooks without blocking.

### 🧠 AI Engine (The "Brain")
- **Tech**: LangChain / Custom Python Logic.
- **Responsibility**:
  - Prompt Engineering & Context Injection.
  - RAG Pipeline (Retrieving knowledge from Qdrant).
  - Tool Calling (Deciding when to book a calendar slot vs. just replying).
- **Optimization**: Uses a **Router** to pick the cheapest/fastest model (e.g., Llama-3-8b for simple greetings, GPT-4o for complex sales objections).

### ⚡ Async Worker & Automation Layer
- **Tech**: Celery or Arq + Redis.
- **Responsibility**:
  - Offloading slow tasks (e.g., "Generate Weekly Marketing Plan").
  - Reliable message delivery (Retries if WhatsApp API fails).
  - Interfacing with **n8n** for user-customizable workflows.

### 🗄️ Data Persistence
1.  **PostgreSQL**: Single source of truth. Uses **Logical Isolation** (TenantID column) for all queries.
2.  **Qdrant**: Stores business knowledge embeddings (FAQs, PDFs). Namespace/Collection per tenant for strict data isolation.
3.  **Redis**: 
    - **Hot Cache**: User sessions, frequent config lookups.
    - **Message Broker**: Queue for incoming WhatsApp messages to prevent server overload during spikes.

---

## 3. Data Flow

### Scenario: A Lead sends a WhatsApp Message
1.  **Ingestion**: Meta sends a `POST` webhook to `api.teamup.ai/webhooks/whatsapp`.
2.  **Buffering**: FastAPI pushes the raw payload to a **Redis Queue** immediately and returns `200 OK` (Latency < 200ms).
3.  **Processing**: An Async Worker picks up the message.
4.  **Context Retrieval**:
    - Worker fetches the Business Profile from **Postgres**.
    - Queries **Qdrant** for relevant FAQs/History related to the user's message.
5.  **Inference**:
    - Constructs a prompt: `(System Role + Business Context + Retrieved Chunks + User Message)`.
    - Sends to LLM (OpenAI/Groq).
6.  **Action**:
    - LLM returns text response OR a Tool Call (e.g., `check_calendar`).
    - Worker executes tool if needed.
7.  **Response**: Worker calls WhatsApp API to send the reply.
8.  **Logging**: The conversation turn is saved to **Postgres** (for analytics) and embedded into **Qdrant** (for long-term memory).

---

## 4. Scalability & Cost Strategy (100k+ Users)

### 📈 Handling Scale
1.  **Stateless Backend**: The FastAPI tier is stateless. We can auto-scale from 1 to 50 containers based on CPU/Memory usage using **Kubernetes (K8s) or AWS ECS**.
2.  **Database Sharding**:
    - **Phase 1**: Single large Postgres instance.
    - **Phase 2**: Read Replicas for Dashboard analytics.
    - **Phase 3**: Sharding by `tenant_id` (putting groups of businesses on different DB servers).
3.  **Vector Search Scaling**: Qdrant allows distributed deployments. We will partition collections by `business_id` to ensure searches remain ms-fast even with billions of vectors.

### 💰 Cost Optimization
1.  **Model Tiering (The "Cascading Architecture")**:
    - **Level 1 (Cheap/Free)**: Use a locally hosted classifier (or tiny model) to detect spam or simple "Hello". (Cost: ~$0)
    - **Level 2 (Mid)**: Llama-3-70b (via Groq) for general conversation. (Cost: Low)
    - **Level 3 (Premium)**: GPT-4o only for complex negotiation or reasoning tasks.
2.  **Caching**: Cache LLM responses for identical queries using **Semantic Caching** (e.g., if 100 users ask "What is your pricing?", generate once, cache vector result).
3.  **Cold vs. Hot Storage**: Archive old conversations to S3/Blob Storage to keep Postgres lean and fast.

### 🛡️ Reliability
- **Dead Letter Queues (DLQ)**: If an AI agent attempts to process a message and crashes (e.g., LLM outage), the message goes to a DLQ for retry/human review, ensuring no lead is ever lost.
- **Rate Limiting**: Implementation of Token Bucket limits per tenant to prevent one noisy tenant from degrading the entire platform.
