"""
Non-Temporal stub orchestrator for local testing.

Real orchestration (Temporal) runs in the separate backend repo and interacts
with this repo via GitHub API (issues, comments, PRs).
"""
from __future__ import annotations
from src.workflows.worker import simulate_code_check


def propose_and_validate_change(plan_text: str, candidate_code: str) -> dict:
    """Return a minimal 'decision' that would stand in for an AI plan + self-check."""
    decision = {
        "plan_summary": plan_text.strip()[:200],
        "passes_basic_check": simulate_code_check(candidate_code),
    }
    return decision
