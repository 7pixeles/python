#!/usr/bin/env python3

import random

regular_names = [
    "Alice",
    "bob",
    "Charlie",
    "dylan",
    "Emma",
    "Gregory",
    "john",
    "kevin",
    "Liam"
    ]

if __name__ == "__main__":
    print("=== Game Data Alchmeist ===\n")

    print("Initial list of players:", regular_names)

    capitalized = [name.capitalize() for name in regular_names]
    print("New list with all names capitalized:", capitalized)

    original_capitalized = [name for name in regular_names
                            if name and name[0].isupper()]
    print("New list of capitalized names only:", original_capitalized)

    name_dict = {name: random.choice(range(1000)) for name in capitalized}
    print("Score dict:", name_dict)

    average = sum(value for key, value in name_dict.items()) / len(name_dict)
    print("Score average is ", round(average, 2))

    high_scores = {name: score for name, score in name_dict.items()
                   if score > average}
    print("High scores:", high_scores)
