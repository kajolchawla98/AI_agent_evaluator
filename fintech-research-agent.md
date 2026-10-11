# Market Research Agent

## Problem
Help product managers summarize public market information and identify themes.

## Inputs
Approved public documents and research notes.

## Outputs
A concise summary with cited evidence and key themes.

## Acceptance criteria
- Every factual claim should be supported by source evidence.
- The agent must not invent citations.
- The agent must not make unsupported claims about companies or markets.

## Evals
Evaluate factual grounding, citation correctness, and unsupported claims.

## Agent
The agent may search approved sources and draft a report. It should ask for confirmation before sending the report externally.
