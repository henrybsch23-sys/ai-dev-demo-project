from __future__ import annotations
from fastapi import FastAPI
from pydantic import BaseModel, Field
from pathlib import Path
import json
from datetime import datetime

from evaluator.apply_patch import apply_unified_diff
from evaluator.run_tests import run_pytests
from evaluator.score import score_result

app = FastAPI(title="AI-Dev Sandbox Adapter", version="0.1.0")

ART = Path("artifacts")
ART.mkdir(parents=True, exist_ok=True)

SCENARIOS = Path("scenarios")  # optional: where your issue fixtures can live
KNOWLEDGE = Path("knowledge/CLAUDE.md")


class IssueSpec(BaseModel):
    id: str = Field(..., description="Scenario/issue id, e.g. S-001")
    title: str
    body: str | None = None
    acceptance: list[str] = []
    repoFixture: str | None = None


class PlanIn(BaseModel):
    issue: IssueSpec
    knowledge: str | None = None  # raw contents or will be read from CLAUDE.md if None


class PatchIn(BaseModel):
    issueId: str
    patch: str  # unified diff
    notes: str | None = None


@app.get("/health")
def health():
    return {"status": "ok", "ts": datetime.utcnow().isoformat()}


@app.post("/v1/plan")
def plan(payload: PlanIn):
    """
    Create a lightweight plan artifact for a given issue.
    This endpoint is fast (<~100ms) to satisfy webhook→workflow initiation SLA.
    """
    issue = payload.issue
    art_dir = ART / issue.id
    art_dir.mkdir(parents=True, exist_ok=True)

    knowledge = payload.knowledge
    if knowledge is None and KNOWLEDGE.exists():
        knowledge = KNOWLEDGE.read_text(encoding="utf-8")

    plan_lines = [
        f"# Plan for {issue.id}: {issue.title}",
        "",
        "## Understanding",
        issue.body or "(no additional body provided)",
        "",
        "## Acceptance Criteria",
        *[f"- {item}" for item in (issue.acceptance or ["(none provided)"])],
        "",
        "## Proposed Changes",
        "- Modify API or service to satisfy the criteria.",
        "- Add/adjust tests under `src/tests` to lock behavior.",
        "",
        "## Knowledge / Conventions",
        (knowledge or "(none)"),
        "",
    ]
    plan_text = "\n".join(plan_lines)
    plan_path = art_dir / "plan.md"
    plan_path.write_text(plan_text, encoding="utf-8")

    return {"planUrl": str(plan_path), "approved": False}


@app.post("/v1/patch")
def patch(payload: PatchIn):
    """
    Apply a unified diff, run tests, compute score, and emit an artifact.
    """
    issue_id = payload.issueId
    art_dir = ART / issue_id
    art_dir.mkdir(parents=True, exist_ok=True)

    # Save patch for provenance
    patch_path = art_dir / "diff.patch"
    patch_path.write_text(payload.patch, encoding="utf-8")

    # Apply patch
    applied = apply_unified_diff(payload.patch, repo_root=".")
    if not applied["ok"]:
        report = {
            "stage": "apply",
            "ok": False,
            "message": applied["message"],
            "score": 0.0,
        }
        report_path = art_dir / "test-report.json"
        report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
        return {
            "tests": {"passed": False},
            "score": 0.0,
            "reportUrl": str(report_path),
            "error": applied["message"],
        }

    # Run tests
    junit_path = str(art_dir / "junit.xml")
    test_result = run_pytests(repo_root=".", junitxml_path=junit_path, quiet=True)
    score = score_result(test_result)

    # Persist report
    report = dict(test_result)
    report["score"] = score
    report_path = art_dir / "test-report.json"
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    return {
        "tests": {"passed": test_result["passed"]},
        "score": score,
        "reportUrl": str(report_path),
    }
