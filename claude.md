# ClusterCraft Repository Overview

## Project Purpose

This is **ClusterCraft**, an AI-powered application that automatically generates NY State Regents Physics exam questions (called "Clusters") using long-context language models.

## What It Does

Given a real-world physics scenario and performance standards, it generates 1-3 test questions that assess students across three dimensions:
- **SEP** (Science & Engineering Practices)
- **CCC** (Cross-Cutting Concepts)
- **DCI** (Disciplinary Core Ideas)

## Core Technology Stack

- **Language**: Python 3.8+
- **LLM**: Google Gemini 1.5 Flash (cost-optimized)
- **Architecture**: Search-First (no vector database)
- **Key Dependencies**: PyYAML, Jinja2

## Repository Structure

| Component | Purpose |
|-----------|---------|
| `clustercraft/` | Production Python package with CLI and core modules |
| `Physics Teaching Standards/` | NY State standards organized by topic |
| `Performance Level Descriptors/` | Teaching context and requirements |
| `Sample Clusters/` | Reference exam questions with grading guides |
| `TechRefDocs/` | Research on AI cost reduction strategies |
| `PoC/` | Proof of concept demonstrating the search-first approach |

## Main Application Components

**`clustercraft/orchestrator.py`** - Main workflow engine
- Manages 4-step pipeline: Search → Build Prompt → Generate → Validate
- Coordinates between searcher, LLM, and validator components
- Supports dry-run mode for prompt preview

**`clustercraft/search.py`** - Context Search and Loading
- Searches Physics Teaching Standards and PLD directories using standard codes
- Normalizes standard code formats (handles both "HS-PS-2-1" and "HS-PS2-1")
- Implements caching system for loaded documents
- Returns context metadata: file count, character count, estimated token count

**`clustercraft/llm.py`** - LLM Client with Cost Tracking
- Handles API calls to Gemini models
- Implements retry logic with exponential backoff
- Tracks input/output tokens for cost analysis
- Estimates costs based on Gemini Flash pricing

**`clustercraft/validator.py`** - Cluster Quality Assurance
- Validates generated clusters against requirements
- Checks for stimulus, question count (1-3), answer keys
- Verifies standards referenced and three-dimensional framework coverage
- Returns structured validation results with errors and warnings

**`clustercraft/cli.py`** - Command-Line Interface
- Full-featured CLI supporting:
  - `--focus-standard`: Primary standard (required, e.g., "HS-PS-2-1")
  - `--ancillary-standards`: Additional standards (comma-separated, optional)
  - `--stimulus`: Scenario description (or use `--stimulus-file`)
  - `--dry-run`: Preview prompt without LLM call
  - `--verbose`: Enable debug logging
  - `--config`: Custom configuration file
- Outputs clusters to markdown files with metadata

## Key Features

### Search-First Architecture
- Eliminates expensive vector databases
- Leverages long context windows (1M+ tokens) from Gemini 1.5
- Direct file system search vs. fragmented vector chunks
- Significantly reduces token usage and costs

### Cost Optimization
**Cost Comparison:**
| Approach | Tokens | Cost | Savings |
|----------|--------|------|---------|
| Broad Topic Search | 3.0M | $0.23 | — |
| **Targeted Standards** | **1.2M** | **$0.09** | **61%** |
| Single Standard | 0.6M | $0.05 | 78% |

### Multi-Dimensional Validation
- Ensures questions assess students across SEP, CCC, and DCI dimensions
- Validates stimulus presence and quality
- Confirms answer keys and grading guidance
- Validates standards alignment

### Customizable Templates
- Jinja2-based prompt templates for easy customization
- YAML configuration for model parameters and data paths
- System instructions defining cluster requirements

## Configuration

**`config/settings.yaml`**:
- Data paths pointing to standards and PLD directories
- Model parameters (name, temperature, max_tokens)
- Search settings (file extensions, caching)
- Output format and logging configuration

## Usage Example

### Basic Generation
```bash
export GEMINI_API_KEY="your-api-key"

clustercraft --focus-standard "HS-PS-2-1" \
             --stimulus "A car braking on wet pavement"
```

### With Multiple Standards and Dry-Run
```bash
clustercraft --focus-standard "HS-PS-3-1" \
             --ancillary-standards "HS-PS-3-2,HS-PS-2-1" \
             --stimulus-file "./stimuli/example.md" \
             --dry-run
```

## Installation

```bash
pip install -e clustercraft  # From the repo root
```

## Data Sources

**Physics Teaching Standards** (in `Physics Teaching Standards/`)
- 19 standards files organized by topic
- Formats: mhtml, pdf
- Standards codes: HS-PS2-1, HS-PS3-1, HS-PS4-1, etc.
- Covers: Energy, Forces & Motion, Waves & Information, Space Systems, Structure & Properties of Matter

**Performance Level Descriptors** (in `Performance Level Descriptors/`)
- Provides additional teaching context and requirements
- Referenced alongside standards during generation

## Project Goals and Scope

**Primary Goal:**
Given a stimulus/scenario and Performance Expectation Standards, automatically generate 1-3 test questions that:
- Assess students across three dimensions (SEP, CCC, DCI)
- Include proper answer keys with grading guidance
- Align with specified physics standards
- Meet NY State Regents exam standards

**Three-Dimensional Assessment Model:**
1. **Dimension 1 (SEP)**: Science & Engineering Practices (what students *do*)
2. **Dimension 2 (CCC)**: Cross-Cutting Concepts (how students *think*)
3. **Dimension 3 (DCI)**: Disciplinary Core Ideas (what students *learn*)

## Testing

The project includes comprehensive test coverage:
- `clustercraft/tests/test_search.py` - Document search and context loading
- `clustercraft/tests/test_llm.py` - LLM generation and cost tracking
- `clustercraft/tests/test_validator.py` - Cluster validation logic
- `clustercraft/tests/test_utils.py` - Utility functions

Run tests with: `clustercraft/tests/run_tests.py`

## Key Accomplishments

- **Production-Ready**: Full CLI, error handling, and configuration management
- **Cost-Efficient**: Demonstrates 61% token reduction vs. broad topic searches
- **Well-Architected**: Modular design with clear separation of concerns
- **Validated Output**: Multi-dimensional quality checks ensure educational standards
- **Scalable**: Supports multiple standards and unlimited stimulus variations
- **Documented**: Comprehensive research on cost reduction strategies included

## Architecture Highlights

The project successfully balances:
- **Educational Accuracy**: Grounded in NY State standards and PLDs
- **Cost Efficiency**: Uses search-first architecture, eliminating expensive vector databases
- **Developer Experience**: Jinja2 templates for easy customization, comprehensive CLI
- **Quality Assurance**: Multi-dimensional validation framework
- **Scalability**: Supports multiple standards and stimulus variations
- **Maintainability**: Clear module organization and configuration management

This repository demonstrates thoughtful architectural decisions informed by technical research on AI cost reduction, making it both economical and maintainable for educational institutions generating physics assessments.
