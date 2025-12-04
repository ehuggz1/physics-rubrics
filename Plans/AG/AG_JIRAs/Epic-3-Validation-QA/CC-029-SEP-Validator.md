# Story: Build Dimension 1 (SEP) validator

**Story ID**: CC-029  
**Epic**: CC-EPIC-003  
**Story Type**: Feature  
**Priority**: Highest  
**Story Points**: 8  
**Status**: To Do  

---

## User Story

As a **validation engineer**, I want to **validate Science & Engineering Practices alignment** so that **questions properly assess scientific practices**.

---

## Description

Build a validator that checks if generated questions require students to engage in the specified Science & Engineering Practices.

---

## Acceptance Criteria

- [ ] SEP detection algorithm implemented
- [ ] All 8 SEP practices covered
- [ ] Validation accuracy >90%
- [ ] Confidence scores provided
- [ ] Integration with validation framework
- [ ] Unit tests written

---

## SEP Practices to Detect

1. Asking Questions and Defining Problems
2. Developing and Using Models
3. Planning and Carrying Out Investigations
4. Analyzing and Interpreting Data
5. Using Mathematics and Computational Thinking
6. Constructing Explanations
7. Engaging in Argument from Evidence
8. Obtaining, Evaluating, and Communicating Information

---

## Detection Methods

- Keyword matching
- Semantic similarity
- Question structure analysis
- Verb analysis (analyze, calculate, explain, etc.)

---

## Dependencies

- **Prerequisite**: CC-028 (Framework designed)
- **Prerequisite**: CC-011 (3D mappings)

---

**Created**: November 20, 2025  
**Labels**: validation, sep, dimension-1, epic-3
