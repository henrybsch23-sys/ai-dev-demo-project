# AI-Dev Demo Project

This repository is a **demo playground** for the Kolomolo Hackathon AI Developer Assistant.  
The AI agent will treat this project like a real codebase: picking up issues, planning solutions, and opening pull requests.

---

## How It Works
1. A developer (human) creates a GitHub Issue and labels it **AI-Dev**.  
2. The AI workflow (running in the separate Temporal worker repo) detects the issue.  
3. The AI posts a **plan** as a comment.  
4. A human applies the label **plan-approved** (or rejects).  
5. The AI pushes code changes in a new branch and opens a Pull Request.  
6. The team reviews and merges the PR.

---

## Labels
- `AI-Dev` → Marks issues for the AI agent.  
- `needs-approval` → (Optional) Issue waiting for human approval.  
- `plan-approved` → Human approved AI’s proposed plan.  

---

## Issue Template
Use the template under `.github/ISSUE_TEMPLATE/ai-dev.md` to create consistent tasks.  
Example fields:
- **Task** – What needs to be implemented  
- **Acceptance Criteria** – What defines “done”

---

## Example Issue
1. Create an Issue titled **"Add BMI calculator function"**.  
   - Add label `AI-Dev`.  
   - Example comment:  
     ```
     AI Plan:
     - Create bmi.py with calculate_bmi(weight_kg, height_m)
     - Add simple unit tests
     - Commit via branch feature/bmi and open PR
     ```
2. Wait for the AI Assistant to comment back with a plan.  
3. Approve the plan with the label `plan-approved`.  
4. The AI will generate code and open a Pull Request. 
---

## Notes
- This repo is **not** the Temporal server; it’s only the **target app**.  
- The AI agent will create files, modify code, and open PRs here.  
- A small starter file `app.py` is included so the AI has something to extend.

---

## License
MIT
