"""Tests for inventory.stock. Do not change these."""

from datetime import date

import pytest

from inventory.stock import (
    add_item,
    expired_items,
    find_item,
    load_stock,
    low_stock,
    total_units,
    units_by_category,
)

DATA = "data/stock.csv"


@pytest.fixture
def items():
    return load_stock(DATA)


def test_load_converts_types(items):
    assert len(items) == 6
    assert items[0] == {
        "name": "Flea Drops",
        "category": "parasite",
        "quantity": 24,
        "expiry": date(2027, 3, 1),
    }


def test_total_units(items):
    assert total_units(items) == 92


def test_total_units_empty():
    assert total_units([]) == 0


def test_units_by_category(items):
    assert units_by_category(items) == {"parasite": 72, "medicine": 17, "hygiene": 3}


def test_find_item_ignores_case(items):
    assert find_item(items, "pain relief")["quantity"] == 5


def test_find_item_missing_returns_none(items):
    assert find_item(items, "Unicorn Tonic") is None


def test_expired_items(items):
    expired = expired_items(items, date(2026, 11, 20))
    assert [i["name"] for i in expired] == ["Worming Tablets"]


def test_add_item_starts_fresh_each_time():
    first = add_item("a")
    second = add_item("b")
    assert first == ["a"]
    assert second == ["b"]


def test_low_stock(items):
    assert low_stock(items) == ["Ear Cleaner", "Pain Relief", "Tick Collar"]


def test_low_stock_custom_threshold(items):
    assert low_stock(items, threshold=5) == ["Ear Cleaner"]
