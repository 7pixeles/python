#!/usr/bin/env python3

from typing import Any
from abc import ABC, abstractmethod


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, ctr: Any) -> bool:
        pass

    @abstractmethod
    def act(self, ctr: Any) -> None:
        pass


class InvalidStrategyError(Exception):
    pass


class NormalStrategy(BattleStrategy):
    # The hasattr() function returns True if the specified object
    # has the specified attribute, otherwise False.

    def is_valid(self, ctr: Any) -> bool:
        return hasattr(ctr, "attack")

    def act(self, ctr: Any) -> None:
        if not self.is_valid(ctr):
            raise InvalidStrategyError(
                "Creature cannot use NormalStrategy"
            )
        print(ctr.attack())


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, ctr: Any) -> bool:
        return (
            hasattr(ctr, "transform")
            and hasattr(ctr, "revert")
            and hasattr(ctr, "attack")
        )

    def act(self, ctr: Any) -> None:
        if not self.is_valid(ctr):
            raise InvalidStrategyError(
                "Creature cannot use AggressiveStrategy"
            )
        print(ctr.transform())
        print(ctr.attack())
        print(ctr.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, ctr: Any) -> bool:
        return (
            hasattr(ctr, "heal")
            and hasattr(ctr, "attack")
        )

    def act(self, ctr: Any) -> None:
        if not self.is_valid(ctr):
            raise InvalidStrategyError(
                "Creature cannot use DefensiveStrategy"
            )
        print(ctr.attack())
        print(ctr.heal())
