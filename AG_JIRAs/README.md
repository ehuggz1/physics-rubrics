# ClusterCraft JIRA Tickets

This folder contains all JIRA tickets for the ClusterCraft project, organized as markdown files for easy version control and collaboration.

---

## Project Overview

**Project**: ClusterCraft  
**Project Key**: CC  
**Description**: AI-powered system for generating 3-dimensional physics test questions for NY State Regents exams  
**Status**: Planning Phase  
**Start Date**: TBD  
**Target Launch**: Q2 2026  

---

## Ticket Numbering Convention

- **CC-000**: Project Overview
- **CC-EPIC-XXX**: Epic tickets (001-004)
- **CC-001 to CC-049**: Story tickets
- **CC-XXX-YY**: Sub-tasks (e.g., CC-001-01)

---

## Epic Structure

### Epic 1: Data Preparation & Knowledge Base Construction
**Epic ID**: CC-EPIC-001  
**Duration**: 2-3 weeks  
**Stories**: CC-001 through CC-012 (12 stories)  
**Status**: To Do  

**Focus**: Extract and structure all physics standards, sample clusters, and PLDs into searchable knowledge base.

**Key Deliverables**:
- 18 Performance Expectations extracted and structured
- 3 Sample clusters analyzed
- Knowledge base operational
- 3D framework mappings complete

---

### Epic 2: AI Model Development
**Epic ID**: CC-EPIC-002  
**Duration**: 4-6 weeks  
**Stories**: CC-013 through CC-027 (15 stories)  
**Status**: To Do  

**Focus**: Build AI-powered question generation engine using Gemini 3.0 Pro with RAG architecture.

**Key Deliverables**:
- LLM selected and configured (Gemini 3.0 Pro)
- RAG system operational
- Prompt library created
- Question generation pipeline functional

---

### Epic 3: Validation & Quality Assurance
**Epic ID**: CC-EPIC-003  
**Duration**: 3-4 weeks  
**Stories**: CC-028 through CC-037 (10 stories)  
**Status**: To Do  

**Focus**: Ensure 3D alignment and quality of generated questions through automated validation and expert review.

**Key Deliverables**:
- 3D alignment checker (>95% accuracy)
- Quality metrics dashboard
- Expert review process
- Validation reports

---

### Epic 4: User Interface & Integration
**Epic ID**: CC-EPIC-004  
**Duration**: 2-3 weeks  
**Stories**: CC-038 through CC-049 (12 stories)  
**Status**: To Do  

**Focus**: Create user-friendly interface and API for question generation.

**Key Deliverables**:
- Web UI (React)
- RESTful API (FastAPI)
- Export functionality (PDF, Word, JSON)
- User documentation

---

## Story Status Summary

| Status | Count | Percentage |
|--------|-------|------------|
| To Do | 49 | 100% |
| In Progress | 0 | 0% |
| In Review | 0 | 0% |
| Done | 0 | 0% |
| **Total** | **49** | **100%** |

---

## Story Points by Epic

| Epic | Stories | Story Points | Avg Points/Story |
|------|---------|--------------|------------------|
| Epic 1 | 12 | ~85 | 7.1 |
| Epic 2 | 15 | ~110 | 7.3 |
| Epic 3 | 10 | ~80 | 8.0 |
| Epic 4 | 12 | ~90 | 7.5 |
| **Total** | **49** | **~365** | **7.4** |

---

## Priority Breakdown

| Priority | Count |
|----------|-------|
| Highest | 12 |
| High | 25 |
| Medium | 10 |
| Low | 2 |

---

## File Organization

```
AG_JIRAs/
├── CC-000-PROJECT-OVERVIEW.md
├── CC-EPIC-001-Data-Preparation.md
├── CC-EPIC-002-AI-Model-Development.md
├── CC-EPIC-003-Validation-QA.md
├── CC-EPIC-004-UI-Integration.md
├── CC-001-Setup-Infrastructure.md
├── CC-002-MHTML-Parser.md
├── CC-013-Evaluate-LLM.md
├── CC-032-3D-Alignment-Checker.md
├── CC-040-Stimulus-Input-Form.md
└── README.md (this file)
```

---

## Sample Stories Created

The following sample stories have been created to demonstrate the structure:

### Epic 1 - Data Preparation
- ✅ **CC-001**: Set up project infrastructure and development environment
- ✅ **CC-002**: Create MHTML parser for standards extraction

### Epic 2 - AI Model Development
- ✅ **CC-013**: Evaluate LLM options and select Gemini 3.0 Pro/Deep Think

### Epic 3 - Validation & QA
- ✅ **CC-032**: Build integrated 3D alignment checker

### Epic 4 - UI & Integration
- ✅ **CC-040**: Build stimulus input form component

---

