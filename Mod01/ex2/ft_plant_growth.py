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
        day (int): Age in days.
    """

    def __init__(self, name, height, day):
        """
        Initializes a new Plant instance.

        Args:
            name (str): Name of the plant.
            height (int | float): Initial height in centimeters.
            day (int): Initial age in days.
        """
        self.name = name
        self.height = height
        self.day = day

    def grow(self, n):
        """
        Increases the height of the plant.

        Args:
            n (int | float): Amount to increase the height in centimeters.
        """
        self.height += n

    def age(self, n):
        """
        Increases the age of the plant.

        Args:
            n (int): Number of days to age the plant.
        """
        self.day += n

    def get_info(self):
        """
        Prints the current state of the plant.
        """
        print(f"{self.name}: {self.height}cm, {self.day} days old")


if __name__ == "__main__":
    """
    Demo of plant growth over a week.
    """
    p1 = Plant("Rose", 25, 30)
    end_age = p1.day + 7
    start_grow = p1.height
    print("=== Day 1 ===")
    p1.get_info()
    while (p1.day < end_age):
        p1.age(1)
        p1.grow(3)
    print("=== Day 7 ===")
    p1.get_info()
    print(f"Growth this week: {p1.height - start_grow} cm")
