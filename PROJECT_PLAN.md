# Physics Rubrics Project - Implementation Plan

## Project Overview

**Goal:** When given the story-line component of a Stimulus and an array of Performance Expectation Standards (e.g., HS-PS2-1, HS-PS3-1, HS-PS3-2), generate 1-3 test questions where each question tests the students' reasoning abilities in each of the 3 reasoning dimension requirements as defined in the Performance Expectation Standards.

**Date Created:** November 20, 2025
**Last Updated:** November 20, 2025

## System Architecture Overview

```mermaid
flowchart TB
    subgraph Input["Input Layer"]
        STIM[Storyline Stimulus]
        PEARRAY[Performance Expectation Array<br/>e.g., HS-PS2-1, HS-PS3-1, HS-PS3-2]
    end
    
    subgraph Knowledge["Knowledge Base"]
        NYSSLS[NYSSLS Physics Standards]
        PLDS[Performance Level Descriptors]
        MHTML[18 PE Documents<br/>.mhtml files]
        SAMPLES[Sample Clusters<br/>& Rating Guides]
    end
    
    subgraph Processing["Processing Engine"]
        DIMMAP[Dimension Mapper]
        QGEN[Question Generator]
        VALID[Validator]
        RUBRIC[Rubric Generator]
    end
    
    subgraph Output["Output Layer"]
        Q1[Question 1]
        Q2[Question 2]
        Q3[Question 3]
        SCORE[Scoring Rubrics<br/>Level 1-4]
    end
    
    STIM --> DIMMAP
    PEARRAY --> DIMMAP
    
    NYSSLS --> DIMMAP
    PLDS --> RUBRIC
    MHTML --> DIMMAP
    SAMPLES --> QGEN
    
    DIMMAP --> QGEN
    QGEN --> VALID
    VALID --> Q1
    VALID --> Q2
    VALID --> Q3
    
    Q1 --> RUBRIC
    Q2 --> RUBRIC
    Q3 --> RUBRIC
    RUBRIC --> SCORE
    
    style Input fill:#e1f5ff
    style Knowledge fill:#fff4e1
    style Processing fill:#e8f5e9
    style Output fill:#f3e5f5
```

## Three-Dimensional Assessment Framework

All questions must test student reasoning across three dimensions:

### Dimension 1: Science & Engineering Practices (What Students Do)
- Asking questions
- Developing models
- Planning investigations
- Analyzing Data
- Using Mathematics
- Engaging in arguments
- Communicating Information

### Dimension 2: Cross-Cutting Concepts (How Students Think)
- Cause and Effect
- Structure and Function
- Systems and System Models
- Scale Proportion and Quantity
- Stability and Change
- Energy and Matter
- Patterns

### Dimension 3: Disciplinary Core Ideas (What Students Learn)
- Topic-specific physics concepts from NYSSLS standards

### Three-Dimensional Integration Model

```mermaid
graph TD
    subgraph Question["Generated Question"]
        Q[Test Question]
    end
    
    subgraph D1["Dimension 1:<br/>Science & Engineering Practices"]
        SEP1[Asking Questions]
        SEP2[Developing Models]
        SEP3[Planning Investigations]
        SEP4[Analyzing Data]
        SEP5[Using Mathematics]
        SEP6[Engaging in Arguments]
        SEP7[Communicating Information]
    end
    
    subgraph D2["Dimension 2:<br/>Cross-Cutting Concepts"]
        CCC1[Cause and Effect]
        CCC2[Structure and Function]
        CCC3[Systems and System Models]
        CCC4[Scale Proportion and Quantity]
        CCC5[Stability and Change]
        CCC6[Energy and Matter]
        CCC7[Patterns]
    end
    
    subgraph D3["Dimension 3:<br/>Disciplinary Core Ideas"]
        DCI1[Forces and Motion]
        DCI2[Energy]
        DCI3[Waves and Information]
        DCI4[Space Systems]
        DCI5[Matter Properties]
    end
    
    Q -.Must Test.-> D1
    Q -.Must Test.-> D2
    Q -.Must Test.-> D3
    
    style Q fill:#ff6b6b,color:#fff
    style D1 fill:#4ecdc4
    style D2 fill:#95e1d3
    style D3 fill:#f38181
```

