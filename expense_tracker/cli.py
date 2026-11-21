import argparse
import sys

from tabulate import tabulate

from . import report, storage
from .models import Expense


def cmd_add(args):
    e = Expense(amount=float(args.amount), category=args.category.lower(), note=args.note or "", date=args.date)
    storage.add_expense(e)
    print(f"Added {e.id}: {e.amount:.0f} KZT ({e.category})")


def cmd_list(args):
    expenses = storage.load_expenses()
    if args.month:
        y, m = args.month.split("-")
        expenses = report.filter_by_month(expenses, int(y), int(m))
    rows = [[e.id, e.date, e.category, f"{e.amount:.0f}", e.note] for e in expenses]
    print(tabulate(rows, headers=["id", "date", "category", "amount", "note"]))


def cmd_summary(args):
    expenses = storage.load_expenses()
    y, m = args.month.split("-")
    month_exp = report.filter_by_month(expenses, int(y), int(m))
    print(f"Summary for {args.month}")
    for cat, amount in sorted(report.by_category(month_exp).items()):
        print(f"  {report.category_label(cat):<18} {amount:>10.0f} KZT")
    print(f"  {'TOTAL':<18} {report.total(month_exp):>10.0f} KZT")
    for w in report.limit_warnings(month_exp):
        print("  WARNING: " + w)


def cmd_export(args):
    expenses = storage.load_expenses()
    try:
        path = storage.export_csv(expenses, args.file)
    except ValueError as err:
        print(f"Error: {err}", file=sys.stderr)
        return 2
    print(f"Exported {len(expenses)} expenses to {path}")
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(prog="expenses", description="Personal expense tracker (KZT)")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("add")
    a.add_argument("amount")
    a.add_argument("category")
    a.add_argument("--note")
    a.add_argument("--date", default="")
    a.set_defaults(func=cmd_add)

    ls = sub.add_parser("list")
    ls.add_argument("--month")
    ls.set_defaults(func=cmd_list)

    s = sub.add_parser("summary")
    s.add_argument("month", help="YYYY-MM")
    s.set_defaults(func=cmd_summary)

    ex = sub.add_parser("export")
    ex.add_argument("file")
    ex.set_defaults(func=cmd_export)

    args = p.parse_args(argv)
    return args.func(args) or 0


if __name__ == "__main__":
    sys.exit(main())
