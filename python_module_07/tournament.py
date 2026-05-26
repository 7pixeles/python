#!/usr/bin/env python3

from typing import Any

from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2.strategy import NormalStrategy, DefensiveStrategy, AggressiveStrategy
from ex2.strategy import InvalidStrategyError
# factory -> create criature
# strategy -> decide how act
# tournament -> organize attacks


def battle(opponents: list[tuple[Any, Any]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    # Check the number of opponents.
    # Prevent them from fighting each other or facing the same opponent twice.
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            # Unpack the tuples
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            # Create creature with appropiated factory
            creature1 = factory1.create_base()
            creature2 = factory2.create_base()

            # Presenting creatures
            print("\n* Battle *")
            print(creature1.describe())
            print(" vs ")
            print(creature2.describe())
            print("Now, fight!")

            # Try each strategy with each creature
            try:
                strategy1.act(creature1)
                strategy2.act(creature2)
            except InvalidStrategyError as error:
                print("Battle error, aborting tournament:", error)
                return


def format_opponents(opponents: list[tuple[Any, Any]]) -> str:
    names = []
    for factory, strategy in opponents:
        f_name = factory.__class__.__name__.replace("Factory", "")
        s_name = strategy.__class__.__name__.replace("Strategy", "")
        names.append(f"({f_name} + {s_name})")

    return "[" + ", ".join(names) + "]"


if __name__ == "__main__":
    # Creating creatures Factory
    flame_f = FlameFactory()
    aqua_f = AquaFactory()
    healing_f = HealingCreatureFactory()
    transform_f = TransformCreatureFactory()

    # Creating different estrategies
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    # Level 0
    print("\nTournament 0 (basic)")
    opponents = [(flame_f, normal), (healing_f, defensive)]
    print(format_opponents(opponents))
    battle(opponents)

    # Level 1
    print("\nTournament 1 (error)")
    opponents = [(flame_f, aggressive), (healing_f, defensive)]
    print(format_opponents(opponents))
    battle(opponents)

    # Level 2
    print("\nTournament 2 (multiple)")
    opponents = [(aqua_f, normal),
                 (healing_f, defensive),
                 (transform_f, aggressive)]
    print(format_opponents(opponents))
    battle(opponents)
