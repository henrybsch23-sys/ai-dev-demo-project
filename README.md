# AI-Dev Demo Project

FastAPI-based demo API and sandbox adapter for experimenting with AI developer workflows.

## 📦 Project Structure

```
.
├─ app/                     # Main application package
│  ├─ api/                  # FastAPI endpoints
│  ├─ services/             # Pure functions for calculations & recommendations
│  └─ tests/                # Unit & integration tests (pytest)
│
├─ adapters/                # Interfaces for Temporal team / AI workers
│  ├─ http_server.py        # FastAPI service with /v1/plan and /v1/patch
│  └─ cli.py                # Command-line adapter
│
├─ evaluator/               # Helpers for applying patches & running tests
│  ├─ apply_patch.py
│  ├─ run_tests.py
│  ├─ score.py
│
├─ scenarios/               # JSON issue/task fixtures (S-001.json, …)
├─ knowledge/CLAUDE.md      # Team conventions / house rules
├─ artifacts/               # AI-generated plans, diffs, test reports
├─ requirements.txt         # Python dependencies
├─ .github/workflows/ci.yml # GitHub Actions CI (pytest)
└─ README.md
```

## 🚀 Getting Started

### 1. Setup environment
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run API (main demo app)
```bash
uvicorn app.api.main:app --reload --port 8000
```
- Swagger UI: http://127.0.0.1:8000/docs  
- Health check: http://127.0.0.1:8000/health

### 3. Run Adapter (sandbox API)
```bash
uvicorn adapters.http_server:app --reload --port 8080
```
- Health check: http://127.0.0.1:8080/health  
- Endpoints: `/v1/plan`, `/v1/patch`

### 4. Run Tests
```bash
pytest -q
```

## 🧪 Example Usage

### Plan creation (CLI)
```bash
python -m adapters.cli plan --issue-json scenarios/S-001.json
```

### Apply patch + score (CLI)
```bash
python -m adapters.cli apply --issue-id S-001 --patch diff.patch
```

### API call
```bash
curl "http://127.0.0.1:8000/tdee?bmr_val=1600&activity=sedentary"
```

## 📂 Scenarios

Sample issue/task specs live in `scenarios/`:
```json
{
  "id": "S-001",
  "title": "Reject unknown activity in /tdee with HTTP 400",
  "acceptance": [
    "GET /tdee?bmr_val=1600&activity=super-saiyan returns 400",
    "GET /tdee?bmr_val=1600&activity=sedentary returns 200 with a number"
  ]
}
```

## ⚙️ CI/CD

- GitHub Actions (`.github/workflows/ci.yml`) runs pytest on each push/PR
- JUnit reports and artifacts saved under `artifacts/`

## 📜 License

MIT – use freely for hackathons, demos, and experiments.
