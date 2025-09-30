from __future__ import annotations
import argparse
import json
from pathlib import Path

from evaluator.apply_patch import apply_unified_diff
from evaluator.run_tests import run_pytests
from evaluator.score import score_result

ART = Path("artifacts")


def cmd_plan(args: argparse.Namespace) -> int:
    issue_path = Path(args.issue_json)
    issue = json.loads(issue_path.read_text(encoding="utf-8"))
    art_dir = ART / issue["id"]
    art_dir.mkdir(parents=True, exist_ok=True)

    knowledge_path = Path("knowledge/CLAUDE.md")
    knowledge = knowledge_path.read_text(encoding="utf-8") if knowledge_path.exists() else ""

    plan_text = f"""# Plan for {issue['id']}: {issue.get('title','(no-title)')}

## Understanding
{issue.get('body','(no body)')}

## Acceptance Criteria
""" + "\n".join(f"- {x}" for x in issue.get("acceptance", [])) + f"""

## Proposed Changes
- Update code and/or tests to satisfy criteria.

## Knowledge / Conventions
{knowledge or "(none)"}
"""
    plan_path = art_dir / "plan.md"
    plan_path.write_text(plan_text, encoding="utf-8")
    print(str(plan_path))
    return 0


def cmd_apply(args: argparse.Namespace) -> int:
    issue_id = args.issue_id
    patch_file = Path(args.patch)
    patch_text = patch_file.read_text(encoding="utf-8")
    art_dir = ART / issue_id
    art_dir.mkdir(parents=True, exist_ok=True)

    # Save patch for provenance
    (art_dir / "diff.patch").write_text(patch_text, encoding="utf-8")

    applied = apply_unified_diff(patch_text)
    if not applied["ok"]:
        print("Patch failed to apply:")
        print(applied["message"])
        return 2

    result = run_pytests(".")
    score = score_result(result)

    report = dict(result); report["score"] = score
    (art_dir / "test-report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps({"passed": result["passed"], "score": score, "report": str(art_dir / "test-report.json")}, indent=2))
    return 0 if result["passed"] else 1


def main():
    parser = argparse.ArgumentParser(prog="ai-dev-sandbox", description="CLI for planning and applying patches.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_plan = sub.add_parser("plan", help="Create a plan artifact from a scenario JSON")
    p_plan.add_argument("--issue-json", required=True, help="Path to scenarios/S-xxx.json")
    p_plan.set_defaults(func=cmd_plan)

    p_apply = sub.add_parser("apply", help="Apply a patch file and run tests")
    p_apply.add_argument("--issue-id", required=True, help="Scenario/issue id (e.g., S-001)")
    p_apply.add_argument("--patch", required=True, help="Path to a unified diff patch file")
    p_apply.set_defaults(func=cmd_apply)

    args = parser.parse_args()
    raise SystemExit(args.func(args))


if __name__ == "__main__":
    main()
