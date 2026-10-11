# Example Review Results

These are deterministic v1 checklist outputs from the bundled reviewer. They are intentionally presented as **spec completeness diagnostics**, not model-quality measurements.

## Example A — Restaurant recommendation
**Diagnostic:** 55/100

Key findings:
- Ambiguous: “relevant”, “personalized”, “fast”
- No negative acceptance criteria
- No explicit AI eval plan
- No defined behavior for failure/unsupported recommendations

**PM takeaway:** The feature intent is understandable, but the AI behavior is not yet testable enough to serve as an executable product contract.

## Example B — Customer support resolution agent
**Diagnostic:** 85/100

Key findings:
- “Accurate” and “helpful” are not operationally defined
- Human escalation exists but “complex issue” is undefined
- Eval coverage is too narrow and does not include adversarial/failure cases

**PM takeaway:** The product has a clearer contract, but the agent boundary and evaluation design need to become explicit.

## Example C — Market research agent
**Diagnostic:** 100/100

The checklist detects:
- problem
- inputs and outputs
- acceptance criteria
- negative criteria
- evals
- agent boundaries

**PM takeaway:** The presence of all sections does not prove the system works. It simply means the spec has a stronger basis for measurable testing.

