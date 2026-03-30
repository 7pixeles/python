#!/usr/bin/env python3

"""
Module ft_garden_security.

Defines the SecurePlant class, representing a plant with basic safety
checks for height and age.

Includes validation to prevent negative values and keeps a global
counter of created plants.
"""


class SecurePlant:
    """
    Represents a plant with protected attributes.
    - Plant name
    - Height (in centimeters)
    - Age (in days)
    """

    def __init__(self, name: str, height: float, age: int):
        self._name = name
        self._height = 0
        self._age = 0

        self.set_height(height)
        self.set_age(age)

        print(f"Plant created: {self._name}: "
              f"{round(self._height, 1)}cm, {self._age} days\n")

    def _validate_height(self, value):
        if not isinstance(value, (int, float)):
            print(f"[ERROR] {self._name}: Height must be a number")
            return False

        if value < 0:
            print(f"[ERROR] {self._name}: Height can't be negative")
            return False

        if value > 1000:
            print(f"[ERROR] {self._name}: Height value unrealistic")
            return False

        return True

    def get_height(self):
        """
        Returns the current height of the plant.

        Returns:
            int | float: Height in centimeters.
        """
        return self._height

    def get_age(self):
        """
        Returns the current age of the plant.

        Returns:
            int: Age in days.
        """
        return self._age

    def set_height(self, new_height: float):
        """
        Sets the height of the plant.
        Only positive values are allowed.

        Args:
            new_height (float): New height in centimeters.
        """
        if new_height >= 0:
            self._height = new_height
            print(f"Height updated: {new_height}cm")
        else:
            print(f"[ERROR] {self._name}: Height can't be negative")
            print("Height update rejected")

    def set_age(self, new_age):
        """
        Sets the age of the plant.
        Only positive values are allowed.

        Args:
            new_age (int): New age in days.
        """
        if new_age >= 0:
            self._age = new_age
            print(f"Age updated: {new_age}cm")
        else:
            print(f"[ERROR] {self._name}: Age can't be negative")
            print("Age update rejected")

    def get_info(self):
        """
        Prints the current information of the plant.
        """
        print(f"\nCurrent state: {self._name} "
              f"({self._height}cm, {self._age} days)")


if __name__ == "__main__":
    """
    Direct module execution block.

    Creates a demonstration plant and modifies some values.
    """
    print("=== Garden Security System ===")
    demo_plant = SecurePlant("Rose", 25, 30)
    demo_plant.set_height(-5)
    demo_plant.set_age(-2)
    demo_plant.get_info()
