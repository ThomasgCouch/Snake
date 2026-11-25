sightings = [
    {"city": "London", "species": "Marsh tick", "count": 3},
    {"city": "Leeds", "species": "Tree-hole tick", "count": 1},
    {"city": "London", "species": "Passerine tick", "count": 5},
    {"city": "Bristol", "species": "Marsh tick", "count": 2},
    {"city": "Leeds", "species": "Marsh tick", "count": 4},
    {"city": "Bristol", "species": "Fox/badger tick", "count": 1},
]


def total_ticks(records):
    """Return the total of all the counts."""
    ticks = 0 
    for record in records:
        ticks += record["count"]
    return ticks

def smallest_sighting(records):
    """Return the record (whole dict) with the SMALLEST count.
    If two are tied, return the first one you find."""
    small = records[0]
    for record in records:
        if record["count"] < small["count"]:
            small = record
    return small
            

def ticks_by_city(records):
    """Return a dict of city -> total count, e.g. {"London": 8, ...}"""
    total = {}
    
    for record in records:
        city = record["city"]
        count = record["count"]
    
        if city in total:
            total[city] += count
        else: 
            total[city] = count
    return total
        

def sightings_per_species(records):
    """Return a dict of species -> how many RECORDS mention it (not the count field).
    e.g. "Marsh tick" appears in 3 records, so {"Marsh tick": 3, ...}"""
    totalspecies = {}
    
    for record in records:
        species = record["species"]
        
        if species in totalspecies:
            totalspecies[species] += 1
        else:
            totalspecies[species] = 1
    
    return totalspecies

def sightings_in_city(records, city):
    """Return a LIST of only the records for the given city."""
    recordcity = []
    
    for record in records:
        if city == record["city"]:
            recordcity.append(record)
            
    return recordcity
assert total_ticks(sightings) == 16
assert smallest_sighting(sightings) == {"city": "Leeds", "species": "Tree-hole tick", "count": 1}
assert ticks_by_city(sightings) == {"London": 8, "Leeds": 5, "Bristol": 3}
assert sightings_per_species(sightings) == {
    "Marsh tick": 3, "Tree-hole tick": 1, "Passerine tick": 1, "Fox/badger tick": 1
}
assert sightings_in_city(sightings, "Bristol") == [
    {"city": "Bristol", "species": "Marsh tick", "count": 2},
    {"city": "Bristol", "species": "Fox/badger tick", "count": 1},
]
print("All passed!")