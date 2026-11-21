import pytest

from expense_tracker import report
from expense_tracker.models import Expense


def make(amount, cat, d):
    return Expense(amount=amount, category=cat, note="", date=d)


def test_total():
    items = [make(1000, "food", "2026-03-01"), make(2500, "transport", "2026-03-02")]
    assert report.total(items) == 3500


def test_by_category():
    items = [make(1000, "food", "2026-03-01"), make(500, "food", "2026-03-05"), make(200, "transport", "2026-03-02")]
    assert report.by_category(items) == {"food": 1500, "transport": 200}


def test_filter_by_month():
    items = [make(1000, "food", "2026-03-01"), make(500, "food", "2026-04-05")]
    # NOTE: month is passed the same way the CLI does it
    result = report.filter_by_month(items, 2026, "03")
    assert len(result) == 1


def test_limit_warning_food():
    items = [make(70000, "food", "2026-03-01")]
    w = report.limit_warnings(items)
    assert len(w) == 1
    assert "Food" in w[0]


def test_no_warning_under_limit():
    items = [make(5000, "transport", "2026-03-01")]
    assert report.limit_warnings(items) == []


# characterization tests added before the category refactor (AC3)


@pytest.mark.parametrize(
    "cat,limit,label",
    [
        ("food", 60000, "Food & groceries"),
        ("transport", 15000, "Transport"),
        ("entertainment", 20000, "Entertainment"),
        ("utilities", 35000, "Utilities"),
        ("gifts", 10000, "Other"),
    ],
)
def test_limits_and_labels_unchanged(cat, limit, label):
    assert report.monthly_limit(cat) == limit
    assert report.category_label(cat) == label
    assert report.limit_warnings([make(limit, cat, "2026-03-01")]) == []
    over = report.limit_warnings([make(limit + 1, cat, "2026-03-01")])
    assert over == [f"{label}: {limit + 1} KZT is over the limit of {limit} KZT"]


# R-01 regression tests: the CLI passes year and month as ints (int("03") == 3)
def test_filter_by_month_with_int_month_like_cli():
    items = [make(3000, "food", "2026-03-04"), make(1500, "transport", "2026-03-10"), make(9000, "food", "2026-04-01")]
    result = report.filter_by_month(items, 2026, 3)
    assert [e.amount for e in result] == [3000, 1500]


def test_january_does_not_include_october_to_december():
    items = [make(4000, "food", "2026-01-15"), make(9000, "food", "2026-10-02"), make(100, "food", "2026-12-31")]
    result = report.filter_by_month(items, 2026, 1)
    assert [e.amount for e in result] == [4000]
