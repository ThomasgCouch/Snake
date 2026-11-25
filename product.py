sales = [
    {"product": "Collar", "amount": 120},
    {"product": "Lead", "amount": 45},
    {"product": "Collar", "amount": 80},
    {"product": "Shampoo", "amount": 200},
    {"product": "Lead", "amount": 30},
]


def total_sales(records):
    """Return the total of all the amounts."""
    total = 0
    for record in records:
        total += record["amount"]
    return total


def best_single_sale(records):
    """Return the record (the whole dict) with the biggest amount."""
    best = records[0]
    for record in records:
        if record["amount"] > best["amount"]:
            best = record
    return best


def totals_by_product(records):
    """Return a dict of product -> total amount, e.g. {"Collar": 200, ...}"""
    totals = {}

    for record in records:
        product = record["product"]
        amount = record["amount"]
        
        if product in totals:
            totals[product] += amount
        else:
            totals[product] = amount
    return totals
        
    

# These check your answers. If nothing prints except "All passed!", you got it.
assert total_sales(sales) == 475
assert best_single_sale(sales) == {"product": "Shampoo", "amount": 200}
assert totals_by_product(sales) == {"Collar": 200, "Lead": 75, "Shampoo": 200}
print("All passed!")