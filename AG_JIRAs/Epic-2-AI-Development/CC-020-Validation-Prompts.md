# Story: Build dimension-specific validation prompts

**Story ID**: CC-020  
**Epic**: CC-EPIC-002  
**Story Type**: Feature  
**Priority**: High  
**Story Points**: 8  
**Status**: To Do  

---

## User Story

As an **AI engineer**, I want to **create prompts that validate dimensional alignment** so that **the system can self-check generated questions**.

---

## Description

Develop specialized prompts that use Gemini 3.0 to validate whether a generated question properly addresses each of the three dimensions.

---

## Acceptance Criteria

- [ ] SEP validation prompt created
- [ ] CCC validation prompt created
- [ ] DCI validation prompt created
- [ ] Integrated validation prompt created
- [ ] Prompts tested on sample questions
- [ ] Validation accuracy >90%
- [ ] Response format standardized

---

## Validation Prompts

1. **SEP Validator**: "Does this question require students to [practice]?"
2. **CCC Validator**: "Does this question address [concept]?"
3. **DCI Validator**: "Does this question test understanding of [idea]?"
4. **Integrated**: "Rate 3D alignment on scale 1-5"

---

## Dependencies

- **Prerequisite**: CC-018 (System prompts created)
- **Prerequisite**: CC-011 (3D mappings available)

---

**Created**: November 20, 2025  
**Labels**: validation-prompts, 3d-validation, epic-2
