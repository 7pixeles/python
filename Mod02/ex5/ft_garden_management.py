#!usr/env/bin python3


class GardenError(Exception):
    """Base class for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Error related to plant-specific problems."""
    def __init__(self, message="Plant Error"):
        super().__init__(message)


class WaterError(GardenError):
    """Error related to watering issues."""
    def __init__(self, message="Watering error"):
        super().__init__(message)


class Sunlight(GardenError):
    """Error related to sunlight hours issues."""
    def __init__(self, message: str):
        super().__init__(message)


class GardenManager():
    def __init__(self):
        self.garden = []
        self.water_tank: int

    def add_plants(self, plant_name: str, plant_water: int,
                   sunlight_hour: int) -> None:
        try:
            if plant_name is not None or plant_name != "":
                plant = {"name": plant_name,
                         "water": plant_water,
                         "sun": sunlight_hour}
                self.garden.append(plant)
                print(f"Added {plant_name} successfully")
            else:
                raise PlantError("Plant name cannot be empty")
        except PlantError as error:
            print(f"Error adding plant: {error}")

    def water_plants(self, plant_name: str, water_level: int) -> None:
        try:
            if water_level > 10:
                raise WaterError(
                    f"Water level {water_level} is too hight (max 10)")
            elif water_level < 1:
                raise WaterError(
                    f"Water level {water_level} is too low (min 1)")
            print(f"Watering {plant_name} - Success")
        except WaterError as error:
            print(f"Error: {error}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name: str, water_level: int,
                           sunlight_hours: str) -> None:
        try:
            if plant_name is None:
                raise ValueError("Plant name cannot be empty")
        except ValueError as error:
            print(f"Error: {error}")
            return
        try:
            if water_level > 10:
                raise ValueError(
                    f"Water level {water_level} is too hight (max 10)")
            elif water_level < 1:
                raise ValueError(
                    f"Water level {water_level} is too low (min 1)")
        except ValueError as error:
            print(f"Error checking {plant_name}: {error}")
            return
        try:
            if sunlight_hours < 2:
                raise ValueError(
                    f"Sunlight hours {sunlight_hours} is too high (min 2)")
            elif sunlight_hours > 16:
                raise ValueError(
                    f"Sunlight hours {sunlight_hours} is too low (max 16)")
        except ValueError as error:
            print(f"Error: {error}")
            return
        print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    print("=== Garden Management System ===")
    print("\nAdding plants to garden...")
    demo_garden = GardenManager()
    demo_garden.water_tank = 8
    print("Adding plants to garden...")
    demo_garden.add_plants("tomato", 5, 8)
    demo_garden.add_plants("lettuce", 15, -8)
    demo_garden.add_plants("", 5, 8)
    print("\nWatering plants...")
    demo_garden.water_plants("lettuce", 5)
    print("\nChecking plant health...")
    demo_garden.check_plant_health("tomato", -2, 8)
    demo_garden.check_plant_health("lettuce", 8, 2)

    print("\nTesting error recovery")
    try:
        if demo_garden.water_tank < 3:
            raise WaterError("Not enought water in the tank")
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    finally:
        print("System recovered and continuing...")

    print("\n Garden management system test complete!")


if __name__ == "__main__":
    test_plant_checks()
