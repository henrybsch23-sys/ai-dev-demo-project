# AI-Dev Demo Project

## Overview
This repository is a **playground** for the Kolomolo Hackathon.  
It is designed to simulate a natural software project where the **AI Developer Assistant** can:
- Pick up GitHub Issues labeled `AI-Dev`
- Propose a plan (as a comment)
- Generate code & open Pull Requests
- Wait for human-in-the-loop approval

The AI logic and Temporal backend run in a **separate server repo**.  
This repo is only for **demo issues, workflows, and simple features**.

---

## Project Structure
```
src/
├── api/              # FastAPI app (REST endpoints)
│   └── main.py
├── services/         # Business logic (calculations, recommendations)
│   ├── calculations.py
│   └── recommendations.py
├── workflows/        # Placeholder for orchestration/worker stubs
│   ├── worker.py
│   └── orchestrator.py
└── tests/            # Unit tests (pytest)
    ├── test_api.py
    └── test_calculator.py

docs/                 # Design notes and extra documentation
.github/              # Issue template + GitHub Actions workflows
```

---

## Quickstart (Local Development)
**Requirements**: Python 3.11+, pip, virtualenv (or uv).

Clone the repo:
```bash
git clone https://github.com/<your-org>/<your-repo>.git
cd <your-repo>
```

Create virtual environment & install deps:
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate    # Windows

pip install -r requirements.txt
```

Run tests:
```bash
pytest -q
```

Run API locally:
```bash
uvicorn src.api.main:app --reload
```

Then open: http://127.0.0.1:8000/docs

---

## Demo Flow (AI-Dev)
1. Create a GitHub **Issue** and label it `AI-Dev`.
2. The AI Assistant proposes a **plan** (as a comment).
3. Human approves the plan (add label `plan-approved`).
4. AI generates code and opens a **Pull Request**.
5. CI runs tests, then the team reviews & merges the PR.

---

## Labels
- `AI-Dev` → triggers the AI workflow.
- `needs-approval` → waiting for human review.
- `plan-approved` → human approved the plan.

---

## Notes
- This repo is **not the Temporal backend**. It’s just a target project for Issues/PRs.
- The AI Assistant connects here via **API keys** provided to the backend server.
- The goal is to demonstrate **Issue → Plan → PR → Merge**.
