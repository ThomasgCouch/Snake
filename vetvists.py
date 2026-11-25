import csv


def load_visits(path):
    """Read the CSV file and return a list of dicts.
    Each cost must be an int, not a string, e.g.
    {"pet": "Milo", "species": "cat", "vet": "Dr Shah", "cost": 45}"""
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        visits = []
        for row in reader:
            row["cost"] = int(row["cost"])
            visits.append(row)
    return visits   
 
def total_cost(visits):
    """Return the total cost of all visits."""
 
    cost = 0
    for visit in visits:
        cost += visit["cost"]
    return cost

def most_expensive(visits):
    """Return the visit (whole dict) with the highest cost."""
    expensive = visits[0]
    for visit in visits:
        if visit["cost"] > expensive["cost"]:
            expensive = visit
            return expensive 

def cost_by_vet(visits):
    """Return a dict of vet -> total cost, e.g. {"Dr Shah": 250, ...}"""
    vet_costs = {}
    for visit in visits:
           visit = visit["visits"]
           cost = cost["cost"]
           
           if visit in vet_costs:
               vet_costs[cost] += 1
           else:
               vet_costs[cost] = 1
    return visit
def visits_for_species(visits, species):
    """Return a list of only the visits for that species."""
    
    speciesvisit = []
    
    for visit in visits:
        if visits == visit["visit"]:
            speciesvisit.append(visit)
    return visit


def sorted_by_cost(visits):
    """Return a NEW list of visits sorted from cheapest to most expensive."""


visits = load_visits("visits.csv")

assert len(visits) == 6
assert visits[0] == {"pet": "Milo", "species": "cat", "vet": "Dr Shah", "cost": 45}
assert total_cost(visits) == 390
assert most_expensive(visits)["pet"] == "Max"
assert cost_by_vet(visits) == {"Dr Shah": 250, "Dr Jones": 140}
assert [v["pet"] for v in visits_for_species(visits, "cat")] == ["Milo", "Luna", "Nala"]
assert [v["pet"] for v in sorted_by_cost(visits)] == ["Coco", "Milo", "Nala", "Luna", "Bella", "Max"]
print("All passed!")
    