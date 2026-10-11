# AI PM Spec & Eval Reviewer

A small, reusable Agent Skill for Product Managers building AI features.

It reviews an AI product spec for:

- ambiguous requirements
- testability and acceptance criteria
- AI eval coverage
- negative acceptance criteria
- hallucination and prompt-injection risks
- agent autonomy boundaries
- human-in-the-loop decisions
- measurable success criteria

## Why I built this

AI can accelerate prototyping and implementation. That makes the quality of the product contract even more important.

This skill explores a practical PM workflow:

**Spec → Acceptance Criteria → Evals → Agent Boundaries → Product Quality**

It is intentionally lightweight: the skill provides the review method, while the bundled Python script gives a deterministic first-pass checklist.

## Repository structure

```text
.agents/
└── skills/
    └── ai-pm-spec-eval-reviewer/
        ├── SKILL.md
        ├── scripts/
        │   └── review.py
        └── examples/
            ├── restaurant-recommendation.md
            ├── support-agent.md
            └── fintech-research-agent.md
```

## Use as an Agent Skill

The skill follows the `SKILL.md` Agent Skills format. Copy the folder into a compatible agent's skills directory, or keep it in a project under:

```text
.agents/skills/ai-pm-spec-eval-reviewer/
```

You can also adapt the same instructions for Claude Code, Claude.ai, or another Agent Skills-compatible client.

## Run the deterministic reviewer

```bash
python .agents/skills/ai-pm-spec-eval-reviewer/scripts/review.py examples/restaurant-recommendation.md
```

The script is deliberately conservative. It does **not** pretend to measure model quality. It checks whether a spec contains observable product requirements and common AI-risk coverage.

## Example output

A review can surface findings such as:

- “Personalized recommendations” has no measurable definition.
- No negative acceptance criterion prevents fabricated restaurant information.
- No behavior is specified for missing user preferences.
- Agent escalation behavior is undefined.
- Evaluation coverage does not include adversarial or unsupported-output cases.

## Important

This is a v1 learning project, not a production-grade AI evaluation framework.

The score is a **spec completeness diagnostic**, not an accuracy score for an AI model.

