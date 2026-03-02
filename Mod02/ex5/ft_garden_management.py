#!usr/env/bin python3
'''

=== Garden Management System ===

Adding plants to garden...
Added tomato successfully
Added lettuce successfully
Error adding plant: Plant name cannot be empty!

Watering plants...
Opening watering system
Watering tomato - success
Watering lettuce - success
Closing watering system (cleanup)

Checking plant health...
tomato: healthy (water: 5, sun: 8)
Error checking lettuce: Water level 15 is too high (max 10)

Testing error recovery...
Caught GardenError: Not enough water in tank
System recovered and continuing...
Garden management system test complete!

'''

class GardenError(Exception):
    """Base class for all garden-related errors."""
    def __init__(self, message = "Caught a garden error"):
        self.message = message
        super().__init__(message)


class PlantError(GardenError):
    """Error related to plant-specific problems."""
    def __init__(self, message = "Plant Error"):
        super().__init__(message)


class WaterError(GardenError):
    """Error related to watering issues."""
    def __init__(self, message = "watering error"):
        super().__init__(message)

class Sunlight(GardenError):
    """Error related to sunlight hours issues."""
    def __init__(self, message: str):
        super().__init__(message)


class GardenManager():
    def __init__(self):
        self.garden = []
        self.water_tank: int

    def add_plants(plant_name: str, plant_water: int, sunlight_hour: int):
        print("Adding plants to garden...")
        try:
            if plant_name is None:
                raise PlantError("Plant name cannot be empty")
            
            print("Added {plant_name} successfully")
        except PlantError as error:
            print(f"Error adding plant: {error}")
            

    def water_plants(plant_name: str, water_level: int):
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


def main():
    print("=== Garden Management System ===")
    print("\nAdding plants to garden...")
    demo_garden = GardenManager()
    demo_garden.water_tank = 2
    demo.add_plants("tomato", 5, 8)
    demo.add_plants("lettuce", 15, -8)
    demo.add_plants("", 5, 8)
    print("Watering plants...")
    demo = demo.water_plants()
    print("\nChecking plant health...")
    demo.check_plant_health("tomato")
    demo.check_plant_health("lettuce")

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
    main()