## Current Repository Assets

### 1. NYSSLS Physics Standards (Primary Reference)
- **Location:** `Physics Teaching Standards/NYSSLS Physics Standards.pdf`
- **Content:** Detailed student expectations for NY State Regents Physics
- **Purpose:** Comprehensive standards document defining what students need to learn and demonstrate

### 2. Performance Level Descriptors
- **Location:** `Performance Level Descriptors/Physics PLDs (1).pdf`
- **Content:** NY State requirements (PLDs) defining what students must demonstrate at each performance level (Level 1-4)
- **Purpose:** Provides the grading criteria framework and additional teaching requirements for the NY State Regents Physics course

### 3. Physics Teaching Standards (Detailed Breakdowns)
**Location:** `Physics Teaching Standards/` (organized by topic)

#### Forces and Motion (5 standards)
- HS-PS2-1 through HS-PS2-5

#### Energy (5 standards)
- HS-PS3-1 through HS-PS3-5

#### Waves and Information (6 standards)
- HS-PS4-1 through HS-PS4-5
- NY HS-PS4-6

#### Space Systems (1 standard)
- HS-ESS1-2

#### Structure and Properties of Matter (1 standard)
- HS-PS1-8

**Total:** 18 performance expectation documents (.mhtml files)

**Note:** These .mhtml files break out the student science and engineering practices, describing how students are to demonstrate their understanding of the learned performance expectations.

### 4. Sample Clusters
- **Location:** `Sample Clusters/`
- `sample-physics-clusters-2025.pdf` - 3 example clusters
- `sample-physics-clusters-ratingguide-2025.pdf` - Answer key and grading guidance

### Repository Structure

```mermaid
graph LR
    ROOT[physics-rubrics/]
    
    ROOT --> PLD[Performance Level Descriptors/]
    ROOT --> PTS[Physics Teaching Standards/]
    ROOT --> SC[Sample Clusters/]
    ROOT --> README[README.md]
    ROOT --> PLAN[PROJECT_PLAN.md]
    
    PLD --> PLDPDF[Physics PLDs.pdf]
    
    PTS --> NYSSLS[NYSSLS Physics Standards.pdf]
    PTS --> FM[Forces and Motion/]
    PTS --> EN[Energy/]
    PTS --> WI[Waves and Information/]
    PTS --> SS[Space Systems/]
    PTS --> SP[Structure and Properties/]
    
    FM --> PS21[HS-PS2-1.mhtml]
    FM --> PS22[HS-PS2-2.mhtml]
    FM --> PS23[HS-PS2-3.mhtml]
    FM --> PS24[HS-PS2-4.mhtml]
    FM --> PS25[HS-PS2-5.mhtml]
    
    EN --> PS31[HS-PS3-1.mhtml]
    EN --> PS32[HS-PS3-2.mhtml]
    EN --> PS33[HS-PS3-3.mhtml]
    EN --> PS34[HS-PS3-4.mhtml]
    EN --> PS35[HS-PS3-5.mhtml]
    
    WI --> PS41[HS-PS4-1.mhtml]
    WI --> PS42[HS-PS4-2.mhtml]
    WI --> PS43[HS-PS4-3.mhtml]
    WI --> PS44[HS-PS4-4.mhtml]
    WI --> PS45[HS-PS4-5.mhtml]
    WI --> PS46[NY HS-PS4-6.mhtml]
    
    SS --> ESS12[HS-ESS1-2.mhtml]
    SP --> PS18[HS-PS1-8.mhtml]
    
    SC --> SCPDF[sample-physics-clusters-2025.pdf]
    SC --> RGPDF[sample-physics-clusters-ratingguide-2025.pdf]
    
    style ROOT fill:#e3f2fd
    style PTS fill:#fff3e0
    style SC fill:#f3e5f5
    style PLD fill:#e8f5e9
```

## Implementation Plan

### Project Phases Timeline

