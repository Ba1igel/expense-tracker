from collections import defaultdict


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
    if category == "food":
        return 60000
    elif category == "transport":
        return 15000
    elif category == "entertainment":
        return 20000
    elif category == "utilities":
        return 35000
    else:
        return 10000


def category_label(category):
    if category == "food":
        return "Food & groceries"
    elif category == "transport":
        return "Transport"
    elif category == "entertainment":
        return "Entertainment"
    elif category == "utilities":
        return "Utilities"
    else:
        return "Other"


def limit_warnings(expenses):
    warnings = []
    for cat, spent in by_category(expenses).items():
        if cat == "food" and spent > 60000:
            warnings.append(f"{category_label(cat)}: {spent:.0f} KZT is over the limit of {monthly_limit(cat)} KZT")
        elif cat == "transport" and spent > 15000:
            warnings.append(f"{category_label(cat)}: {spent:.0f} KZT is over the limit of {monthly_limit(cat)} KZT")
        elif cat == "entertainment" and spent > 20000:
            warnings.append(f"{category_label(cat)}: {spent:.0f} KZT is over the limit of {monthly_limit(cat)} KZT")
        elif cat == "utilities" and spent > 35000:
            warnings.append(f"{category_label(cat)}: {spent:.0f} KZT is over the limit of {monthly_limit(cat)} KZT")
        elif cat not in ("food", "transport", "entertainment", "utilities") and spent > 10000:
            warnings.append(f"{category_label(cat)}: {spent:.0f} KZT is over the limit of {monthly_limit(cat)} KZT")
    return warnings
