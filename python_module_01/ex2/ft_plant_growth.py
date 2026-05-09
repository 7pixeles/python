#!/usr/bin/env python3

class Plant:

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self, value: float) -> None:
        self.height += value

    def increment_age(self, value: int) -> None:
        self.age += value

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Growth ===\n")

    plant = Plant("Rose", 25.00, 30)
    start = plant.height

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant.show()
        plant.increment_age(1)
        plant.grow(0.8)

    print(f"\nGrowth this week: {round(plant.height - start, 1)} cm")
