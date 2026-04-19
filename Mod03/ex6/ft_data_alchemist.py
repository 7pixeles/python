#!/usr/bin/env python3

import random

"""
Game Data Alchemist script.

Processes a list of player names by normalizing capitalization, filtering
originally capitalized names, assigning random scores, and computing summary
statistics.

Parameters
----------
None

Returns
-------
None

Notes
-----
This script performs the following steps:
- Displays the initial list of player names.
- Normalizes all names to capitalized format.
- Filters names that were originally capitalized.
- Generates a random score in the range [0, 999] for each player.
- Computes the mean score.
- Selects players with scores above the mean.

The output is non-deterministic due to the use of random score generation.
"""

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
