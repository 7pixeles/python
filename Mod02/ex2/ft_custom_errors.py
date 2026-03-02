#!/usr/bin/env python3

class GardenError(Exception):
    """Base class for all garden-related errors."""
    def __init__(self, message: str):
        super().__init__(message)


class PlantError(GardenError):
    """Error related to plant-specific problems."""
    def __init__(self, message: str):
        super().__init__(message)


class WaterError(GardenError):
    """Error related to watering issues."""
    def __init__(self, message: str):
        super().__init__(message)


def check_plants(status):
    """Raise PlantError if plant status indicates a problem."""
    if status == "wilting":
        raise PlantError("The tomato plant is wilting!")


def check_water(level):
    """Raise WaterError if water level is below threshold."""
    if level < 10:
        raise WaterError("Not enough water in the tank!")


def main():
    """Demonstrate custom garden error handling."""
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError")
    try:
        check_plants("wilting")
    except PlantError as error:
        print(f"Caught PlantError: {error}")

    print("\nTesting WaterError")
    try:
        check_water(5)
    except WaterError as error:
        print(f"Caught WaterError: {error}")

    print("\nTesting catching all garden errors...")
    try:
        check_plants("wilting")
    except GardenError as error:
        print(f"Caught a garden error: {error}")

    try:
        check_water(0)
    except GardenError as error:
        print(f"Caught a garden error: {error}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