## Remaining Stories to Create

### Epic 1 (10 remaining)
- CC-003: Extract Energy domain standards
- CC-004: Extract Forces and Motion standards
- CC-005: Extract Waves and Information standards
- CC-006: Extract Space Systems and Matter standards
- CC-007: Create PDF parser for sample clusters
- CC-008: Analyze sample cluster question patterns
- CC-009: Extract and structure Performance Level Descriptors
- CC-010: Design and implement knowledge base schema
- CC-011: Create 3D framework mapping system
- CC-012: Validate data completeness and create test dataset

### Epic 2 (14 remaining)
- CC-014: Set up Google AI Studio and Vertex AI access
- CC-015: Configure embedding model for semantic search
- CC-016: Design RAG architecture and data flow
- CC-017: Implement vector database integration with Weaviate
- CC-018: Create system prompts for question generation
- CC-019: Develop few-shot examples from sample clusters
- CC-020: Build dimension-specific validation prompts
- CC-021: Implement context retrieval system
- CC-022: Create context injection and formatting system
- CC-023: Build question generation pipeline
- CC-024: Implement output formatting and structuring
- CC-025: Create initial validation rules engine
- CC-026: Conduct initial testing and quality assessment
- CC-027: Iterate on prompts based on test results

### Epic 3 (9 remaining)
- CC-028: Design validation framework architecture
- CC-029: Build Dimension 1 (SEP) validator
- CC-030: Build Dimension 2 (CCC) validator
- CC-031: Build Dimension 3 (DCI) validator
- CC-033: Implement standard alignment validator
- CC-034: Build context appropriateness scoring system
- CC-035: Create difficulty level classifier
- CC-036: Develop quality metrics dashboard
- CC-037: Generate questions for all 18 standards (test suite)

### Epic 4 (11 remaining)
- CC-038: Design UI/UX mockups and user flows
- CC-039: Set up React frontend project structure
- CC-041: Create standards multi-select component
- CC-042: Implement configuration options panel
- CC-043: Build question display component
- CC-044: Create question editing interface
- CC-045: Implement 3D alignment report visualization
- CC-046: Build export functionality (PDF, Word, JSON)
- CC-047: Create batch processing interface
- CC-048: Develop RESTful API with FastAPI
- CC-049: Write API documentation and create Swagger UI

---

## How to Use These Tickets

1. **For Planning**: Review epics and stories to understand project scope
2. **For Development**: Pick up stories in order within each epic
3. **For Tracking**: Update story status as work progresses
4. **For Collaboration**: Add comments and updates directly to markdown files
5. **For Reporting**: Use story points and status for sprint planning

---

## Story Template

When creating new stories, use this template:

```markdown
# Story: [Title]

**Story ID**: CC-XXX  
**Epic**: CC-EPIC-XXX  
**Story Type**: Feature/Task/Bug/Research  
**Priority**: Highest/High/Medium/Low  
**Story Points**: X  
**Status**: To Do/In Progress/In Review/Done  

## User Story
As a **[role]**, I want to **[action]** so that **[benefit]**.

## Description
[Detailed description]

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2

## Technical Tasks
### Sub-tasks
1. CC-XXX-01: Task 1
2. CC-XXX-02: Task 2

## Dependencies
- Prerequisite: CC-XXX
- Required: [Resources]

## Definition of Done
- [ ] All acceptance criteria met
- [ ] Code reviewed
- [ ] Tests passing
- [ ] Documentation updated

## Related Stories
- Depends On: CC-XXX
- Blocks: CC-XXX

**Created**: YYYY-MM-DD  
**Assigned To**: TBD  
**Reporter**: TBD  
**Labels**: tag1, tag2
```

---

## Labels/Tags Used

- `infrastructure` - Setup and configuration
- `data-extraction` - Data parsing and extraction
- `parser` - Parser development
- `ai-model` - AI/ML related
- `validation` - Quality assurance
- `3d-alignment` - Three-dimensional learning
- `frontend` - UI development
- `ui-component` - React components
- `api` - Backend API
- `epic-1`, `epic-2`, `epic-3`, `epic-4` - Epic associations
- `critical` - High priority/blocking
- `spike` - Research/investigation

---

## Next Steps

1. **Complete remaining story creation** (44 stories)
2. **Assign story points** to all stories
3. **Identify dependencies** between stories
4. **Create sprint plan** (2-week sprints)
5. **Assign team members** to stories
6. **Set up project board** (Kanban or Scrum)

---

## Related Documents

- [Project Plan](../AG_ProjectPlan.md)
- [Product Naming](../ProductNameOptions.md)
- [Repository README](../README.md)

---

**Last Updated**: November 20, 2025  
**Maintained By**: Project Team  
**Questions**: Contact project lead
