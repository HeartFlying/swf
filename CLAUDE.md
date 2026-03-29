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

### Three-Stage Coordinator Agent Architecture

The system uses three coordinator Agents that execute Skills serially with embedded validation and user interaction within each Skill.

```
User Input → coordinator-requirements (S0→S1→S2→S3→S4)
                    ↓
            coordinator-architecture (S5)
                    ↓
            coordinator-detailed-design (S6)
                    ↓
                Final Report
                    ↓
            Todo-List (state tracking)
```

### Directory Structure

```
swf/
├── agents/                    # Agent definitions
│   ├── coordinator-requirements.md    # Requirements analysis agent (S0-S4)
│   ├── coordinator-architecture.md    # Architecture design agent (S5)
│   └── coordinator-detailed-design.md # Detailed design agent (S6)
├── skills/                    # 27 Skills organized by stage
│   ├── s0-plan/               # S001: Plan definition
│   ├── s1-competitor/         # S101: Competitor analysis
│   ├── s1-market-analysis/    # S102: Market validation
│   ├── s2-boundary/           # S201: Requirement boundary
│   ├── s2-explicit/           # S202: Explicit requirements
│   ├── s2-implicit/           # S203: Implicit requirements
│   ├── s2-validation/         # S204: Requirements validation
│   ├── s3-feasibility/        # S301: Technical feasibility
│   ├── s3-selection/          # S302: Technology selection
│   ├── s3-nfr/                # S303: Non-functional requirements
│   ├── s3-risk/               # S304: Risk identification
│   ├── s4-classify/           # S401: Requirements classification
│   ├── s4-priority/           # S402: Requirements prioritization
│   ├── s4-core/               # S403: Core requirements extraction
│   ├── s4-user-stories/       # S405: User story writing
│   ├── s4-prototype/          # S406: Prototype design
│   ├── s5-vision/             # S5-A01: Architecture vision definition
│   ├── s5-views/              # S5-A02: Architecture view design
│   ├── s5-data/               # S5-A03: Data architecture design
│   ├── s5-interface/          # S5-A04: Interface architecture design
│   ├── s5-deployment/         # S5-A05: Deployment architecture design
│   ├── s5-validation/         # S5-A06: Architecture validation and review
│   ├── s6-module/             # S6-A01: Module detailed design
│   ├── s6-database/           # S6-A02: Database detailed design
│   ├── s6-uiux/               # S6-A03: UI/UX design
│   ├── s6-test-strategy/      # S6-A04: Test strategy design
│   └── cm-impact-analysis/    # CM-001: Change impact analysis
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
| S1 | S101 | s1-competitor/ | Competitor analysis |
| S1 | S102 | s1-market-analysis/ | Market pain point validation |
| S2 | S201 | s2-boundary/ | Requirement boundary definition |
| S2 | S202 | s2-explicit/ | Explicit requirements collection |
| S2 | S203 | s2-implicit/ | Implicit requirements analysis |
| S2 | S204 | s2-validation/ | Requirements validation |
| S3 | S301 | s3-feasibility/ | Technical feasibility analysis |
| S3 | S302 | s3-selection/ | Technology selection |
| S3 | S303 | s3-nfr/ | Non-functional requirements definition |
| S3 | S304 | s3-risk/ | Risk identification |
| S4 | S401 | s4-classify/ | Requirements classification |
| S4 | S402 | s4-priority/ | Requirements prioritization |
| S4 | S403 | s4-core/ | Core requirements extraction |
| S4 | S405 | s4-user-stories/ | User story writing |
| S4 | S406 | s4-prototype/ | Prototype design |
| S5 | S5-A01 | s5-vision/ | Architecture vision definition |
| S5 | S5-A02 | s5-views/ | Architecture view design (4+1 views) |
| S5 | S5-A03 | s5-data/ | Data architecture design |
| S5 | S5-A04 | s5-interface/ | Interface architecture design |
| S5 | S5-A05 | s5-deployment/ | Deployment architecture design |
| S5 | S5-A06 | s5-validation/ | Architecture validation and review |
| S6 | S6-A01 | s6-module/ | Module detailed design |
| S6 | S6-A02 | s6-database/ | Database detailed design |
| S6 | S6-A03 | s6-uiux/ | UI/UX design |
| S6 | S6-A04 | s6-test-strategy/ | Test strategy design |
| CM | CM-001 | cm-impact-analysis/ | Change impact analysis |

**Total**: 27 Skills (26 workflow Skills + 1 change management Skill)

## Execution Modes

The system automatically selects execution mode based on information completeness score (0-100):

| Mode | Threshold | Description | Skipped Skills |
|------|-----------|-------------|----------------|
| Normal | Score < 90 | Full 26-skill execution with deep analysis | None |
| Lightweight | Score ≥ 90 | Fast execution with essential skills only | S101, S102, S203, S406 |

## Key Files to Reference

- **WORKFLOW.md**: Complete workflow documentation including user review process, change management, and prototype design
- **agents/coordinator-requirements.md**: Requirements analysis agent (S0-S4)
- **agents/coordinator-architecture.md**: Architecture design agent (S5)
- **agents/coordinator-detailed-design.md**: Detailed design agent (S6)
- **skills/s0-plan/SKILL.md**: Entry point skill with scoring methodology
- **srs.md**: Full system requirements specification

## Output Artifact Paths

All outputs are stored in `artifacts/`:

```
artifacts/
├── plans/{PlanID}.md              # Plan definition
├── plans/{PlanID}/todo-list.md    # Task tracking (single source of truth)
└── stages/{s0-s6}/                # Skill outputs by stage
```

## Product ID Format

- Plan ID: `P{6 digits}` (e.g., P000001)
- Skill Output ID: `{PlanID}-S{Stage}-{SkillID}-{seq}` (e.g., P000001-S0-S001-001, P000001-S1-S101-001)

## Skill Definition Standards

Each Skill follows a consistent 6-section structure with **progressive disclosure** design:

### File Structure

```
skills/s{stage}-{name}/
├── SKILL.md                    # Main skill file (~300 lines)
│   └── YAML frontmatter        # name, description, version
├── template.md                 # Output template
└── references/                 # Detailed content (loaded on demand)
    ├── execution-details.md    # Detailed step descriptions
    ├── examples.md             # Demo examples
    ├── quality-standard.md     # ISO/IEC 25010 quality standard (copied from templates/)
    ├── error-code-standard.md  # Unified error code standard (copied from templates/)
    ├── execution-flow-standard.md  # Execution flow standard (copied from templates/)
    ├── artifact-specifications.md  # Artifact specifications (copied from templates/)
    └── user-interaction/       # User interaction templates (copied from templates/)
        ├── clarification-template.md
        ├── information-collection-template.md
        └── option-selection-template.md
