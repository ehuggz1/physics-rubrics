# AG Implementation Guide & Roadmap

## 1. Overview

This document serves as the primary execution guide for the ClusterCraft project. It is derived directly from the JIRA stories in the `AG_JIRAs` folder and aligns with the `AG_TechnicalArchitecture.md`. It provides a step-by-step roadmap for developers and includes best practice guidance for the selected technology stack.

---

## 2. Implementation Phases

### Phase 1: Data Preparation & Infrastructure (Epic 1)
**Goal**: Establish the project foundation and build the knowledge base from raw standard documents.

*   **Infrastructure Setup**
    *   **[CC-001]**: Initialize Git, set up **Google AntiGravity IDE**, configure Docker for PostgreSQL/Weaviate.
    *   **[CC-010]**: Define schemas for SQL (Standards metadata) and Weaviate (Embeddings).
*   **Data Extraction**
    *   **[CC-002/007]**: Implement parsers for MHTML (Standards) and PDF (Sample Clusters).
    *   **[CC-003-006]**: Run extraction scripts for all 5 Physics domains (Energy, Forces, etc.).
    *   **[CC-009]**: Extract Performance Level Descriptors (PLDs).
*   **Knowledge Base Construction**
    *   **[CC-011]**: Map extracted data to the 3D Framework (SEP, CCC, DCI).
    *   **[CC-012]**: Validate data completeness and create a "Golden Test Set" for future validation.

### Phase 2: AI Model Development (Epic 2)
**Goal**: Develop the core RAG pipeline and prompt engineering using Gemini 3.0 Pro.

*   **Model Setup**
    *   **[CC-013]**: Confirm **Gemini 3.0 Pro** performance benchmarks.
    *   **[CC-014]**: Configure **Vertex AI / Google AI Studio** as the Runtime API Provider.
    *   **[CC-015]**: Configure embedding models (Gecko/OpenAI) in Weaviate.
*   **RAG Pipeline**
    *   **[CC-016/017]**: Design the RAG architecture and implement Weaviate retrieval logic.
    *   **[CC-021]**: Implement Context Retrieval strategies (hybrid search: keyword + vector).
*   **Prompt Engineering**
    *   **[CC-018]**: Develop System Prompts enforcing the "Physics Regents" persona.
    *   **[CC-019]**: Create Few-Shot examples from the "Golden Test Set".
    *   **[CC-023]**: Build the end-to-end Generation Pipeline (Input -> Retrieve -> Prompt -> Generate).

### Phase 3: Validation & QA (Epic 3)
**Goal**: Ensure generated questions are valid, safe, and aligned with NY State Standards.

*   **Validation Framework**
    *   **[CC-028]**: Design the automated validation architecture.
    *   **[CC-029-031]**: Implement specific validators for SEP, CCC, and DCI dimensions.
    *   **[CC-032]**: Build the **3D Alignment Checker** (the core quality gate).
*   **Quality Metrics**
    *   **[CC-034]**: Implement Context Scoring (how well does the question fit the stimulus?).
    *   **[CC-035]**: Develop a Difficulty Classifier to ensure Regents-level appropriateness.
    *   **[CC-036]**: Create a Quality Dashboard to track pass/fail rates of generated questions.

### Phase 4: UI Integration & API (Epic 4)
**Goal**: Build the user-facing application for teachers to generate and export questions.

*   **Backend API**
    *   **[CC-048]**: Develop **FastAPI** endpoints (`/generate`, `/validate`, `/standards`).
    *   **[CC-049]**: Generate OpenAPI/Swagger documentation.
*   **Frontend Development**
    *   **[CC-039]**: Initialize **React + Vite** project with **Tailwind CSS** and **Shadcn/UI**.
    *   **[CC-040-042]**: Build the Stimulus Input Form and Configuration Panel.
    *   **[CC-043]**: Implement the Question Display component with Markdown rendering.
    *   **[CC-046]**: Add Export functionality (PDF/Word).

---

## 3. Technology Best Practices

### 3.1 Backend: FastAPI & Python
*   **Type Safety**: Use **Pydantic v2** models for all request/response schemas. Strict typing prevents runtime errors and auto-generates documentation.
*   **Dependency Injection**: Leverage FastAPI's `Depends()` for database sessions, auth, and service layers. This makes testing easier by allowing mock injections.
*   **Async/Await**: The RAG pipeline is I/O bound (waiting for LLM/DB). Use `async def` for all route handlers to handle high concurrency.
*   **Project Structure**: Follow a domain-driven structure:
    ```
    /app
      /api (routes)
      /core (config, security)
      /models (pydantic/sql)
      /services (business logic)
    ```

### 3.2 Frontend: React, Vite, & Tailwind
*   **Component Composition**: Use **Shadcn/UI** components as building blocks. Do not reinvent buttons or inputs.
*   **State Management**: Use **Zustand** for global client state (e.g., user preferences) and **React Query** for server state (fetching standards, generation jobs).
*   **Styling**: Use utility classes (Tailwind) for layout and spacing. Avoid custom CSS files unless absolutely necessary for complex animations.
*   **Performance**: Lazy load heavy components (like the PDF exporter) using `React.lazy()`.

### 3.3 AI & Data: Gemini & Weaviate
*   **Prompting**:
    *   **Chain-of-Thought**: Ask the model to "think step-by-step" before generating the final question to improve reasoning quality.
    *   **Structured Output**: Use Gemini's native JSON mode or Pydantic parsers to ensure the output is machine-readable.
*   **Retrieval**:
    *   **Hybrid Search**: Don't rely on vectors alone. Use Weaviate's hybrid search (Vector + Keyword) to find specific standards (e.g., "HS-PS3-1") while maintaining semantic relevance.
    *   **Chunking**: When ingesting standards, keep chunks small (paragraph level) but preserve the hierarchy (Standard -> Section -> Bullet point) in metadata.

### 3.4 Development: Google AntiGravity
*   **Agent Workflows**: Delegate routine tasks (e.g., "Write a Pydantic model for this JSON schema") to AntiGravity agents.
*   **Artifacts**: Keep this `AG_ImplementationPlan.md` and other artifacts open. Update them as you complete tasks to maintain a "living" documentation.
*   **Context**: When asking the IDE to generate code, reference the specific JIRA ticket ID (e.g., "Implement CC-048") to give it context on the requirements.
