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
│   ├── skill0-plan/           # S0: Plan definition
│   ├── s1-requirements/       # S1: Requirement boundary & collection (4 skills)
│   ├── s2-market/             # S2: Market validation (2 skills)
│   ├── s3-technical/          # S3: Technical feasibility (3 skills)
│   └── s4-integration/        # S4: Integration & core extraction (4 skills)
├── templates/                 # Output templates
├── .trae/                     # Progress tracking
│   ├── rules/                 # Project rules
│   └── progress/              # Daily progress logs
├── WORKFLOW.md                # Main workflow documentation
└── srs.md                     # System requirements specification
```

### Skill Stages

| Stage | Skills | Purpose |
|-------|--------|---------|
| S0 | Skill0 | Plan definition, ID generation, completeness scoring |
| S1 | Skill1-4 | Requirement boundary, explicit/implicit requirements, validation |
| S2 | Skill9-10 | Competitor analysis, market pain point validation |
| S3 | Skill7,11-12 | Risk identification, technical feasibility, tech selection |
| S4 | Skill5-6,8,15 | Classification, prioritization, core extraction, prototype |

## Execution Modes

The system automatically selects execution mode based on information completeness score (0-100):

| Mode | Threshold | Description |
|------|-----------|-------------|
| Normal | Score < 90 | Full 14-skill execution with deep analysis |
| Lightweight | Score ≥ 90 | Skips Skill3, Skill9, Skill10, Skill15 for faster execution |

## Key Files to Reference

- **WORKFLOW.md**: Complete workflow documentation including user review process, change management, and prototype design
- **agents/coordinator.md**: Main agent execution flow, state management, and Todo-List rules
- **skills/skill0-plan/SKILL.md**: Entry point skill with scoring methodology
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
- Skill Output ID: `{PlanID}-{Stage}-{SkillID}-{seq}` (e.g., P000001-S1-S01-001)

## Skill Definition Standards

Each Skill follows a consistent structure:
1. **Pre-check**: Validate dependencies exist
2. **User interaction**: Clarify ambiguous content (if needed)
3. **Core execution**: Generate output using templates
4. **Post-check**: Validate output format
5. **User review**: Confirm/modify/new ideas

## Key Rules (from .trae/rules/swf-rule.md)

1. This is workflow definition, not code development
2. Skills are designed for AI IDEs (Claude Code, Codex, Trae)
3. All document outputs must be Markdown format
4. Documents cannot contain any code
5. Flowcharts must use Mermaid syntax
6. Reference: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
