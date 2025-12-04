# Story: Set up Google AI Studio and Vertex AI access

**Story ID**: CC-014  
**Epic**: CC-EPIC-002  
**Story Type**: Task  
**Priority**: Highest  
**Story Points**: 5  
**Status**: To Do  

---

## User Story

As a **technical lead**, I want to **set up Google AI Studio and Vertex AI access** so that **the team can use Gemini 3.0 Pro for question generation**.

---

## Description

Configure Google Cloud Platform project and enable Vertex AI/AI Studio as the **Runtime API Provider** for the deployed application. This is distinct from the AntiGravity IDE used for development.

---

## Acceptance Criteria

- [ ] GCP project created
- [ ] Vertex AI API enabled
- [ ] Service account created with appropriate permissions
- [ ] API keys/credentials securely stored
- [ ] Development environment configured
- [ ] Production environment configured
- [ ] Rate limits and quotas understood
- [ ] Billing alerts set up
- [ ] Team access granted

---

## Technical Tasks

1. **CC-014-01**: Create GCP project
2. **CC-014-02**: Enable Vertex AI API
3. **CC-014-03**: Enable Gemini API
4. **CC-014-04**: Create service account
5. **CC-014-05**: Generate and secure API keys
6. **CC-014-06**: Configure environment variables
7. **CC-014-07**: Set up billing and quotas
8. **CC-014-08**: Test API connectivity
9. **CC-014-09**: Document setup process

---

## Security Considerations

- Store credentials in Google Secret Manager
- Use service accounts (not user accounts)
- Implement least privilege access
- Enable audit logging
- Set up billing alerts

---

## Dependencies

- **Prerequisite**: CC-013 (LLM selected)
- **Required**: GCP account with billing enabled
- **Required**: Budget approval

---

**Created**: November 20, 2025  
**Labels**: setup, gcp, gemini, epic-2, infrastructure
