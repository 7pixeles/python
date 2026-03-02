#!/usr/bin/env python3

def water_plants(plant_list: list):
    """Water each plant and ensure system cleanup."""
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Plant name is invalid")
            print(f"Watering {plant}...")
    except ValueError as error:
        print(f"Error: {error}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """Test watering with valid and invalid inputs."""
    print("=== Garden Watering System ===")
    print("\nTesting normal watering...")
    water_plants(plant_list=["tomato", "lettuce", "carrots"])
    print("\nTesting with error...")
    water_plants(plant_list=["tomato", None])

    print("\nCleanup always happens, even with erorrs!")


if __name__ == "__main__":
    test_watering_system()
