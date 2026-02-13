#!/usr/bin/env python3
"""
Module ft_plant_types.

Defines a hierarchy of plant types for a garden simulation.

Classes:
    Plant: Base class for all plant types, providing common attributes.
    Flower: Represents flowering plants that can bloom and change color.
    Tree: Represents trees that calculate shade area based on trunk diameter.
    Vegetable: Represents vegetables with harvest season and nutritional value.

Usage:
    This module can be run as a script to demonstrate plant growth behavior
    and display information for each plant type.

Notes:
    - The Plant base class is not meant to be instantiated directly.
    - Subclasses implement their specific grow behavior.
    - COLORS is a shared constant used for flower color selection.
"""

COLORS = ["red", "white", "yellow", "pink", "purple", "orange"]


class Plant:
    """
    Base class for all plants.

    Represents common attributes shared by every plant type.

    Attributes:
        name (str): Plant name.
        height (int): Height in centimeters.
        day (int): Age of the plant in days.

    Notes:
        This class is not meant to be instantiated directly.
        Subclasses must implement `grow()`.
    """
    def __init__(self, name, height, day):
        """
        Initialize a Plant instance.

        Args:
            name (str): Name of the plant.
            height (int): Height in centimeters.
            day (int): Age in days.
        """
        self.name = name
        self.height = height
        self.day = day


class Flower(Plant):
    """
    Flower plant type.

    Flowers change color when growing. The color is selected deterministically
    based on plant age and height.

    Attributes:
        color (str): Current flower color.
    """

    def __init__(self, name, height, day, color):
        """
        Create a Flower.

        Args
             name (str): Flower name.
            - height (int): Height in centimeters.
            - day (int): Age in days.
            - color (str): Initial color.
        """
        super().__init__(name, height, day)
        self.color = color

    def bloom(self):
        """
        Update flower color.

        The color index is computed as:

            (day + height) % len(COLORS)

        This guarantees a valid index while producing predictable variation.

        Side effects:
            Mutates self.color.
        """
        index = (self.day + self.height) % len(COLORS)
        self.color = COLORS[index]

    def grow(self):
        """
        Trigger flower growth behavior.

        Currently implemented as blooming (color change).
        """
        self.bloom()

    def get_info(self):
        """
        Print flower information to standard output.
        """
        print(f"{self.name} (Flower): {self.height}cm, {self.day} days, "
              f"{self.color} color")
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """
    Tree plant type.

    Trees compute the amount of shade they provide based on trunk diameter.

    Attributes:
        trunk_diameter (float): Diameter of the trunk in centimeters.
        shade (float): Calculated shade area in square meters (after grow()).
    """
    def __init__(self, name, height, day, trunk_diameter):
        """
        Create a Tree.

        Args:
            name (str): Tree name.
            height (int): Height in centimeters.
            day (int): Age in days.
            trunk_diameter (float): Trunk diameter in centimeters.
        """
        super().__init__(name, height, day)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """
        Calculate shade area.

        Shade is approximated using a simplified circle area formula:

            area = 31416 * radius²

        where radius is trunk_diameter converted to meters.

        Side effects:
            Sets self.shade.
        """
        radius = self.trunk_diameter / 1000
        self.shade = 31416 * radius ** 2

    def grow(self):
        """
        Trigger tree growth behavior.

        Currently implemented as shade calculation.
        """
        self.produce_shade()

    def get_info(self):
        """
        Print tree information to standard output.
        """
        print(f"{self.name} (Tree): {self.height}cm, {self.day} days, "
              f"{self.trunk_diameter} cm diameter")
        print(f"{self.name} provides {self.shade:.0f} square meters of shade")


class Vegetable(Plant):
    """
    Vegetable plant type.

    Vegetables store harvest season and nutritional value.

    Growth logic is intentionally left unimplemented.
    """
    def __init__(self, name, height, day, harvest_season, nutritional_value):
        """
        Create a Vegetable.

        Args:
            name (str): Vegetable name.
            height (int): Height in centimeters.
            day (int): Age in days.
            harvest_season (str): Harvest season.
            nutritional_value (str): Main nutritional benefit.
        """
        super().__init__(name, height, day)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def grow(self):
        """
        Vegetable growth placeholder.

        Currently does nothing.
        """
        pass

    def get_info(self):
        """
        Print vegetable information to standard output.
        """
        print(f"{self.name} (Vegetable): {self.height}cm, {self.day} days, "
              f"{self.harvest_season} harvest")
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    plants = [
        Flower("Rose", 25, 30, "Red"),
        Flower("Sunflower", 80, 45, "Yellow"),
        Tree("Oak", 15, 120, 50),
        Tree("Eucaliptus", 200, 12, 64),
        Vegetable("Tomato", 2, 1, "Winter", "Vitamin C"),
        Vegetable("Peas", 2, 1, "Summer", "Iron")
    ]

    print("\n === Garden Plant Types === \n")
    for plant in plants:
        plant.grow()
        plant.get_info()
        print("--------------------------------------------------")
