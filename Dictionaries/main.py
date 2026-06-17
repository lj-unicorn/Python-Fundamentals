capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested List in Dictionary
# travel_log = {
#   "France": ["Paris", "Little", "Dijion"],
#   "Germany": ["Stuttgart", "Berling"],
# }

# print Lille
# print(travel_log["France"][1])

# nestedList

nested_list = ["A", "B", ["C", "D"]]
# print(nested_list[2][1])


travel_log = {
    "France": {
        "num_times_visted": "8",
        "cities_visited": ["Paris", "Little", "Dijion"],
    },
    "Germany": {"cities_visited": ["Stuttgart", "Berling"], "total_visits": 5},
}


print(travel_log["Germany"]["cities_visited"][0])