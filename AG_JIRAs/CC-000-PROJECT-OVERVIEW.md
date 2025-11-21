# ClusterCraft Project Overview

**Project Key**: CC  
**Project Name**: ClusterCraft  
**Project Type**: Software Development  
**Created**: November 20, 2025  
**Status**: Planning

---

## Project Description

ClusterCraft is an AI-powered system that generates high-quality, 3-dimensional test questions for NY State Regents Physics exams. The system takes a storyline stimulus and an array of Performance Expectation Standards and automatically generates 1-3 test questions that assess students across all three reasoning dimensions as defined by the NYSSLS framework.

---

## Project Goals

1. Generate questions that align with specified Performance Expectations
2. Questions must test all three dimensions simultaneously (SEP, CCC, DCI)
3. Questions should be contextually appropriate to the provided stimulus
4. Output quality comparable to official Regents exam clusters
5. System can handle all 18 Physics Performance Expectations across 5 domains

---

## Epic Structure

### Epic 1: Data Preparation & Knowledge Base (CC-EPIC-001)
**Duration**: 2-3 weeks  
**Stories**: 12  
**Focus**: Extract, structure, and organize all physics standards and sample data

### Epic 2: AI Model Development (CC-EPIC-002)
**Duration**: 4-6 weeks  
**Stories**: 15  
**Focus**: Build and configure the AI-powered question generation engine

### Epic 3: Validation & Quality Assurance (CC-EPIC-003)
**Duration**: 3-4 weeks  
**Stories**: 10  
**Focus**: Ensure 3D alignment and quality of generated questions

### Epic 4: User Interface & Integration (CC-EPIC-004)
**Duration**: 2-3 weeks  
**Stories**: 12  
**Focus**: Create user-friendly interface and integration capabilities

---

## Technology Stack

- **LLM**: Gemini 3.0 Pro / Deep Think
- **Backend**: Python FastAPI
- **Frontend**: React
- **Vector DB**: Weaviate
- **Database**: PostgreSQL
- **Hosting**: Google Cloud Platform (Vertex AI)

---

## Success Metrics

| Metric | Target |
|--------|--------|
| 3D Alignment Accuracy | >95% |
| Standard Alignment | 100% |
| Context Appropriateness | >90% |
| Generation Time | <30 seconds |
| Question Quality Score | >4.0/5.0 |

---

## Project Timeline

**Total Duration**: 4-5 months

- Phase 1: Data Preparation (Weeks 1-3)
- Phase 2: AI Development (Weeks 4-9)
- Phase 3: Validation & QA (Weeks 10-13)
- Phase 4: UI & Integration (Weeks 14-16)
- Phase 5: Testing & Launch (Weeks 17-18)

---

## Team Roles

- **Product Owner**: TBD
- **Tech Lead**: TBD
- **AI/ML Engineer**: TBD
- **Backend Developer**: TBD
- **Frontend Developer**: TBD
- **QA Engineer**: TBD
- **Physics Subject Matter Expert**: TBD

---

## JIRA Numbering Convention

- **Project Overview**: CC-000
- **Epics**: CC-EPIC-001 through CC-EPIC-004
- **Stories**: CC-001 through CC-049
- **Sub-tasks**: CC-001-01, CC-001-02, etc.

---

## Related Documents

- [AG_ProjectPlan.md](../AG_ProjectPlan.md) - Comprehensive project plan
- [ProductNameOptions.md](../ProductNameOptions.md) - Branding and naming
- [README.md](../README.md) - Repository overview
