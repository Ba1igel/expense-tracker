import csv
import json
import os

from .models import Expense

DATA_DIR = os.environ.get("EXPENSES_DIR", os.path.join(os.path.expanduser("~"), ".expenses"))
DATA_FILE = "expenses.json"


def _path():
    return os.path.join(DATA_DIR, DATA_FILE)


def load_expenses():
    if not os.path.exists(_path()):
        return []
    with open(_path()) as f:
        raw = json.load(f)
    return [Expense.from_dict(r) for r in raw]


def save_expenses(expenses):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(_path(), "w") as f:
        json.dump([e.to_dict() for e in expenses], f, indent=2)


def add_expense(expense):
    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    return expense


def _safe_export_path(filename):
    """Only plain file names are allowed, the file always goes into DATA_DIR."""
    if not filename or filename != os.path.basename(filename) or filename in (".", ".."):
        raise ValueError(f"export file must be a plain file name, got {filename!r}")
    base = os.path.realpath(DATA_DIR)
    out = os.path.realpath(os.path.join(base, filename))
    if os.path.dirname(out) != base:
        raise ValueError(f"export path {out!r} is outside the data directory")
    return out


def export_csv(expenses, filename):
    out = _safe_export_path(filename)
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "date", "category", "amount", "note"])
        for e in expenses:
            w.writerow([e.id, e.date, e.category, e.amount, e.note])
    return out
