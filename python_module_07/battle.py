#!/usr/bin/env python3

from typing import Any
from ex0.factory import FlameFactory, AquaFactory


def test_factory(factory: Any) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print("Testing factory")

    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def battle(factory_a: Any, factory_b: Any) -> None:
    creature_a = factory_a.create_base()
    creature_b = factory_b.create_base()

    print("Testing battle:")
    print(creature_a.describe())
    print("vs")
    print(creature_b.describe())
    print("fight!")
    print(creature_a.attack())
    print(creature_b.attack())


if __name__ == "__main__":
    flame = FlameFactory()
    aqua = AquaFactory()

    test_factory(flame)
    print()
    test_factory(aqua)
    print()

    battle(flame, aqua)
