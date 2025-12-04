# Story: Build context appropriateness scoring system

**Story ID**: CC-034  
**Epic**: CC-EPIC-003  
**Story Type**: Feature  
**Priority**: High  
**Story Points**: 5  
**Status**: To Do  

---

## User Story

As a **validation engineer**, I want to **score context appropriateness** so that **questions properly utilize the provided stimulus**.

---

## Description

Build a scoring system that evaluates how well generated questions use and reference the provided stimulus scenario.

---

## Acceptance Criteria

- [ ] Context scoring algorithm implemented
- [ ] Scores range 0-100
- [ ] Checks stimulus reference
- [ ] Validates data usage
- [ ] Detects standalone questions
- [ ] Scoring accuracy >85%
- [ ] Unit tests written

---

## Scoring Criteria

1. **Direct Reference**: Question mentions stimulus elements (30 points)
2. **Data Usage**: Uses numerical data from stimulus (25 points)
3. **Scenario Integration**: Builds on stimulus context (25 points)
4. **Necessity**: Can't be answered without stimulus (20 points)

---

## Thresholds

- **Excellent**: 85-100
- **Good**: 70-84
- **Acceptable**: 60-69
- **Poor**: <60 (flag for review)

---

## Dependencies

- **Prerequisite**: CC-028 (Framework designed)

---

**Created**: November 20, 2025  
**Labels**: validation, context-scoring, epic-3
