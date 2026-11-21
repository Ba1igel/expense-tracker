# AGENTS.md

Instructions for AI coding agents (Claude Code, Codex, Copilot agent, etc.) working in this repository.
Humans can read it too, it doubles as a short contributor guide.

## What this project is

A small personal CLI that records expenses in tenge (KZT) and prints monthly summaries
with per-category limit warnings. Single user, local only, no network, no database.
Data lives in a JSON file at `$EXPENSES_DIR/expenses.json` (default `~/.expenses/`).

## Architecture

| File | Responsibility |
|------|----------------|
| `expense_tracker/cli.py` | argparse commands (`add`, `list`, `summary`, `export`), printing only |
| `expense_tracker/report.py` | pure functions: month filter, totals, limit warnings |
| `expense_tracker/categories.py` | category rules table (label + monthly limit), add new categories here |
| `expense_tracker/storage.py` | JSON load/save and CSV export, the only module that touches the disk |
| `expense_tracker/models.py` | `Expense` dataclass |
| `tests/` | pytest tests, one file per module |

Keep business logic out of `cli.py`. New calculations go to `report.py` and get a test.

## Setup

```
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt -r requirements-dev.txt
```

Python 3.10+ is required.

## Safe commands (you may run these without asking)

```
python -m pytest -q              # all tests, must pass before you finish
ruff check .                     # lint, must be clean
mypy expense_tracker             # type check
python -m expense_tracker --help
EXPENSES_DIR=$(mktemp -d) python -m expense_tracker ...   # manual runs ONLY with a temp dir
git status / git diff / git log
```

Never run the CLI against the real `~/.expenses` directory. Always set `EXPENSES_DIR` to a temp folder.

## Coding conventions

- Python, 4 spaces, max line length 120, imports sorted (ruff `I` rules).
- Money is stored in whole tenge. Do not introduce new float arithmetic for amounts.
- Dates are ISO strings `YYYY-MM-DD`.
- Small functions, no new classes unless they remove real duplication.
- Keep the JSON file format backward compatible (old files must still load).

## Test expectations

- Every bug fix comes with a test that fails before the fix and passes after it.
- Tests must not touch the real home directory: use `tmp_path` + `monkeypatch` on `storage.DATA_DIR`.
- Do not delete or weaken existing tests to make a change pass. If a test looks wrong, stop and explain.

## Forbidden actions

- Do not add, commit or print secrets, tokens, `.env` files or real personal financial data.
- Do not add, remove or upgrade dependencies (`requirements*.txt`, `pyproject.toml`) without explicit approval in the task.
- No destructive commands: `rm -rf`, `git push --force`, `git reset --hard`, history rewrites, deleting data files.
- No deployments, no publishing to PyPI, no network calls from the code.
- Do not edit files outside this repository.
- Do not disable lint rules or tests to get a green run.

## Review gates

1. Work on a separate branch, never directly on `main`.
2. Before finishing: `python -m pytest -q` and `ruff check .` must pass; paste the output in the summary.
3. Summary must list changed files, why, and anything you could not verify.
4. A human reviews the diff and merges. Agents never merge their own changes.

## Acceptance criteria (must stay true after any change)

See `docs/acceptance-criteria.md`.
