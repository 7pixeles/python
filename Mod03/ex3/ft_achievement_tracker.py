#!/usr/bin/env python3
"""
Track and analyze player achievements.

Provides a Player class and a function to analyze common, unique,
and rare achievements among multiple players.
"""


class Player:
    """Represent a player with a name and a set of achievements."""

    def __init__(self, name: str, achieve: set):
        """
        Initialize a Player instance.

        Args:
                name (str): Player's name.
                achieve (set): Set of player's achievements.
        """
        self.name = name
        self.achieve = set(achieve)


def analyze_player_achievement(p_a: Player, p_b: Player, p_c: Player) -> None:
    """Analyze achievements among three players and print statistics.

    Prints:
        - All unique achievements
        - Common achievements to all players
        - Rare achievements (achieved by only one player)
        - Pairwise common and unique achievements
    """
    print("\n=== Achievement Analytics ===")

    common = p_a.achieve.intersection(p_b.achieve, p_c.achieve)
    total = p_a.achieve.union(p_b.achieve, p_c.achieve)

    print("All unique achievements:", total)
    print("Total unique achievements:", len(total))
    print("\n")
    print("Common to all players:", common)

    inter_ab = p_a.achieve.intersection(p_b.achieve)
    inter_ac = p_a.achieve.intersection(p_c.achieve)
    inter_bc = p_b.achieve.intersection(p_c.achieve)
    repeated = inter_ab.union(inter_ac, inter_bc)
    rare = total.difference(repeated)

    print("Rare achievements (1 player):", rare)
    print("\n")
    print(f"{p_a.name} vs {p_b.name} common:",
          p_a.achieve.intersection(p_b.achieve))
    print(f"{p_a.name} unique:",
          p_a.achieve.difference(p_b.achieve))
    print(f"{p_b.name} unique:",
          p_b.achieve.difference(p_a.achieve))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")

    p_a = Player("alice",
                 {'first_kill',
                  'level_10',
                  'treasure_hunter',
                  'speed_demon'})

    p_b = Player("bob",
                 {'first_kill',
                  'level_10',
                  'boss_slayer',
                  'collector'})

    p_c = Player("charlie",
                 {'level_10',
                  'treasure_hunter',
                  'boss_slayer',
                  'speed_demon',
                  'perfectionist'})

    print(f"Player {p_a.name} achievements:", p_a.achieve)
    print(f"Player {p_b.name} achievements:", p_b.achieve)
    print(f"Player {p_c.name} achievements:", p_c.achieve)

    analyze_player_achievement(p_a, p_b, p_c)