```mermaid
gantt
    title Physics Rubrics Project Implementation Timeline
    dateFormat YYYY-MM-DD
    section Phase 1: Data Extraction
    Task 1: NYSSLS Standards          :t1, 2025-11-20, 3d
    Task 1b: PLDs Extraction          :t1b, after t1, 2d
    Task 2: Parse MHTML Files         :t2, after t1b, 5d
    Task 3: Analyze Sample Clusters   :t3, after t2, 3d
    
    section Phase 2: Knowledge Base
    Task 4: Data Models               :t4, after t3, 4d
    Task 5: Build Knowledge Base      :t5, after t4, 5d
    
    section Phase 3: Generation System
    Task 6: Question Framework        :t6, after t5, 7d
    Task 7: Question Templates        :t7, after t6, 5d
    Task 8: Validation System         :t8, after t7, 5d
    
    section Phase 4: Integration
    Task 9: Pipeline Integration      :t9, after t8, 7d
    Task 10: Rubric Generation        :t10, after t9, 5d
```

### Phase 1: Data Extraction & Understanding

#### Task 1: Extract and Parse NYSSLS Physics Standards
**Objective:** Parse the primary NYSSLS Physics Standards PDF to extract comprehensive student expectations

**Actions:**
- Extract text from NYSSLS Physics Standards.pdf
- Identify all performance expectations and detailed requirements
- Extract dimensional requirements for each standard
- Create base reference document

**Deliverable:** Structured NYSSLS standards reference document

---

#### Task 1b: Extract and Parse Performance Level Descriptors
**Objective:** Parse the Physics PLDs PDF to extract NY State grading requirements

**Actions:**
- Extract text from Physics PLDs (1).pdf
- Identify Level 1, 2, 3, and 4 criteria
- Map performance levels to assessment requirements
- Create structured data format for PLDs
- Link PLDs to NYSSLS standards

**Deliverable:** Structured PLD reference document/database

---

#### Task 2: Parse All Performance Expectations from MHTML Files
**Objective:** Extract detailed content from all 18 .mhtml files

**Actions:**
- Parse HTML content from .mhtml files
- Extract for each standard:
  - Performance expectation statement
  - Science and engineering practices
  - Disciplinary core ideas
  - Cross-cutting concepts
  - Assessment boundaries
  - Clarification statements
- Organize by topic area

**Deliverable:** Structured database of all 18 performance expectations

---

#### Task 3: Analyze Sample Clusters and Rating Guide
**Objective:** Understand existing cluster structure and 3D assessment patterns

**Actions:**
- Study the 3 sample clusters in detail (sample-physics-clusters-2025.pdf)
- Analyze question formats and types
- Map how each question tests across 3 dimensions
- Understand scoring rubrics from rating guide (sample-physics-clusters-ratingguide-2025.pdf)
- Identify patterns in stimulus-to-question connections
- Document cluster structure:
  - Stimulus sections (1-5 questions per stimulus)
  - Total 6-8 questions per cluster
  - How clusters focus on one core PE while incorporating others
  - How additional scenarios build story-lines

**Deliverable:** Analysis document with question patterns and cluster structure templates

---

### Phase 2: Knowledge Base Construction

#### Task 4: Create Data Models for 3-Dimensional Assessment
**Objective:** Design data structures for the three reasoning dimensions

**Actions:**
- Define schema for Science & Engineering Practices (7 practices)
- Define schema for Cross-Cutting Concepts (7 concepts)
- Define schema for Disciplinary Core Ideas (topic-specific)
- Create mapping structure between performance expectations and dimensions
- Design relationship model showing how dimensions interact

**Deliverable:** Data model documentation and schemas

---

#### Task 5: Build Performance Expectation Knowledge Base
**Objective:** Create comprehensive, structured database of all standards

**Actions:**
- Organize all 18 performance expectations by topic
- Map each PE to its dimensional components:
  - Associated science practices
  - Related cross-cutting concepts
  - Core disciplinary ideas
- Include assessment boundaries
- Add clarification statements
- Link related performance expectations

**Deliverable:** Queryable knowledge base (JSON/database format)

---

### Phase 3: Generation System Development

#### Task 6: Develop Question Generation Framework
**Objective:** Core system to generate questions from stimulus + PE array

