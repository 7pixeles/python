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

    The class manages:
    - Plant name
    - Height (in centimeters)
    - Age (in days)

    It also keeps track of the total number of plant instances created.
    """

    total_plants = 0
    """Total number of SecurePlant instances created."""

    def __init__(self, name, height, age):
        """
        Initializes a new plant.

        Args:
            name (str): Name of the plant.
            height (int | float): Initial height in centimeters.
            age (int): Initial age in days.
        """
        self._name = name
        self._height = height
        self._age = age
        print(f"Plant created: {self._name}")
        SecurePlant.total_plants += 1

    @property
    def height(self):
        """
        Returns the current height of the plant.

        Returns:
            int | float: Height in centimeters.
        """
        print()
        return self._height

    @height.setter
    def height(self, value):
        """
        Sets the height of the plant.

        Only positive values are allowed.

        Args:
            value (int | float): New height in centimeters.
        """
        if value > 0:
            self._height = value
            print(f"Height updated: {value}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("\nSecurity: Negative height rejected")

    @property
    def age(self):
        """
        Returns the current age of the plant.

        Returns:
            int: Age in days.
        """
        return self._age

    @age.setter
    def age(self, value):
        """
        Sets the age of the plant.

        Only positive values are allowed.

        Args:
            value (int): New age in days.
        """
        if value > 0:
            self._age = value
            print(f"Age updated: {value} days [OK]")
        else:
            print(f"Invalid operation attempted: age {value}cm [REJECTED]")
            print("Security: Negative age rejected")

    def get_info(self):
        """
        Prints the current information of the plant.
        """
        print(f"\nCurrent Plant: {self._name} ", end='')
        print(f"({self._height}cm, {self._age} days)")


if __name__ == "__main__":
    """
    Direct module execution block.

    Creates a demonstration plant and modifies some values.
    """
    print("=== Garden Security System ===")
    demo_plant = SecurePlant("Rose", 25, 30)
    demo_plant.height = 5
    demo_plant.age = 52
    demo_plant.get_info()
