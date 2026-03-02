#!/usr/bin/env python3

def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: str):
    """Validate inputs and report plant health status."""
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
        print(f"Error: {error}")
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


def test_plant_checks():
    """Run tests with valid and invalid plant data."""
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    check_plant_health("tomato", 4, 6)
    print("\nTesting plant name...")
    check_plant_health(None, 16, 22)
    print("\nTesting bad water level...")
    check_plant_health("tomato", 25, 12)
    print("\nTesting bad sunlight hours...")
    check_plant_health("tomato", 8, 1)


if __name__ == "__main__":
    test_plant_checks()
