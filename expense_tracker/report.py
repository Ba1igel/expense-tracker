from collections import defaultdict

from .categories import rule_for


def filter_by_month(expenses, year, month):
    prefix = f"{year}-{month}"
    return [e for e in expenses if e.date.startswith(prefix)]


def total(expenses):
    return sum(e.amount for e in expenses)


def by_category(expenses):
    result = defaultdict(float)
    for e in expenses:
        result[e.category] += e.amount
    return dict(result)


def monthly_limit(category):
    return rule_for(category).monthly_limit


def category_label(category):
    return rule_for(category).label


def limit_warnings(expenses):
    warnings = []
    for cat, spent in by_category(expenses).items():
        rule = rule_for(cat)
        if rule.is_over_limit(spent):
            warnings.append(f"{rule.label}: {spent:.0f} KZT is over the limit of {rule.monthly_limit} KZT")
    return warnings
