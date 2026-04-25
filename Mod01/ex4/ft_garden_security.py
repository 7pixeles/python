#!/usr/bin/env python3

class Plant:

    def __init__(self, name: str, height: float, age: int):
        self._name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)
        print(f"Plant created: {self._name}: {self._height}cm, "
              f"{self._age} days old")

    def get_height(self) -> float:
        return self._height

    def set_height(self, value: float) -> None:
        if value >= 0:
            self._height = float(value)
            print(f"Height updated: {value}cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def get_age(self) -> int:
        return self._age

    def set_age(self, value: int) -> None:
        if value >= 0:
            self._age = int(value)
            print(f"Age updated: {value} days")
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def show(self) -> None:
        print(f"Current state: {self._name}: {self._height}cm, "
              f"{self._age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    ind_plant = Plant("Rose", 15.0, 10)
    ind_plant.set_height(25)
    ind_plant.set_age(30)
    ind_plant.set_height(-5)
    ind_plant.set_age(-2)
    ind_plant.show()