```

### YAML Frontmatter

Each SKILL.md starts with YAML frontmatter for AI IDE auto-discovery:

```yaml
---
name: S101 需求边界界定
description: This skill should be used when the user asks to "define requirement boundaries",
  "clarify product scope", "identify target users", or "establish project boundaries".
  It provides 5-dimensional boundary analysis.
version: 3.2.0
---
```

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
- Brief step summary (table format)
- **References**: Detailed steps in `references/execution-details.md`
- **References**: Demo examples in `references/examples.md`

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

All Skills use standardized interaction templates (now copied to each Skill's `references/user-interaction/` directory):
- **Clarification**: `references/user-interaction/clarification-template.md`
- **Information Collection**: `references/user-interaction/information-collection-template.md`
- **Option Selection**: `references/user-interaction/option-selection-template.md`

### Quality Standards Reference

All Skills follow the quality assessment framework (now copied to each Skill's `references/` directory):
- **Quality Standard**: `references/quality-standard.md`
- **Error Code Standard**: `references/error-code-standard.md`
- **Execution Flow Standard**: `references/execution-flow-standard.md`
- **Artifact Specifications**: `references/artifact-specifications.md`

## Key Rules (from .trae/rules/swf-rule.md)

1. This is workflow definition, not code development
2. Skills are designed for AI IDEs (Claude Code, Codex, Trae)
3. All document outputs must be Markdown format
4. Documents cannot contain any code
5. Flowcharts must use Mermaid syntax
6. Reference: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
