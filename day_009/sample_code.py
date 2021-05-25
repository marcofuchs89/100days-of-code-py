from pprint import pprint

# Nesting lists inside a dictionary inside a dictionary
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Avignon"],
        "total_visits": 12,
        "traveled_by": "car",
    },
    "Turkey": {
        "cities_visited": ["Alanya", "Antalya", "Evrenseki", "Aspendos"],
        "total_visits": 1,
        "traveled_by": "plane",
    },
    "United States": {
        "cities_visited": ["San Francisco", "Palo Alto"],
        "total_visits": 3,
        "traveled_by": "plane",
    }
}
pprint("Travel log 1:")
pprint(travel_log)
pprint("")

# Nesting multiple dictionaries inside a list
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Avignon"],
        "total_visits": 12,
        "traveled_by": "car",
    },
    {
        "country": "Turkey",
        "cities_visited": ["Alanya", "Antalya", "Evrenseki", "Aspendos"],
        "total_visits": 1,
        "traveled_by": "plane",
    },
    {
        "country": "United States",
        "cities_visited": ["San Francisco", "Palo Alto"],
        "total_visits": 3,
        "traveled_by": "plane",
    }
]

pprint("Travel Log 2")
pprint(travel_log)
pprint("")
