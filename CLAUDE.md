# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is **swf (Software WorkFlow)**, an AI-driven requirements analysis system that uses Agent+Skill architecture to automate software requirements analysis. The system guides users from raw, ambiguous requirements to structured, actionable outputs through a multi-stage workflow.

**Important Constraints**:
- This project defines workflows, NOT code development
- All outputs are Markdown documents
- Documents must NOT contain any code
- All diagrams must use Mermaid syntax
- Skills are designed for AI IDEs like Claude Code, Codex, and Trae

## Architecture

### Single Coordinator Agent Architecture

The system uses a single main coordinator Agent that executes all Skills serially with embedded validation and user interaction within each Skill.

```
User Input → Coordinator Agent → Skills (S0→S1→S2→S3→S4) → Final Report
                                    ↓
                            Todo-List (state tracking)
```

### Directory Structure

```
swf/
├── agents/                    # Agent definitions
│   ├── coordinator.md         # Main coordinator agent (primary)
│   └── requirements-analyst.md # Alternative requirements analyst
├── skills/                    # 14 Skills organized by stage
│   ├── s0-plan/               # S0-S001: Plan definition
│   ├── s1-boundary/           # S1-S101: Requirement boundary
│   ├── s1-explicit/           # S1-S102: Explicit requirements
│   ├── s1-implicit/           # S1-S103: Implicit requirements
│   ├── s1-validation/         # S1-S104: Requirements validation
│   ├── s2-competitor/         # S2-S201: Competitor analysis
│   ├── s2-market-analysis/    # S2-S202: Market validation
│   ├── s3-risk/               # S3-S301: Risk identification
│   ├── s3-feasibility/        # S3-S302: Technical feasibility
│   ├── s3-selection/          # S3-S303: Technology selection
│   ├── s4-classify/           # S4-S401: Requirements classification
│   ├── s4-priority/           # S4-S402: Requirements prioritization
│   ├── s4-core/               # S4-S403: Core requirements extraction
│   └── s4-prototype/          # S4-S404: Prototype design
├── templates/                 # Output templates
│   ├── user-interaction/      # User interaction templates
│   │   ├── clarification-template.md      # Requirement clarification
│   │   ├── information-collection-template.md  # Information collection
│   │   └── option-selection-template.md   # Option selection
│   ├── quality-standard.md    # ISO/IEC 25010 quality standard
│   ├── error-code-standard.md # Unified error code standard (E001-E999)
│   └── skill-structure-reference.md  # Skill 6-section structure reference
├── .trae/                     # Progress tracking
│   ├── rules/                 # Project rules
│   └── progress/              # Daily progress logs
├── WORKFLOW.md                # Main workflow documentation
└── srs.md                     # System requirements specification
```

### Skill Stages

| Stage | Skill ID | Directory | Purpose |
|-------|----------|-----------|---------|
| S0 | S001 | s0-plan/ | Plan definition, ID generation, completeness scoring |
| S1 | S101 | s1-boundary/ | Requirement boundary definition |
| S1 | S102 | s1-explicit/ | Explicit requirements collection |
| S1 | S103 | s1-implicit/ | Implicit requirements analysis |
| S1 | S104 | s1-validation/ | Requirements validation |
| S2 | S201 | s2-competitor/ | Competitor analysis |
| S2 | S202 | s2-market-analysis/ | Market pain point validation |
| S3 | S301 | s3-risk/ | Risk identification |
| S3 | S302 | s3-feasibility/ | Technical feasibility analysis |
| S3 | S303 | s3-selection/ | Technology selection |
| S4 | S401 | s4-classify/ | Requirements classification |
| S4 | S402 | s4-priority/ | Requirements prioritization |
| S4 | S403 | s4-core/ | Core requirements extraction |
| S4 | S404 | s4-prototype/ | Prototype design |

## Execution Modes

The system automatically selects execution mode based on information completeness score (0-100):

| Mode | Threshold | Description |
|------|-----------|-------------|
| Normal | Score < 90 | Full 14-skill execution with deep analysis |
| Lightweight | Score ≥ 90 | Skips S103, S201, S202, S404 for faster execution |

## Key Files to Reference

- **WORKFLOW.md**: Complete workflow documentation including user review process, change management, and prototype design
- **agents/coordinator.md**: Main agent execution flow, state management, and Todo-List rules
- **skills/s0-plan/SKILL.md**: Entry point skill with scoring methodology
- **srs.md**: Full system requirements specification

## Output Artifact Paths

All outputs are stored in `database/`:

```
database/
├── plans/{PlanID}.md              # Plan definition
├── plans/{PlanID}/todo-list.md    # Task tracking (single source of truth)
└── stages/{s0-s4}/                # Skill outputs by stage
```

## Product ID Format

- Plan ID: `P{6 digits}` (e.g., P000001)
- Skill Output ID: `{PlanID}-S{Stage}-{SkillID}-{seq}` (e.g., P000001-S0-S001-001, P000001-S1-S101-001)

## Skill Definition Standards

Each Skill follows a consistent 6-section structure:

### Section 1: Meta Information
- Skill ID, Name, English Name
- Stage, Execution Order
- Execution Mode, Dependencies, Post-Skills
- Version, Last Update Time

### Section 2: Functional Description
- Core responsibilities
- Input specifications (standardized input, validation rules)
- Output specifications (standardized output, artifact list)

### Section 3: Execution Process
- Process overview (Mermaid flowchart)
- Detailed step descriptions (objectives, operations, validation rules, error handling)
- **Demo examples** (input example, processing, output example)

### Section 4: Artifact Specifications
- Artifact ID naming rules
- Storage path structure
- Artifact version management

### Section 5: Quality Standards (ISO/IEC 25010)
- Quality assessment framework (5-dimension weights)
- Checklist (specific check items for each dimension)
- **Quality score calculation**
- **Acceptance criteria (≥85%)**
- **Non-compliance handling process** (re-execution mechanism)

### Section 6: Error Handling
- Error classification and code table (E001-E999)
- Error handling flowchart
- **User interaction protocols** (clarification, options, information collection)
- Error recovery strategies

### User Interaction Templates

All Skills use standardized interaction templates:
- **Clarification**: [templates/user-interaction/clarification-template.md](templates/user-interaction/clarification-template.md)
- **Information Collection**: [templates/user-interaction/information-collection-template.md](templates/user-interaction/information-collection-template.md)
- **Option Selection**: [templates/user-interaction/option-selection-template.md](templates/user-interaction/option-selection-template.md)

### Quality Standards Reference

All Skills follow the quality assessment framework:
- **Quality Standard**: [templates/quality-standard.md](templates/quality-standard.md)
- **Error Code Standard**: [templates/error-code-standard.md](templates/error-code-standard.md)

## Key Rules (from .trae/rules/swf-rule.md)

1. This is workflow definition, not code development
2. Skills are designed for AI IDEs (Claude Code, Codex, Trae)
3. All document outputs must be Markdown format
4. Documents cannot contain any code
5. Flowcharts must use Mermaid syntax
6. Reference: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
