#!/usr/bin/env python3
"""
Module ft_plant_growth.

Defines a simple Plant class that can grow and age over time.
Provides methods to increment height and age, and to display plant info.
"""


class Plant:
    """
    Represents a plant with a name, height, and age in days.

    Attributes:
        name (str): Name of the plant.
        height (int | float): Height in centimeters.
        age (int): Age in days.
    """

    def __init__(self, name: str, height: float, age: int):
        """
        Initializes a new Plant instance.

        Args:
            name (str): Name of the plant.
            height (int | float): Initial height in centimeters.
            age (int): Initial age in days.
        """
        self.name = name
        self.height = height
        self.age = age

    def grow(self, n: float):
        """
        Increases the height of the plant.

        Args:
            n (int | float): Amount to increase the height in centimeters.
        """
        self.height += n

    def aging(self, n: int):
        """
        Increases the age of the plant.

        Args:
            n (int): Number of days to age the plant.
        """
        self.age += n

    def get_info(self):
        """
        Prints the current state of the plant.
        """
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


if __name__ == "__main__":
    """
    Demo of plant growth over a week.
    """
    print("=== Garden Plant Growth ===\n")
    p1 = Plant("Rose", 25.00, 30)
    start_grow = p1.height
    week = range(1, 8)
    for day in week:
        print(f"=== Day {day} ===")
        p1.get_info()
        p1.aging(1)
        p1.grow(0.8)
    print(f"\nGrowth this week: {round(p1.height - start_grow)}cm")
