#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        """
        Initialize a Plant instance.

        Args:
            name (str): Name of the plant.
            height (float): Height in centimeters.
            age (int): Age in days.
        """
        self.name: str = name
        self.height: float = height
        self.age: int = age

    def get_info(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")

    def grow(self) -> None:
        pass

    def age_up(self, days: int) -> None:
        self.age += days


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self.blooming: bool = False

    def bloom(self) -> None:
        print(f"[asking the {self.name} to bloom]")
        self.blooming = True

    def get_info(self) -> None:
        super().get_info()
        print(f"Color: {self.color}")

        if not self.blooming:
            print(f"{self.name} has not bloomed yet")
        else:
            print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float
    ) -> None:

        super().__init__(name, height, age)
        self.trunk_diameter: float = trunk_diameter
        self.shade: bool = False

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        self.shade = True

    def get_info(self) -> None:
        super().get_info()
        print(f"Trunk diameter: {round(self.trunk_diameter, 1)}cm")

        if self.shade:
            print(
                f"Tree {self.name} now produces a shade of "
                f"{round(self.height, 1)}cm long and "
                f"{round(self.trunk_diameter, 1)}cm wide."
            )


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str
    ) -> None:

        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: int = 0

    def grow(self) -> None:
        self.height += 2
        self.nutritional_value += 1

    def age_up(self, days: int) -> None:
        super().age_up(days)
        self.nutritional_value += days

    def get_info(self) -> None:
        super().get_info()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    plants = [
        Flower("Rose", 15, 10, "Red"),
        Flower("Sunflower", 80, 45, "Yellow"),
        Vegetable("Tomato", 5, 10, "April"),
        Vegetable("Peas", 5, 10, "June"),
        Tree("Oak", 200, 365, 5),
        Tree("Pine", 150, 200, 3),
    ]

    print("\n=== Garden Plant Types ===")

    for plant in plants:

        if isinstance(plant, Flower):
            print("\n=== Flower ===")
            plant.get_info()
            plant.bloom()
            plant.get_info()

        elif isinstance(plant, Tree):
            print("\n=== Tree ===")
            plant.get_info()
            plant.produce_shade()
            plant.get_info()

        elif isinstance(plant, Vegetable):
            print("\n=== Vegetable ===")
            plant.get_info()
            plant.grow()
            plant.age_up(20)
            plant.get_info()
