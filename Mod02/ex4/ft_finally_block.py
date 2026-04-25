#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    pass


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system():
    plants_test1 = ["Tomato", "Letucce", "Carrots"]
    plants_test2 = ["Tomato", "letucce"]

    print("=== Garden Watering System ===")
    try:
        print("\nOpening watering system")
        for plant in plants_test1:
            water_plant(plant)
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        return
    finally:
        print("Closing watering system")

    try:
        print("\nOpening watering system")
        for plant in plants_test2:
            water_plant(plant)
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        return
    finally:
        print("Closing watering system")

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
