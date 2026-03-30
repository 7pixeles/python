#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self, value):
        if value < 0:
            print("[WARNING] Height must have a positive value.")
        else:
            self.height = self.height + value
            print(f"{self.name} grew {value}cm")

    def score_value(self):
        return self.height

    def get_info(self):
        print(f"{self.name}: {self.height}cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, color, is_blooming):
        super().__init__(name, height)
        self.color = color
        self.is_blooming = is_blooming

    def bloom(self):
        if not self.is_blooming:
            self.is_blooming = True

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.color} flowers", end=" ")
        if self.is_blooming:
            print("(blooming)")


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, is_blooming, prize_points):
        super().__init__(name, height, color, is_blooming)
        self.prize_points = prize_points

    def add_prize_points(self, value):

        self.prize_points += value

    def score_value(self):
        return self.height + self.prize_points

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.color} flowers", end=" ")
        if self.is_blooming:
            print("(blooming)", end=", ")
        else:
            print("(not blooming)", end=", ")
        print(f"Prize points: {self.prize_points}")


class GardenManager:
    total_gardens = 0

    def __init__(self, owner):
        self.owner = owner
        self.plant_list = []
        self.plants_added = 0
        self.total_growth = 0
        GardenManager.total_gardens += 1

    def add_plant(self, plant):
        if not isinstance(plant, Plant):
            print("[WARNING] You cannot add a plant that does not exist.")
        else:
            self.plant_list.append(plant)
            self.plants_added += 1
            print(f"Added {plant.name} to {self.owner}'s garden")

    def help_grow(self, value):
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plant_list:
            plant.grow(value)
            self.total_growth += value

    def calculate_score(self):
        return sum(plant.score_value() for plant in self.plant_list)

    @classmethod
    def create_garden_network(cls, owners):
        gardens = []

        for owner in owners:
            gardens.append(cls(owner))

        return gardens

    @staticmethod
    def validate_height(height):
        return height > 0

    class GardenStats():
        @staticmethod
        def count_types(plant_list):
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
            return sum(plant.score_value() for plant in plant_list)

    def generate_report(self):
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
    print("=== Garden Statistics ===\n")

    # Create gardens
    gardens = GardenManager.create_garden_network(["Alice", "Bob"])

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
