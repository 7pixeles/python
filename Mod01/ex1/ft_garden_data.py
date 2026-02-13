#!/usr/bin/env python3
"""
Module ft_garden_data

Defines a basic Plant class with attributes for name, height, and age in days.
Includes a demonstration of creating multiple plants and printing their info.
"""


class Plant:
    """
    Represents a plant with a name, height, and age.

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
            height (int | float): Height in centimeters.
            day (int): Age in days.
        """
        self.name = name
        self.height = height
        self.day = day


if __name__ == "__main__":
    '''
    Demo creating multiple plants and printing their information.
    '''
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)
    p3 = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    print(f"{p1.name}: {p1.height}cm, {p1.day} days old")
    print(f"{p2.name}: {p2.height}cm, {p2.day} days old")
    print(f"{p3.name}: {p3.height}cm, {p3.day} days old")