**Actions:**
- Design input interface (storyline stimulus + PE Standards array)
- Create dimension analyzer to identify dimensional requirements from each PE Standard
- Develop question generation engine
- Implement PE combination logic for multi-standard questions
- Build stimulus-to-question connection algorithm
- Ensure each question tests all 3 dimensional requirements as defined in the PE Standards
- Incorporate NYSSLS standards requirements into generation logic

**Deliverable:** Question generation core module

---

#### Task 7: Create Templates for Question Types
**Objective:** Build templates for various assessment formats

**Actions:**
- Create templates for:
  - Calculation/quantitative questions
  - Graph/data analysis questions
  - Model evaluation questions
  - Experimental design questions
  - Argument evaluation questions
  - Qualitative reasoning questions
- Map question types to dimensional requirements
- Develop template selection logic

**Deliverable:** Question template library

---

#### Task 8: Implement Validation System
**Objective:** Ensure generated questions meet all requirements

**Actions:**
- Build validators for:
  - Performance expectation alignment
  - 3-dimensional coverage (all dimensions tested)
  - Stimulus-storyline connection
  - Appropriate difficulty level per PLDs
  - Question clarity and answerable format
- Create feedback mechanism for failed validation
- Implement quality scoring system

**Deliverable:** Validation module with quality metrics

---

### Phase 4: Integration & Testing

#### Task 9: Create Sample Question Generation Pipeline
**Objective:** Complete end-to-end workflow

**Actions:**
- Integrate all modules into single pipeline
- Implement: Input → Dimension Mapping → Question Generation → Validation → Output
- Create user interface/API for inputs
- Format outputs (questions with scoring guidance)
- Add error handling and logging
- Test with various stimulus scenarios

**Deliverable:** Working prototype system

---

#### Task 10: Develop Automated Rubric Generation
**Objective:** Generate scoring rubrics based on PLDs

**Actions:**
- Map question components to PLD levels
- Generate rubric showing Level 1, 2, 3, 4 responses
- Describe dimensional requirements for each level
- Include sample acceptable responses
- Format for teacher use

**Deliverable:** Automated rubric generation system

---

## Question Generation Workflow

```mermaid
flowchart TD
    START([Start: User Input])
    INPUT[/"Input:<br/>- Storyline Stimulus<br/>- PE Standards Array"/]
    
    LOAD[Load Knowledge Base]
    
    EXTRACT[Extract Dimensional<br/>Requirements from PEs]
    
    subgraph DIM["For Each PE Standard"]
        D1[Identify Required<br/>Science Practices]
        D2[Identify Required<br/>Cross-Cutting Concepts]
        D3[Identify Required<br/>Core Ideas]
    end
    
    COMBINE[Combine Requirements<br/>Across All PEs]
    
    ANALYZE[Analyze Stimulus<br/>for Connection Points]
    
    SELECT[Select Question<br/>Type Template]
    
    GEN[Generate Question<br/>Draft]
    
    VALIDATE{Validation Checks}
    
    CHECK1{All 3 Dimensions<br/>Tested?}
    CHECK2{Connected to<br/>Stimulus?}
    CHECK3{Aligns with<br/>PEs?}
    CHECK4{Appropriate<br/>Difficulty?}
    
    REFINE[Refine Question]
    ACCEPT[Accept Question]
    
    COUNT{Generated<br/>1-3 Questions?}
    
    RUBRIC[Generate Scoring<br/>Rubric for Each Question]
    
    OUTPUT[/"Output:<br/>- Questions<br/>- Rubrics"/]
    FINISH([End])
    
    START --> INPUT
    INPUT --> LOAD
    LOAD --> EXTRACT
    EXTRACT --> DIM
    DIM --> D1 & D2 & D3
    D1 & D2 & D3 --> COMBINE
    COMBINE --> ANALYZE
    ANALYZE --> SELECT
    SELECT --> GEN
    GEN --> VALIDATE
    
    VALIDATE --> CHECK1
    CHECK1 -->|No| REFINE
    CHECK1 -->|Yes| CHECK2
    CHECK2 -->|No| REFINE
    CHECK2 -->|Yes| CHECK3
    CHECK3 -->|No| REFINE
    CHECK3 -->|Yes| CHECK4
    CHECK4 -->|No| REFINE
    CHECK4 -->|Yes| ACCEPT
    
    REFINE --> GEN
    ACCEPT --> COUNT
    COUNT -->|No| SELECT
    COUNT -->|Yes| RUBRIC
    RUBRIC --> OUTPUT
    OUTPUT --> FINISH
    
    style START fill:#4caf50,color:#fff
    style FINISH fill:#4caf50,color:#fff
    style VALIDATE fill:#ff9800,color:#fff
    style CHECK1 fill:#2196f3,color:#fff
    style CHECK2 fill:#2196f3,color:#fff
    style CHECK3 fill:#2196f3,color:#fff
    style CHECK4 fill:#2196f3,color:#fff
    style ACCEPT fill:#4caf50,color:#fff
    style REFINE fill:#f44336,color:#fff
```

