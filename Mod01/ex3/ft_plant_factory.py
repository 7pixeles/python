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

    def __init__(self, name: str, height: float, age: int):
        """
        Initializes a new Plant instance.

        Args:
            name (str): Name of the plant.
            height (int | float): Height in centimeters.
            day (int): Age in days.
        """
        self.name = name
        self.height = height
        self.age = age
        Plant.total_plants += 1

    def show(self):
        """
        Prints the plant's information in a readable format.
        """
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


if __name__ == "__main__":
    """
    Demo block: creates multiple plants and prints their information.
    """
    plants = [
        Plant("Rose", 24.99, 30),
        Plant("Oak", 199.99, 365),
        Plant("Cactus", 4.99, 90),
        Plant("Sunflower", 80.99, 45),
        Plant("Fern", 14.99, 120)
    ]

    print("=== Garden Plant Registry ===")
    for plant in plants:
        print("Created: ", end='')
        plant.show()
    print("\nTotal plants created:", Plant.total_plants)
