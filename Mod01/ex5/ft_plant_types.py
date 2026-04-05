#!/usr/bin/env python3

class Plant:
    """
    Base class representing a generic plant.

    Attributes
    ----------
    name : str
        Name of the plant.
    height : float
        Height in centimeters.
    age : int
        Age in days.
    """
    def __init__(self, name: str, height: float, age: int):
        """
        Initialize a Plant instance.

        Parameters
        ----------
        name : str
            Name of the plant.
        height : float
            Initial height in centimeters.
        age : int
            Initial age in days.
        """
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        """
        Define basic growth behavior.

        This method is intended to be overridden by subclasses.
        """
        pass

    def age_up(self) -> None:
        """
        Increase plant age by one day.
        """
        self.age += 1

    def show(self) -> None:
        """
        Display basic plant information.

        Prints the name, height, and age of the plant.
        """
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


class Flower(Plant):
    """
    Represent a flowering plant.

    Attributes
    ----------
    color : str
        Color of the flower.
    is_blooming : bool
        Indicates whether the flower is blooming.
    """
    def __init__(self, name: str, height: float, age: int, color: str):
        """
        Initialize a Flower instance.

        Parameters
        ----------
        name : str
            Name of the plant.
        height : float
            Initial height in centimeters.
        age : int
            Initial age in days.
        color : str
            Flower color.
        """
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        """
        Trigger the blooming state of the flower.
        """
        print(f"[asking the {self.name.lower()} to bloom]")
        self.is_blooming = True

    def show(self) -> None:
        """
        Display flower information.

        Extends base information with color and blooming state.
        """
        super().show()
        print(f"Color: {self.color}")
        status = "is blooming beautifully!" if self.is_blooming else \
                 "has not bloomed yet"
        print(f"{self.name} {status}")


class Tree(Plant):
    """
    Represent a tree that produces shade.

    Attributes
    ----------
    trunk_diameter : float
        Diameter of the trunk in centimeters.
    """
    def __init__(self, name: str, height: float, age: int, trunk: float):
        """
        Initialize a Tree instance.

        Parameters
        ----------
        name : str
            Name of the plant.
        height : float
            Initial height in centimeters.
        age : int
            Initial age in days.
        trunk : float
            Trunk diameter in centimeters.
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk

    def produce_shade(self) -> None:
        """
        Display shade dimensions based on tree size.
        """
        print(f"[asking the {self.name.lower()} to produce shade]")
        print(f"Tree {self.name} now produces a shade of "
              f"{round(self.height, 1)}cm long and "
              f"{round(self.trunk_diameter, 1)}cm wide.")

    def show(self) -> None:
        """
        Display tree information.

        Extends base information with trunk diameter.
        """
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 1)}cm")


class Vegetable(Plant):
    """
    Represent a vegetable with nutritional value.

    Attributes
    ----------
    harvest_season : str
        Season when the vegetable is harvested.
    nutritional_value : int
        Accumulated nutritional value.
    """
    def __init__(self, name: str, height: float, age: int, season: str):
        """
        Initialize a Vegetable instance.

        Parameters
        ----------
        name : str
            Name of the plant.
        height : float
            Initial height in centimeters.
        age : int
            Initial age in days.
        season : str
            Harvest season.
        """
        super().__init__(name, height, age)
        self.harvest_season = season
        self.nutritional_value = 0

    def grow(self) -> None:
        """
        Increase height and nutritional value.
        """
        self.height += 2.1
        self.nutritional_value += 1

    def age_up(self) -> None:
        """
        Increase age and nutritional value.
        """
        super().age_up()
        self.nutritional_value += 1

    def show(self) -> None:
        """
        Display vegetable information.

        Extends base information with harvest season and nutrition.
        """
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
