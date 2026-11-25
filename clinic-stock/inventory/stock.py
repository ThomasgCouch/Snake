"""Functions for loading and analysing a vet clinic's medicine stock."""

import csv
from datetime import date


def load_stock(path):
    """Read the stock CSV and return a list of dicts.

    'quantity' must be an int and 'expiry' must be a datetime.date, e.g.
    {"name": "Flea Drops", "category": "parasite", "quantity": 24,
     "expiry": date(2027, 3, 1)}
    """
    items = []
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            row["quantity"] = int(row["quantity"])
            row["expiry"] = date.fromisoformat(row["expiry"])
            items.append(row)
    return items


def total_units(items):
    """Return the total quantity across all items."""
    total = 0
    for item in items:
        total += item["quantity"]
    return total


def units_by_category(items):
    """Return a dict of category -> total quantity in that category."""
    totals = {}
    for item in items:
        category = item["category"]
        if category in totals:
            totals[category] += item["quantity"]
        else:
            totals[category] = item["quantity"]
    return totals


def find_item(items, name):
    """Return the item with this name, ignoring upper/lower case.

    Return None if there is no item with that name.
    """
    for item in items:
        if item["name"].lower() == name.lower():
            return item
    return None


def expired_items(items, today):
    """Return a list of items whose expiry date is BEFORE today.

    An item expiring today is still OK to use, so it is not expired.
    """
    expired = []
    for item in items:
        if item["expiry"] < today:
            expired.append(item)
    return expired


def add_item(item, items=[]):
    """Add an item to a list and return the list.

    If no list is given, start a new empty one each time.
    """
    items.append(item)
    return items


def low_stock(items, threshold=10):
    """Return the NAMES of items with quantity below the threshold,
    sorted from the lowest quantity to the highest.

    e.g. ["Ear Cleaner", "Pain Relief", "Tick Collar"]
    """
    raise NotImplementedError("TODO: implement low_stock")
