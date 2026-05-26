#!/usr/bin/env python3

from typing import Any
from ex1.creature_factory import (HealingCreatureFactory,
                                  TransformCreatureFactory)


def healing_factory(factory: Any) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print("Testing Creature with healing capability")

    print("\nbase:")
    print(base.describe())
    print(base.attack())
    print(base.heal())

    print("\nevolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def transform_factory(factory: Any) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print("Testing Creature with transform capability")

    print("\nbase:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    print("\nevolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


if __name__ == "__main__":
    healing = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    healing_factory(healing)
    print()
    transform_factory(transform)
