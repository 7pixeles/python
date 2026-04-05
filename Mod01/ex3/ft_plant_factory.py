#!/usr/bin/env python3

class Plant:
    """
    Represent a plant with basic attributes and tracking.

    Attributes
    ----------
    name : str
        Name of the plant.
    height : float
        Height in centimeters.
    age : int
        Age in days.
    total_plants : int
        Total number of Plant instances created.
    """

    total_plants = 0

    def __init__(self, name: str, height: float, age: int):
        """
        Initialize a Plant instance.
        """
        self.name = name
        self.height = height
        self.age = age
        Plant.total_plants += 1

    def show(self):
        """
        Display the current state of the plant.
        """
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


if __name__ == "__main__":
    plants = [
        Plant("Rose", 24.99, 30),
        Plant("Oak", 199.99, 365),
        Plant("Cactus", 4.99, 90),
        Plant("Sunflower", 80.99, 45),
        Plant("Fern", 14.99, 120)
    ]

    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end='')
        plant.show()
    print("\nTotal plants created:", Plant.total_plants)
