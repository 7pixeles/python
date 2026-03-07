#!usr/env/bin python3


class GardenError(Exception):
    """Base class for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Exception raised for plant-related problems."""
    def __init__(self, message="Plant Error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    """Exception raised for watering problems."""
    def __init__(self, message="Watering error") -> None:
        super().__init__(message)


class Sunlight(GardenError):
    """Exception raised for invalid sunlight conditions."""
    def __init__(self, message: str) -> None:
        super().__init__(message)


class GardenManager():
    """Manage plants, watering, and health checks in a garden."""
    def __init__(self) -> None:
        """Initialize the garden manager."""
        self.garden = []
        self.water_tank: int

    def add_plants(self, plant_name: str, plant_water: int,
                   sunlight_hour: int) -> None:
        """Add a plant with water and sunlight requirements."""
        try:
            if plant_name:
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
        """Water a plant if the water level is within valid limits."""
        try:
            if water_level > 10:
                raise WaterError(
                    f"Water level {water_level} is too high (max 10)")
            elif water_level < 1:
                raise WaterError(
                    f"Water level {water_level} is too low (min 1)")
            print(f"Watering {plant_name} - Success")
        except WaterError as error:
            print(f"Error: {error}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name: str, water_level: int,
                           sunlight_hour: int) -> None:
        """Validate plant conditions for water and sunlight."""
        try:
            if plant_name is None:
                raise ValueError("Plant name cannot be empty")
        except ValueError as error:
            print(f"Error: {error}")
            return
        try:
            if water_level > 10:
                raise ValueError(
                    f"Water level {water_level} is too high (max 10)")
            elif water_level < 1:
                raise ValueError(
                    f"Water level {water_level} is too low (min 1)")
        except ValueError as error:
            print(f"Error checking {plant_name}: {error}")
            return
        try:
            if sunlight_hour < 2:
                raise ValueError(
                    f"Sunlight hours {sunlight_hour} is too high (min 2)")
            elif sunlight_hour > 16:
                raise ValueError(
                    f"Sunlight hours {sunlight_hour} is too low (max 16)")
        except ValueError as error:
            print(f"Error: {error}")
            return
        print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    """Run a demo of the garden management system."""

    print("=== Garden Management System ===")
    demo_garden = GardenManager()
    demo_garden.water_tank = 8
    print("\nAdding plants to garden...")
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
            raise WaterError("Not enough water in the tank")
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    finally:
        print("System recovered and continuing...")

    print("\n Garden management system test complete!")


if __name__ == "__main__":
    test_plant_checks()
