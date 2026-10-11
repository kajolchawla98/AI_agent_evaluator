#!/usr/bin/env python3
"""
AI PM Spec & Eval Reviewer — deterministic v1 checklist.

Usage:
    python review.py path/to/spec.md
"""

from pathlib import Path
import json
import re
import sys

AMBIGUOUS = [
    "fast", "accurate", "relevant", "intelligent", "personalized",
    "seamless", "appropriate", "high quality", "automatically",
    "as needed", "easy to use", "robust", "safe"
]

SECTION_HINTS = {
    "problem": ["problem", "user", "goal", "objective"],
    "inputs": ["input", "data", "context"],
    "outputs": ["output", "response", "result"],
    "acceptance": ["acceptance", "success criteria", "definition of done"],
    "negative": ["must not", "should not", "not do", "prohibited"],
    "evals": ["eval", "evaluation", "test case", "test plan"],
    "agent": ["agent", "tool", "autonom", "human", "escalat", "approval"],
}

def has_any(text, terms):
    t = text.lower()
    return any(term in t for term in terms)

def score_spec(text):
    checks = {
        "problem": has_any(text, SECTION_HINTS["problem"]),
        "inputs_outputs": has_any(text, SECTION_HINTS["inputs"]) and has_any(text, SECTION_HINTS["outputs"]),
        "acceptance": has_any(text, SECTION_HINTS["acceptance"]),
        "negative_criteria": has_any(text, SECTION_HINTS["negative"]),
        "evals": has_any(text, SECTION_HINTS["evals"]),
        "agent_boundaries": has_any(text, SECTION_HINTS["agent"]),
    }

    ambiguous_hits = sorted(set(
        term for term in AMBIGUOUS
        if re.search(r"\b" + re.escape(term) + r"\b", text, flags=re.I)
    ))

    weights = {
        "problem": 15,
        "inputs_outputs": 20,
        "acceptance": 20,
        "evals": 20,
        "negative_criteria": 15,
        "agent_boundaries": 10,
    }
    score = sum(weights[k] for k, ok in checks.items() if ok)

    findings = []
    if ambiguous_hits:
        findings.append({
            "finding": "Ambiguous language detected",
            "evidence": ", ".join(ambiguous_hits),
            "recommendation": "Replace vague terms with observable behavior, examples, thresholds, or pass/fail conditions."
        })
    if not checks["acceptance"]:
        findings.append({
            "finding": "Acceptance criteria are missing or not clearly labeled",
            "evidence": "No acceptance/success-criteria section detected.",
            "recommendation": "Define observable pass/fail criteria for the core behaviors."
        })
    if not checks["negative_criteria"]:
        findings.append({
            "finding": "Negative acceptance criteria are missing",
            "evidence": "No explicit must-not/should-not behavior detected.",
            "recommendation": "Specify important failure modes and prohibited outputs/actions."
        })
    if not checks["evals"]:
        findings.append({
            "finding": "AI evaluation plan is missing or unclear",
            "evidence": "No eval/evaluation/test-plan language detected.",
            "recommendation": "Add representative, edge, adversarial, and failure-mode test cases."
        })
    if not checks["agent_boundaries"]:
        findings.append({
            "finding": "Agent autonomy / human escalation is unclear",
            "evidence": "No clear tool, autonomy, approval, or escalation behavior detected.",
            "recommendation": "Define allowed actions and when the agent must ask for human confirmation."
        })

    return {
        "spec_completeness_diagnostic": score,
        "checks": checks,
        "ambiguous_terms": ambiguous_hits,
        "findings": findings,
        "note": "This is a deterministic checklist, not a model-quality or production-readiness score."
    }

def main():
    if len(sys.argv) != 2:
        print("Usage: python review.py path/to/spec.md")
        raise SystemExit(2)

    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8")
    result = score_spec(text)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
