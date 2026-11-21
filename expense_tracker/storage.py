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


def export_csv(expenses, filename):
    out = os.path.join(DATA_DIR, filename)
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "date", "category", "amount", "note"])
        for e in expenses:
            w.writerow([e.id, e.date, e.category, e.amount, e.note])
    return out
