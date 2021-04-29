# Dictionaries {}
# Lists []


# {
#     Key:[List],
#     Key2: {Dict}
# }

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Gernamy": ["Berlin", "Hamburg"]
}

# Nesting Dictionary in a Dictionary
cities_visited = ["Paris", "Lille", "Dijon"]
travel_log = {
    "France": cities_visited,
    "Gernamy": ["Berlin", "Hamburg"]
}
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Gernamy": {
        "cities_visited": ["Berlin", "Hamburg"],
        "total_visits": 21
    }
}

############## Nesting Dictionary in a List
# [
#     {
#         Key: [List],
#         Key2: {Dict}
#     },
#     {
#         Key: Value,
#         Key2: Value
#     }
# ]


travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Gernamy",
        "cities_visited": ["Berlin", "Hamburg"],
        "total_visits": 21
    }
]


def add_new_country(country_visited_param, visits_count_param, cities_visited_list_param):
    new_record = {
        "country": country_visited_param,
        "cities_visited": cities_visited_list_param,
        "total_visits": visits_count_param
    }

    travel_log.append(new_record)
    pass


add_new_country(
    country_visited_param="Russia",
    visits_count_param=2,
    cities_visited_list_param=["Moscow", "Saint Petersburg"]
)

print(travel_log)
