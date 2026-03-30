# AGENTS.md

This file provides guidance to Codex when working with the SWF repository.

## Purpose

SWF is a document-first requirements analysis workflow. The repository content is not application code; it is a reusable workflow definition for running software requirements analysis, architecture design, and detailed design.

## How Codex Should Interpret This Repository

- Treat `agents/*.md` as coordinator playbooks, not as executable platform-specific agent manifests.
- Treat `skills/*/SKILL.md` as the primary workflow definitions for each stage.
- Treat `references/` under each skill as on-demand detail. Load only the files needed for the current step.
- Treat YAML frontmatter in the agent files as legacy Claude metadata. Preserve it if useful, but do not depend on automatic agent triggering.

## Codex Execution Model

Codex should run SWF explicitly by reading the relevant coordinator file and then executing the referenced skills in order.

### Trigger Mapping

- User asks for requirement analysis:
  Load `agents/coordinator-requirements.md` and execute S0-S4.
- User asks for architecture design:
  Load `agents/coordinator-architecture.md` and execute S5.
- User asks for detailed design:
  Load `agents/coordinator-detailed-design.md` and execute S6.
- User asks for change impact analysis:
  Load `skills/cm-impact-analysis/SKILL.md`.

### Skill Loading Rules

1. Read the current coordinator file to determine the next skill.
2. Read that skill's `SKILL.md`.
3. Read only the referenced files needed for the current step.
4. Produce the artifact files defined by the skill.
5. Update the relevant `todo-list` file.
6. Ask the user for review in plain conversation.
7. Continue only after the user confirms or provides revisions.

## Interaction Rules

- Use normal Codex conversation for review checkpoints; there is no Claude-style automatic agent handoff.
- When a skill says "trigger next agent", Codex should instead load the next coordinator file itself.
- If artifact directories do not exist, create them before writing outputs.
- Keep all generated outputs in `artifacts/` using the paths defined by each skill.
- All workflow outputs should remain Markdown unless a skill explicitly requires another file type.

## Repository Constraints

- This repository defines workflows, not product source code.
- Generated outputs should be readable, structured documents.
- Mermaid should be used for diagrams when a diagram is required.
- Preserve the existing stage IDs, skill IDs, artifact naming rules, and roadmap layout.

## Recommended Starting Files

- `README.md`: overview and Codex usage entry point
- `WORKFLOW.md`: end-to-end workflow definition
- `agents/coordinator-requirements.md`: S0-S4 coordinator
- `agents/coordinator-architecture.md`: S5 coordinator
- `agents/coordinator-detailed-design.md`: S6 coordinator
- `skills/s0-plan/SKILL.md`: workflow entry skill

## Practical Note

This Codex adaptation keeps the original SWF content structure intact. The main difference is execution style:

- Claude Code: relies on platform-level agent and skill discovery
- Codex: reads the same files as explicit workflow instructions and executes them step by step