## Data Model Relationships

```mermaid
erDiagram
    PERFORMANCE_EXPECTATION ||--o{ SCIENCE_PRACTICE : requires
    PERFORMANCE_EXPECTATION ||--o{ CROSS_CUTTING_CONCEPT : requires
    PERFORMANCE_EXPECTATION ||--o{ DISCIPLINARY_CORE_IDEA : requires
    PERFORMANCE_EXPECTATION ||--o{ ASSESSMENT_BOUNDARY : defines
    PERFORMANCE_EXPECTATION ||--|| TOPIC_AREA : belongs_to
    
    QUESTION ||--|| STIMULUS : based_on
    QUESTION ||--o{ PERFORMANCE_EXPECTATION : tests
    QUESTION ||--o{ SCIENCE_PRACTICE : demonstrates
    QUESTION ||--o{ CROSS_CUTTING_CONCEPT : applies
    QUESTION ||--o{ DISCIPLINARY_CORE_IDEA : assesses
    QUESTION ||--|| RUBRIC : has
    
    RUBRIC ||--o{ PLD_LEVEL : contains
    
    CLUSTER ||--o{ STIMULUS : contains
    STIMULUS ||--o{ QUESTION : generates
    
    PERFORMANCE_EXPECTATION {
        string id PK
        string statement
        string topic_area
        string clarification
    }
    
    SCIENCE_PRACTICE {
        string id PK
        string name
        string description
    }
    
    CROSS_CUTTING_CONCEPT {
        string id PK
        string name
        string description
    }
    
    DISCIPLINARY_CORE_IDEA {
        string id PK
        string name
        string description
        string topic
    }
    
    QUESTION {
        string id PK
        string text
        string type
        string difficulty
    }
    
    STIMULUS {
        string id PK
        string storyline
        string scenario
    }
    
    RUBRIC {
        string id PK
        string question_id FK
    }
    
    PLD_LEVEL {
        int level PK
        string criteria
        string description
    }
    
    CLUSTER {
        string id PK
        string focus_pe
        int question_count
    }
```

## Success Criteria

A successful implementation will:

1. ✓ Accept a storyline stimulus and array of Performance Expectation Standards as input
2. ✓ Generate 1-3 questions that are directly connected to the stimulus storyline
3. ✓ Ensure each question tests student reasoning across all 3 dimensional requirements as defined in the Performance Expectation Standards:
   - **Dimension 1:** Science & Engineering Practices (What Students Do)
   - **Dimension 2:** Cross-Cutting Concepts (How Students Think)  
   - **Dimension 3:** Disciplinary Core Ideas (What Students Learn)
4. ✓ Align questions with specified Performance Expectation Standards from NYSSLS
5. ✓ Produce questions at appropriate difficulty levels per NYS PLDs (Level 1-4)
6. ✓ Generate scoring rubrics showing Level 1-4 criteria for each question
7. ✓ Validate questions meet all dimensional and alignment requirements
8. ✓ Follow cluster structure format (stimulus with 1-5 questions, building storylines)

## Technology Considerations

### Recommended Approach
- **Data Storage:** JSON or SQLite for knowledge base
- **Parser:** Python (for PDF/HTML parsing)
- **Question Generation:** Template-based with AI enhancement options
- **Validation:** Rule-based system with quality metrics
- **Interface:** CLI or web-based API

### Key Dependencies
- PDF parsing library (PyPDF2, pdfplumber)
- HTML/MHTML parsing (BeautifulSoup, lxml)
- Data validation framework
- Natural language processing (optional, for advanced features)

