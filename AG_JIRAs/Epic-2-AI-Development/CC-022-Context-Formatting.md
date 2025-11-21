# Story: Create context injection and formatting system

**Story ID**: CC-022  
**Epic**: CC-EPIC-002  
**Story Type**: Feature  
**Priority**: Highest  
**Story Points**: 5  
**Status**: To Do  

---

## User Story

As an **AI engineer**, I want to **format retrieved context into prompts** so that **Gemini 3.0 receives well-structured input**.

---

## Description

Build a system that takes retrieved context and formats it into a structured prompt for Gemini 3.0, ensuring optimal context utilization within token limits.

---

## Acceptance Criteria

- [ ] Context formatting function created
- [ ] Prompt template system implemented
- [ ] Token counting integrated
- [ ] Context truncation strategy defined
- [ ] Priority-based context inclusion
- [ ] Final prompt validation
- [ ] Unit tests written

---

## Prompt Structure

```
SYSTEM: [Role and instructions]

STANDARDS:
[Selected standard(s) details]

DIMENSIONS:
SEP: [practices]
CCC: [concepts]
DCI: [core ideas]

EXAMPLES:
[Few-shot examples]

STIMULUS:
[User's scenario]

TASK:
Generate 1-3 questions...
```

---

## Dependencies

- **Prerequisite**: CC-021 (Context retrieval)
- **Prerequisite**: CC-018 (System prompts)

---

**Created**: November 20, 2025  
**Labels**: context-formatting, prompts, epic-2
