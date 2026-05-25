# CODEX-EVOLVE.md — Self-Evolution Protocol for Codex

## Purpose

This file records project-local learning for Codex. Each meaningful task should improve the next session.

## 1. Pre-Task: Load Context

Before writing code:

1. Read parent/project `AGENTS.md`.
2. Read project `CONTEXT.md` if it exists.
3. Read this file's `## 5. Evolution Log`.
4. Identify which prior rule or skill applies.

## 2. Execution: The 6-Layer Harness

### Layer 1 — Context Governance
- Load only context needed for the task.
- Prefer project vocabulary from `CONTEXT.md`.

### Layer 2 — Tool System
- Prefer local scripts and existing project patterns.
- Use global skills from `/Users/a1/.codex/skills/` when triggered.

### Layer 3 — Execution Orchestration
- Step 0: environment/preflight check.
- Build in small verified increments.
- Do not generate large scripts before validating the path.

### Layer 4 — Memory & State
- Persist durable learning in project files, not only chat.
- Keep project-specific learnings in this file.

### Layer 5 — Evaluation & Observation
- Run the code or command.
- Read the output.
- Verify before stacking the next step.

### Layer 6 — Constraints & Recovery
- Respect AGENTS guardrails.
- If stuck for more than 2 attempts on the same error, step back and rethink.

## 3. Post-Task: Reflect & Write Back

Append to `## 5. Evolution Log`:

```markdown
### EVOL-[NNN] | [Date] | [One-line summary]
- Task:
- What worked:
- What failed:
- Root cause:
- New rule:
- Skill upgrade:
```

## 4. Internalized Rules

### General
- Read `CONTEXT.md` and `CODEX-EVOLVE.md` before complex work.
- Keep versions side by side; never overwrite without confirmation.
- Test batch/risky operations in a sandbox first.

### From Global Skill Design
- Skill descriptions must include precise trigger conditions.
- Keep `SKILL.md` short; move deep references and templates into adjacent files.
- Debugging starts with a deterministic pass/fail feedback loop.
- Tests should verify observable behavior through public interfaces.
- Split work into vertical slices that are independently verifiable.

### Production
- Use `preflight-benchmark` before batch generation, long rendering, or client-facing production.
- Use `ai-video-production` for AI video workflows.

## 5. Evolution Log

### EVOL-000 | System Init | Project Bootstrap
- Task: Initial project evolution file created from template
- What worked: Project now has a local learning loop
- What failed: N/A
- Root cause: N/A
- New rule: Keep project-specific learnings here
- Skill upgrade: N/A

### EVOL-001 | 2026-05-03 | Mobile-first portfolio HTML checks
- Task: Create a Daniel Li portfolio page based on a reference HTML and Canva portfolio content.
- What worked: Extracted source portfolio copy from Canva HTML, created a side-by-side v1 HTML file, and verified desktop plus mobile screenshots.
- What failed: Chrome headless CLI uses a 500px minimum layout viewport for simple screenshots, which made the first mobile screenshot misleading.
- Root cause: The screenshot image width was 390px, but CSS media queries were being evaluated against a 500px viewport.
- New rule: For mobile validation, use DevTools device metrics or another true mobile viewport check, and verify `scrollWidth === innerWidth`.
- Skill upgrade: For frontend pages, check mobile overflow before finalizing.

### EVOL-002 | 2026-05-03 | Portfolio MVP rebuilt from prompt
- Task: Rebuild the portfolio MVP as a deploy-ready single-file `index.html` from the provided Codex prompt.
- What worked: Used the prompt's exact section order, design tokens, copy direction, system diagram, agent stack, credentials, and static deployment shape.
- What failed: The first 768px pass inherited full mobile single-column rules, so tablet did not match the requested two-column layout.
- Root cause: A single `max-width: 768px` breakpoint handled both nav simplification and mobile layout.
- New rule: Separate nav-collapse breakpoints from content-layout breakpoints; use true mobile layout below 768px only.
- Skill upgrade: For responsive work, verify both `390px` mobile and `768px` tablet grid columns, not just overflow.

### EVOL-003 | 2026-05-03 | Portfolio link loop over embedded autoplay
- Task: Add looping portfolio work to the hero section.
- What worked: Replaced the placeholder demo card with a lightweight auto-rotating portfolio link carousel using YouTube thumbnails, captions, roles, dots, and outbound links.
- What failed: Direct YouTube iframe autoplay showed an embed/configuration error in local file testing.
- Root cause: External video embeds can be blocked or unreliable under `file://` and browser autoplay/embed restrictions.
- New rule: Use thumbnail/link carousel for static MVP reliability; ask for direct `.mp4`/`.webm` or a confirmed embeddable video host before implementing true inline autoplay.
- Skill upgrade: Verify embedded media visually, not only by checking element existence.
