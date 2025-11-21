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

## Folder Structure

```
AG_JIRAs/
├── CC-000-PROJECT-OVERVIEW.md
├── README.md (this file)
├── Epic-1-Data-Preparation/
│   ├── CC-EPIC-001-Data-Preparation.md
│   ├── CC-001-Setup-Infrastructure.md
│   ├── CC-002-MHTML-Parser.md
│   ├── CC-003-Extract-Energy-Standards.md
│   ├── CC-004-Extract-Forces-Motion-Standards.md
│   ├── CC-005-Extract-Waves-Standards.md
│   ├── CC-006-Extract-Space-Matter-Standards.md
│   ├── CC-007-PDF-Parser.md
│   ├── CC-008-Analyze-Question-Patterns.md
│   ├── CC-009-Extract-PLDs.md
│   ├── CC-010-Knowledge-Base-Schema.md
│   ├── CC-011-3D-Framework-Mapping.md
│   └── CC-012-Validate-Data-Create-TestSet.md
├── Epic-2-AI-Development/
│   ├── CC-EPIC-002-AI-Model-Development.md
│   ├── CC-013-Evaluate-LLM.md
│   ├── CC-014-Setup-Google-AI.md
│   ├── CC-015-Configure-Embeddings.md
│   ├── CC-016-Design-RAG-Architecture.md
│   ├── CC-017-Weaviate-Integration.md
│   ├── CC-018-System-Prompts.md
│   ├── CC-019-Few-Shot-Examples.md
│   ├── CC-020-Validation-Prompts.md
│   ├── CC-021-Context-Retrieval.md
│   ├── CC-022-Context-Formatting.md
│   ├── CC-023-Generation-Pipeline.md
│   ├── CC-024-Output-Formatting.md
│   ├── CC-025-Validation-Rules.md
│   ├── CC-026-Initial-Testing.md
│   └── CC-027-Iterate-Prompts.md
├── Epic-3-Validation-QA/
│   ├── CC-EPIC-003-Validation-QA.md
│   ├── CC-028-Validation-Framework-Design.md
│   ├── CC-029-SEP-Validator.md
│   ├── CC-030-CCC-Validator.md
│   ├── CC-031-DCI-Validator.md
│   ├── CC-032-3D-Alignment-Checker.md
│   ├── CC-033-Standard-Alignment-Validator.md
│   ├── CC-034-Context-Scoring.md
│   ├── CC-035-Difficulty-Classifier.md
│   ├── CC-036-Quality-Dashboard.md
│   └── CC-037-Comprehensive-Testing.md
└── Epic-4-UI-Integration/
    ├── CC-EPIC-004-UI-Integration.md
    ├── CC-038-UI-UX-Design.md
    ├── CC-039-React-Setup.md
    ├── CC-040-Stimulus-Input-Form.md
    ├── CC-041-Standards-Selector.md
    ├── CC-042-Configuration-Panel.md
    ├── CC-043-Question-Display.md
    ├── CC-044-Question-Editing.md
    ├── CC-045-Alignment-Visualization.md
    ├── CC-046-Export-Functionality.md
    ├── CC-047-Batch-Processing.md
    ├── CC-048-FastAPI-Backend.md
    └── CC-049-API-Documentation.md
```

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

| Epic | Stories | Estimated Story Points | Avg Points/Story |
|------|---------|------------------------|------------------|
| Epic 1 | 12 | 70 | 5.8 |
| Epic 2 | 15 | 106 | 7.1 |
| Epic 3 | 10 | 72 | 7.2 |
| Epic 4 | 12 | 87 | 7.3 |
| **Total** | **49** | **335** | **6.8** |

---

## Priority Breakdown

| Priority | Count |
|----------|-------|
| Highest | 18 |
| High | 22 |
| Medium | 7 |
| Low | 2 |

---

## Complete Story List

