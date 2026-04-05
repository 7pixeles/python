#!/usr/bin/env python3

class Plant:
    """
    A class to represent a plant with protected attributes.

    Attributes
    ----------
    _name : str
        The name of the plant.
    _height : float
        The height of the plant in centimeters.
    _age : int
        The age of the plant in days.
    """

    def __init__(self, name: str, height: float, age: int):
        self._name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)
        print(f"Plant created: {self._name}: {self._height}cm, "
              f"{self._age} days old")

    def get_height(self) -> float:
        """Return the current height."""
        return self._height

    def set_height(self, value: float) -> None:
        """Set height with validation."""
        if value >= 0:
            self._height = float(value)
            print(f"Height updated: {value}cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def get_age(self) -> int:
        """Return the current age."""
        return self._age

    def set_age(self, value: int) -> None:
        """Set age with validation."""
        if value >= 0:
            self._age = int(value)
            print(f"Age updated: {value} days")
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def show(self) -> None:
        """Display the plant's current state."""
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
