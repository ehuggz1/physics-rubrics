# Story: Create system prompts for question generation

**Story ID**: CC-018  
**Epic**: CC-EPIC-002  
**Story Type**: Feature  
**Priority**: Highest  
**Story Points**: 13  
**Status**: To Do  

---

## User Story

As an **AI engineer**, I want to **create comprehensive system prompts** so that **Gemini 3.0 generates high-quality, 3D-aligned questions**.

---

## Description

Design and implement system prompts that instruct Gemini 3.0 on how to generate physics questions that test all three dimensions simultaneously.

---

## Acceptance Criteria

- [ ] Master system prompt created
- [ ] Dimension-specific instructions included
- [ ] Output format clearly specified
- [ ] Constraints and rules defined
- [ ] Prompts tested with sample stimuli
- [ ] Prompt library organized and versioned
- [ ] Documentation complete

---

## Prompt Components

1. **Role Definition**: "You are an expert physics assessment designer..."
2. **Task Description**: Generate 1-3 questions from stimulus
3. **3D Requirements**: Must test SEP, CCC, and DCI
4. **Format Specification**: JSON output structure
5. **Quality Criteria**: Clarity, difficulty, authenticity
6. **Constraints**: No recall-only, must use stimulus

---

## Dependencies

- **Prerequisite**: CC-008 (Question patterns analyzed)
- **Prerequisite**: CC-014 (Gemini access)

---

**Created**: November 20, 2025  
**Labels**: prompts, prompt-engineering, epic-2, critical
