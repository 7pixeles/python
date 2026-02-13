#!/usr/bin/env python3
"""
Module ft_plant_factory.

Defines a simple Plant class with basic attributes and a global counter
for all plants created. Provides a method to print plant information.
"""


class Plant:
    """
    Represents a plant with basic attributes.

    Attributes:
        name (str): Name of the plant.
        height (int | float): Height in centimeters.
        day (int): Age in days.

    Class Attributes:
        total_plants (int): Counts the total number of Plant instances created.
    """

    total_plants = 0
    """Total number of Plant instances created."""

    def __init__(self, name, height, day):
        """
        Initializes a new Plant instance.

        Args:
            name (str): Name of the plant.
            height (int | float): Height in centimeters.
            day (int): Age in days.
        """
        self.name = name
        self.height = height
        self.day = day
        Plant.total_plants += 1

    def get_info(self):
        """
        Prints the plant's information in a readable format.
        """
        print(f"{self.name} ({self.height}cm, {self.day} days)")


if __name__ == "__main__":
    """
    Demo block: creates multiple plants and prints their information.
    """
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
        Plant("Eucaliptus", 200, 12),
        Plant("Aloe Vera", 2, 1)
    ]

    print("=== Garden Plant Registry ===")
    for plant in plants:
        print("Created: ", end='')
        plant.get_info()
    print("\nTotal plants created:", Plant.total_plants)