## Next Steps

1. Begin Phase 1, Task 1: Extract NYSSLS Physics Standards PDF
2. Continue with Task 1b: Extract Performance Level Descriptors
3. Set up project structure and development environment
4. Create data directory for extracted content
5. Establish version control for knowledge base
6. Document extraction and parsing procedures

## Key Definitions

### Cluster
A "story-line" composed of one or more real-world scenarios and related test questions which can be used in the Regents Exam. Each cluster consists of:

- **Stimulus/Stimuli:** One or more sections building on the storyline
  - Each stimulus includes: description, possibly graphs, tables, diagrams, and models
  - A completed stimulus section includes 1-5 questions related to the stimulus
- **Real-world scenario:** Situation where students apply scientific reasoning from Physics class
- **Questions:** Up to 6-8 questions total related to the real-world scenario
- **Additional scenarios:** May be included to create more detailed story-lines with additional questions
- **Focus:** Each cluster focuses on one performance expectation as defined in NYSSLS Physics Standard, while including other related performance expectations
- **Purpose:** Test students' ability to apply science and engineering practices using cross-cutting concepts from other related scientific ideas
- **3-Dimensional Approach:** MUST test students' abilities across all three dimensions

## Notes

- The NYSSLS Physics Standards.pdf is the primary comprehensive reference document
- The .mhtml files are archived web pages from thewonderofscience.com providing detailed breakdowns
- Each performance expectation has detailed breakdowns of practices and concepts in the .mhtml files
- Sample clusters provide concrete examples of the desired output format
- Focus on systematic, validated question generation rather than random generation
- Maintain alignment with NY State Regents Physics requirements throughout
- Each question MUST test all 3 dimensional requirements as specified in the Performance Expectation Standards

## Cluster Structure Visualization

```mermaid
graph TB
    subgraph CLUSTER["Physics Cluster"]
        FOCUS[Focus PE Standard<br/>e.g., HS-PS2-1]
        
        subgraph STIM1["Stimulus 1"]
            S1DESC[Real-World Scenario<br/>Description, Graphs, Tables]
            S1Q1[Question 1]
            S1Q2[Question 2]
            S1Q3[Question 3]
        end
        
        subgraph STIM2["Stimulus 2 (Optional)"]
            S2DESC[Extended Scenario<br/>Building on Storyline]
            S2Q1[Question 4]
            S2Q2[Question 5]
        end
        
        subgraph STIM3["Stimulus 3 (Optional)"]
            S3DESC[Additional Context]
            S3Q1[Question 6]
            S3Q2[Question 7]
            S3Q3[Question 8]
        end
        
        RELATED[Related PE Standards<br/>HS-PS3-1, HS-PS3-2, etc.]
    end
    
    FOCUS --> STIM1
    FOCUS --> STIM2
    FOCUS --> STIM3
    
    RELATED -.supports.-> STIM1
    RELATED -.supports.-> STIM2
    RELATED -.supports.-> STIM3
    
    S1DESC --> S1Q1 & S1Q2 & S1Q3
    S2DESC --> S2Q1 & S2Q2
    S3DESC --> S3Q1 & S3Q2 & S3Q3
    
    S1Q1 & S1Q2 & S1Q3 -.3D Test.-> DIMS
    S2Q1 & S2Q2 -.3D Test.-> DIMS
    S3Q1 & S3Q2 & S3Q3 -.3D Test.-> DIMS
    
    DIMS[All Questions Test:<br/>✓ Science Practices<br/>✓ Cross-Cutting Concepts<br/>✓ Core Ideas]
    
    style CLUSTER fill:#e3f2fd
    style FOCUS fill:#ff6b6b,color:#fff
    style RELATED fill:#4ecdc4
    style DIMS fill:#95e1d3
    style STIM1 fill:#fff9c4
    style STIM2 fill:#fff9c4
    style STIM3 fill:#fff9c4
```

## Performance Expectation Standards Coverage

```mermaid
pie title 18 Performance Expectations by Topic Area
    "Forces and Motion" : 5
    "Energy" : 5
    "Waves and Information" : 6
    "Space Systems" : 1
    "Matter Properties" : 1
```
