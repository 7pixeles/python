#!/usr/bin/env python3

import random


achievements = [
    "Crafting Genius",
    "First Steps",
    "Speed Runner",
    "Master Explorer",
    "Treasure Hunter",
    "Boss Slayer",
    "Untouchable",
    "Strategist",
    "Survivor",
    "Sharp Mind",
    "Collector Supreme",
    "World Savior",
    "Unstoppable",
    "Hidden Path Finder"
]


def gen_player_achievement() -> set:
    """
    Generate a random set of achievements for a player.

    Randomly selects between 6 and the total number of available
    achievements and returns them as a set to ensure uniqueness.

    Returns
    -------
    set of str
        A set containing randomly selected achievements.

    Notes
    -----
    Uses ``random.sample``, so no duplicates are included. The result
    depends on the global ``achievements`` list.
    """
    count = random.randint(6, len(achievements))
    achievement = random.sample(achievements, count)
    return set(achievement)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    a = gen_player_achievement()
    print("Player Alice:", a)
    b = gen_player_achievement()
    print("Player Bob:", b)
    c = gen_player_achievement()
    print("Player Charlie:", c)
    d = gen_player_achievement()
    print("Player Dylan:", d)

    # All player achievements
    all_achievements = a.union(b, c, d)
    print("\nAll distinct achievements:", all_achievements)

    print("")

    # Common achievement
    common = a.intersection(b, c, d)
    print(f"Common achievements: {common}")

    print("")

    # Unique achievements for each player
    only_a = a.difference(b.union(c, d))
    print("Only Alice has:", only_a)
    only_b = b.difference(a.union(c, d))
    print("Only Bob has:", only_b)
    only_c = c.difference(a.union(b, d))
    print("Only Charlie has:", only_c)
    only_d = d.difference(a.union(b, c))
    print("Only Dylan has:", only_d)

    print("")

    # Missing achievements
    miss_a = all_achievements.difference(a)
    print("Alice is missing:", miss_a)
    miss_b = all_achievements.difference(b)
    print("Bob is missing:", miss_b)
    miss_c = all_achievements.difference(c)
    print("Charlie is missing:", miss_c)
    miss_d = all_achievements.difference(d)
    print("Dylan is missing:", miss_d)
