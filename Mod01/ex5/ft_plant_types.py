#!/usr/bin/env python3

class Plant:

    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        pass

    def age_up(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        print(f"[asking the {self.name.lower()} to bloom]")
        self.is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        status = "is blooming beautifully!" if self.is_blooming else \
                 "has not bloomed yet"
        print(f"{self.name} {status}")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk: float):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk

    def produce_shade(self) -> None:
        print(f"[asking the {self.name.lower()} to produce shade]")
        print(f"Tree {self.name} now produces a shade of "
              f"{round(self.height, 1)}cm long and "
              f"{round(self.trunk_diameter, 1)}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 1)}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, season: str):
        super().__init__(name, height, age)
        self.harvest_season = season
        self.nutritional_value = 0

    def grow(self) -> None:
        self.height += 2.1
        self.nutritional_value += 1

    def age_up(self) -> None:
        super().age_up()
        self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    flwr = Flower("Rose", 15.0, 10, "red")
    flwr.show()
    flwr.bloom()
    flwr.show()

    print("\n=== Tree")
    tr = Tree("Oak", 200.0, 365, 5.0)
    tr.show()
    tr.produce_shade()

    print("\n=== Vegetable")
    veg = Vegetable("Tomato", 5.0, 10, "April")
    veg.show()

    for _ in range(20):
        veg.grow()
        veg.age_up()

    veg.show()
