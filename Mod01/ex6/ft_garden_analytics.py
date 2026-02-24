#!/usr/bin/env python3

class Plant:
    """
    Represents a basic plant with a name and height.

    A Plant can grow over time and provides a score value
    based on its height.
    """

    def __init__(self, name, height):
        """
        Initialize a Plant instance.
        """
        self.name = name
        self.height = height

    def grow(self, value):
        """
        Increase the plant height.

        If the value is negative, a warning is printed and
        the height is not modified.
        """
        if value < 0:
            print("[WARNING] Height must have a positive value.")
        else:
            self.height = self.height + value
            print(f"{self.name} grew {value}cm")

    def score_value(self):
        """
        Return the score value of the plant.

        The score is equal to the plant height.

        Returns:
            int or float: Plant score.
        """
        return self.height

    def get_info(self):
        """
        Print plant information.

        Displays the plant name and height.
        """
        print(f"{self.name}: {self.height}cm")


class FloweringPlant(Plant):
    """
    Represents a plant that can produce flowers.

    Extends Plant by adding flower color and blooming state.
    """
    def __init__(self, name, height, color, is_blooming):
        """
        Initialize a FloweringPlant instance.
        """
        super().__init__(name, height)
        self.color = color
        self.is_blooming = is_blooming

    def bloom(self):
        """
        Set the plant as blooming.

        If the plant is not blooming, the blooming state
        becomes True.
        """
        if not self.is_blooming:
            self.is_blooming = True

    def get_info(self):
        """
        Print flowering plant information.

        Displays name, height, flower color and blooming state.
        """
        print(f"{self.name}: {self.height}cm, {self.color} flowers", end=" ")
        if self.is_blooming:
            print("(blooming)")


class PrizeFlower(FloweringPlant):
    """
    Represents a flowering plant that can earn prize points.

    Extends FloweringPlant by adding prize points that
    increase the plant score.
    """
    def __init__(self, name, height, color, is_blooming, prize_points):
        """
        Initialize a PrizeFlower instance.
        """
        super().__init__(name, height, color, is_blooming)
        self.prize_points = prize_points

    def add_prize_points(self, value):
        """
        Add prize points to the plant.
        """
        self.prize_points += value

    def score_value(self):
        """
        Return the total score of the plant.

        The score is the sum of height and prize points.

        Returns:
            int or float: Total score.
        """
        return self.height + self.prize_points

    def get_info(self):
        """
        Print prize flower information.

        Displays name, height, flower color, blooming state,
        and prize points.
        """
        print(f"{self.name}: {self.height}cm, {self.color} flowers", end=" ")
        if self.is_blooming:
            print("(blooming)", end=", ")
        else:
            print("(not blooming)", end=", ")
        print(f"Prize points: {self.prize_points}")


class GardenManager:
    """
    Manages a collection of plants belonging to a garden owner.

    Tracks plants, growth activity and garden statistics.
    """
    total_gardens = 0

    def __init__(self, owner):
        """
        Initialize a GardenManager instance.
        """
        self.owner = owner
        self.plant_list = []
        self.plants_added = 0
        self.total_growth = 0
        GardenManager.total_gardens += 1

    def add_plant(self, plant):
        """
        Add a plant to the garden.

        Only Plant instances or subclasses are accepted.
        """
        if not isinstance(plant, Plant):
            print("[WARNING] You cannot add a plant that does not exist.")
        else:
            self.plant_list.append(plant)
            self.plants_added += 1
            print(f"Added {plant.name} to {self.owner}'s garden")

    def help_grow(self, value):
        """
        Grow all plants in the garden.

        Each plant increases its height by the given value.
        """
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plant_list:
            plant.grow(value)
            self.total_growth += value

    def calculate_score(self):
        """
        Calculate the total garden score.

        Returns:
            int or float: Sum of all plant scores.
        """
        return sum(plant.score_value() for plant in self.plant_list)

    @classmethod
    def create_garden_network(cls, owners):
        """
        Create multiple gardens from a list of owners.
        Returns:
            list[GardenManager]: List of created gardens.
        """
        gardens = []

        for owner in owners:
            gardens.append(cls(owner))

        return gardens

    @staticmethod
    def validate_height(height):
        """
        Validate a plant height value.

        Returns:
            bool: True if height is positive.
        """
        return height > 0

    class GardenStats():
        """
        Utility class for garden statistics calculations.
        """
        @staticmethod
        def count_types(plant_list):
            """
            Count plant types in a list.

            Returns:
                tuple: (regular, flowering, prize)
            """
            regular = 0
            flower = 0
            prize = 0

            for plant in plant_list:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flower += 1
                elif isinstance(plant, Plant):
                    regular += 1

            return regular, flower, prize

        @staticmethod
        def calculate_garden_scores(plant_list):
            """
            Calculate the total score of a plant list.

            Returns:
                int or float: Total score.
            """
            return sum(plant.score_value() for plant in plant_list)

    def generate_report(self):
        """
        Print a detailed garden report.

        Includes:
        - Plant list
        - Plants added
        - Total growth
        - Plant type counts
        - Height validation test
        """
        print(f"\n=== {self.owner}'s Garden Report ===", end="\n")
        print("Plants in garden:")

        for plant in self.plant_list:
            print("-", end=" ")
            plant.get_info()

        print(f"\nPlants added: {self.plants_added}", end=", ")

        print(f"Total growth: {self.total_growth}cm")
        regular, flower, prize = self.GardenStats.count_types(self.plant_list)

        print("Plant types:", end=" ")
        print(regular, "regular", end=", ")
        print(flower, "flowering", end=", ")
        print(prize, "prize", end="\n\n")

        print("Height validation test:", self.validate_height(10))


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    # Create gardens
    gardens = GardenManager.create_garden_network(["Ana", "Bob"])

    # Add plants to gardens
    gardens[0].add_plant(Plant("Oat Tree", 45))
    gardens[1].add_plant(Plant("Pine", 50))
    gardens[0].add_plant(FloweringPlant("Rose", 26, "red", True))
    gardens[1].add_plant(FloweringPlant("Tulip", 20, "yellow", True))
    gardens[0].add_plant(PrizeFlower("Sunflower", 51, "yellow", False, 10))
    gardens[1].add_plant(PrizeFlower("Lily", 30, "white", True, 5))

    # Grow gardens
    for garden in gardens:
        garden.help_grow(1)

    # Individual Report
    for garden in gardens:
        garden.generate_report()

    # Resumen
    print("Garden scores - ", end="")
    for garden in gardens:
        print(f"{garden.owner}: {garden.calculate_score()}", end=", ")
    print(f"\nTotal gardens managed: {GardenManager.total_gardens}")
