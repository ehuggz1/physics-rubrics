# Story: Build stimulus input form component

**Story ID**: CC-040  
**Epic**: CC-EPIC-004 (User Interface & Integration)  
**Story Type**: Feature  
**Priority**: High  
**Story Points**: 8  
**Status**: To Do  

---

## User Story

As a **physics teacher**, I want to **easily input my storyline stimulus through an intuitive web interface** so that **I can quickly generate assessment questions without technical barriers**.

---

## Description

Create a user-friendly React component for inputting physics problem stimuli. The component should support rich text editing, optional file uploads for diagrams/graphs, and provide helpful guidance on writing effective stimuli.

---

## Acceptance Criteria

- [ ] Rich text editor supports formatting (bold, italic, lists, etc.)
- [ ] Users can paste text from Word/Google Docs without formatting issues
- [ ] Optional image upload for diagrams, graphs, or tables
- [ ] Character count display (recommend 200-500 words)
- [ ] Real-time validation and helpful error messages
- [ ] Save draft functionality (local storage)
- [ ] Example stimuli available for reference
- [ ] Responsive design works on desktop and tablet
- [ ] Accessibility compliant (WCAG 2.1 AA)

---

## UI/UX Design

### Component Layout

```
┌─────────────────────────────────────────────────────────┐
│  Stimulus Input                                    [?]  │
├─────────────────────────────────────────────────────────┤
│  ┌───────────────────────────────────────────────────┐ │
│  │ Title: [Roller Coaster Energy Conservation    ]  │ │
│  └───────────────────────────────────────────────────┘ │
│                                                         │
│  ┌───────────────────────────────────────────────────┐ │
│  │ [B] [I] [U] [List] [Link] [Image]                │ │
│  ├───────────────────────────────────────────────────┤ │
│  │                                                   │ │
│  │ A roller coaster car with mass 500 kg starts    │ │
│  │ from rest at point A, 30 meters above the       │ │
│  │ ground. The car descends to point B at ground   │ │
│  │ level, then climbs to point C at 20 meters...   │ │
│  │                                                   │ │
│  │ [Diagram: roller-coaster.png]                    │ │
│  │                                                   │ │
│  └───────────────────────────────────────────────────┘ │
│                                                         │
│  📊 Word count: 247 / 500 recommended                  │
│                                                         │
│  [📎 Upload Image] [💾 Save Draft] [👁️ Preview]       │
│                                                         │
│  💡 Tips for writing effective stimuli:                │
│  • Use real-world scenarios students can relate to     │
│  • Include specific numerical values                   │
│  • Reference diagrams or data when applicable          │
│  • Keep it concise but provide sufficient context      │
│                                                         │
│  [View Example Stimuli]                                │
└─────────────────────────────────────────────────────────┘
```

---

## Technical Tasks

### Sub-tasks

1. **CC-040-01**: Set up React component structure
2. **CC-040-02**: Integrate rich text editor library (TipTap or Draft.js)
3. **CC-040-03**: Implement title input field with validation
4. **CC-040-04**: Build rich text editing toolbar
5. **CC-040-05**: Add image upload functionality
6. **CC-040-06**: Implement character/word counter
7. **CC-040-07**: Create validation logic and error messages
8. **CC-040-08**: Build save draft feature (localStorage)
9. **CC-040-09**: Create example stimuli modal/drawer
10. **CC-040-10**: Add tips and guidance section
11. **CC-040-11**: Implement preview functionality
12. **CC-040-12**: Add accessibility features (ARIA labels, keyboard navigation)
13. **CC-040-13**: Create responsive design for tablet
14. **CC-040-14**: Write component tests (Jest + React Testing Library)
15. **CC-040-15**: Integrate with parent form state management

---

## Technical Specifications

### Component Props

```typescript
interface StimulusInputProps {
  value: StimulusData;
  onChange: (data: StimulusData) => void;
  onValidate?: (isValid: boolean) => void;
  maxLength?: number;
  required?: boolean;
}

interface StimulusData {
  title: string;
  description: string;
  images?: ImageFile[];
  contextType: 'real_world' | 'theoretical' | 'experimental';
}

interface ImageFile {
  id: string;
  file: File;
  url: string;
  caption?: string;
}
```

### Validation Rules

| Field | Rule | Error Message |
|-------|------|---------------|
| Title | Required, 5-100 chars | "Title must be between 5 and 100 characters" |
| Description | Required, 50-2000 chars | "Description must be between 50 and 2000 characters" |
| Images | Optional, max 3, <5MB each | "Maximum 3 images, each under 5MB" |

---

## Rich Text Editor Features

**Supported Formatting:**
- Bold, Italic, Underline
- Bulleted and numbered lists
- Hyperlinks
- Inline images
- Subscript/Superscript (for scientific notation)
- Special characters (Greek letters, mathematical symbols)

**Not Supported:**
- Tables (use image upload instead)
- Complex formatting (colors, fonts)
- Embedded videos

---

## Example Stimuli

### Example 1: Energy Conservation
```
Title: Roller Coaster Energy Transformations

A roller coaster car with mass 500 kg starts from rest at point A, 
30 meters above the ground. The car descends to point B at ground 
level, then climbs to point C at 20 meters above the ground. 
Assume friction is negligible.

[Diagram showing points A, B, and C with heights marked]
```

### Example 2: Collision
```
Title: Momentum in Vehicle Collision

Two cars approach an intersection. Car A (mass 1200 kg) travels 
east at 15 m/s. Car B (mass 1500 kg) travels north at 12 m/s. 
The cars collide and stick together.

[Diagram showing before and after collision]
```

---

## Dependencies

- **Prerequisite**: CC-039 (React frontend project setup)
- **Libraries**: 
  - TipTap or Draft.js (rich text editor)
  - React Dropzone (file upload)
  - Zod or Yup (validation)

---

## Definition of Done

- [ ] Component renders correctly
- [ ] All formatting features work
- [ ] Image upload functional
- [ ] Validation working as specified
- [ ] Save draft persists across sessions
- [ ] Example stimuli accessible
- [ ] Responsive on desktop and tablet
- [ ] Accessibility audit passed
- [ ] Unit tests >80% coverage
- [ ] Integration with form state working

---

## Accessibility Requirements

- [ ] All form fields have proper labels
- [ ] Keyboard navigation fully functional
- [ ] Screen reader compatible
- [ ] Focus indicators visible
- [ ] Error messages announced to screen readers
- [ ] Color contrast meets WCAG AA standards
- [ ] Alt text for all images

---

## Performance Requirements

- Component renders in <200ms
- Rich text editor responsive (no lag when typing)
- Image upload shows progress indicator
- Draft saves within 500ms

---

## Notes

- Consider using TipTap (more modern, better React integration)
- Store drafts in localStorage with timestamp
- Provide clear guidance on what makes a good stimulus
- Consider adding a "stimulus quality checker" in future iteration

---

## Related Stories

- **Depends On**: CC-039 (React frontend setup)
- **Related To**: CC-041 (Standards selector component)
- **Blocks**: CC-048 (API integration)

---

**Created**: November 20, 2025  
**Assigned To**: TBD  
**Reporter**: TBD  
**Labels**: frontend, ui-component, epic-4, user-input