### Epic 1: Data Preparation (CC-001 to CC-012)
1. ✅ CC-001: Set up project infrastructure
2. ✅ CC-002: Create MHTML parser
3. ✅ CC-003: Extract Energy standards
4. ✅ CC-004: Extract Forces and Motion standards
5. ✅ CC-005: Extract Waves standards
6. ✅ CC-006: Extract Space Systems and Matter standards
7. ✅ CC-007: Create PDF parser
8. ✅ CC-008: Analyze question patterns
9. ✅ CC-009: Extract PLDs
10. ✅ CC-010: Design knowledge base schema
11. ✅ CC-011: Create 3D framework mapping
12. ✅ CC-012: Validate data and create test dataset

### Epic 2: AI Development (CC-013 to CC-027)
13. ✅ CC-013: Evaluate LLM options
14. ✅ CC-014: Set up Google AI Studio
15. ✅ CC-015: Configure embeddings
16. ✅ CC-016: Design RAG architecture
17. ✅ CC-017: Weaviate integration
18. ✅ CC-018: Create system prompts
19. ✅ CC-019: Develop few-shot examples
20. ✅ CC-020: Build validation prompts
21. ✅ CC-021: Implement context retrieval
22. ✅ CC-022: Create context formatting
23. ✅ CC-023: Build generation pipeline
24. ✅ CC-024: Implement output formatting
25. ✅ CC-025: Create validation rules
26. ✅ CC-026: Conduct initial testing
27. ✅ CC-027: Iterate on prompts

### Epic 3: Validation & QA (CC-028 to CC-037)
28. ✅ CC-028: Design validation framework
29. ✅ CC-029: Build SEP validator
30. ✅ CC-030: Build CCC validator
31. ✅ CC-031: Build DCI validator
32. ✅ CC-032: Build 3D alignment checker
33. ✅ CC-033: Implement standard alignment validator
34. ✅ CC-034: Build context scoring
35. ✅ CC-035: Create difficulty classifier
36. ✅ CC-036: Develop quality dashboard
37. ✅ CC-037: Comprehensive testing

### Epic 4: UI & Integration (CC-038 to CC-049)
38. ✅ CC-038: Design UI/UX mockups
39. ✅ CC-039: Set up React frontend
40. ✅ CC-040: Build stimulus input form
41. ✅ CC-041: Create standards selector
42. ✅ CC-042: Implement configuration panel
43. ✅ CC-043: Build question display
44. ✅ CC-044: Create question editing
45. ✅ CC-045: Implement alignment visualization
46. ✅ CC-046: Build export functionality
47. ✅ CC-047: Create batch processing
48. ✅ CC-048: Develop FastAPI backend
49. ✅ CC-049: Write API documentation

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
1. CC-XXX-01: Task 1
2. CC-XXX-02: Task 2

## Dependencies
- **Prerequisite**: CC-XXX
- **Required**: [Resources]

## Definition of Done
- [ ] All acceptance criteria met
- [ ] Code reviewed
- [ ] Tests passing
- [ ] Documentation updated

**Created**: YYYY-MM-DD  
**Assigned To**: TBD  
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
- `backend` - Backend API
- `epic-1`, `epic-2`, `epic-3`, `epic-4` - Epic associations
- `critical` - High priority/blocking

---

## How to Use These Tickets

1. **For Planning**: Review epics and stories to understand project scope
2. **For Development**: Pick up stories in order within each epic
3. **For Tracking**: Update story status as work progresses
4. **For Collaboration**: Add comments and updates directly to markdown files
5. **For Reporting**: Use story points and status for sprint planning

---

## Sprint Planning Recommendations

**Sprint 1-2** (Weeks 1-4): Epic 1 - Data Preparation  
**Sprint 3-5** (Weeks 5-10): Epic 2 - AI Development  
**Sprint 6-7** (Weeks 11-14): Epic 3 - Validation & QA  
**Sprint 8-9** (Weeks 15-18): Epic 4 - UI & Integration  

---

## Related Documents

- [Project Plan](../AG_ProjectPlan.md)
- [Product Naming](../ProductNameOptions.md)
- [Repository README](../README.md)

---

**Last Updated**: November 20, 2025  
**Maintained By**: Project Team  
**Total Stories**: 49 (100% complete)  
**Total Story Points**: ~335
