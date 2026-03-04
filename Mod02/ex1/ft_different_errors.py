#!/usr/bin/env python3

def garden_operations(n_plants: int, plants: dict, target_height: str,
                      file: str | None) -> None:
    """
    Performs garden-related operations that may trigger common
    Python exceptions.

    Parameters:
        n_plants (int | str): Number of plants used to calculate
            the average height. May raise ValueError if it cannot
            be converted to int.
        plants (dict): Dictionary mapping plant names to heights.
        target_height (str): Plant name to compare against the
            average. May raise KeyError if not found.
        file (str | None): Optional filename where the result will
            be written. May raise FileNotFoundError if missing.

    Raises:
        ValueError: If n_plants cannot be converted to int.
        ZeroDivisionError: If n_plants is zero.
        KeyError: If target_height is not in plants.
        FileNotFoundError: If file is provided but does not exist.
    """
    total_height = 0
    for plant in plants:
        total_height += plants[plant]
    average = total_height / int(n_plants)
    if average > plants[target_height]:
        message = "Target is below the average"
    else:
        message = "Target is above the average"
    if file:
        a = open(file, "r+")
        print(message, file=a)
    else:
        print(message)


def test_error_types() -> None:
    """
    Demonstrates different Python exception types and shows that
    the program continues running after handling each error.
    """
    print("=== Garden Error Types Demo ===", end="\n")
    plants = {"Rose": 25, "Sunflower": 80, "Cactus": 15}
    print("\nTesting ValueError...")
    try:
        garden_operations("abc", plants, "Rose", None)
    except ValueError as error:
        print(f"Caught ValueError: {error}")

    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations("0", plants, "Rose", None)
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}")

    print("\nTesting FileNotFoundError...")
    try:
        garden_operations("3", plants, "Rose", "example.txt")
    except FileNotFoundError as error:
        print(f"Caught FileNotFoundError: {error}")

    print("\nTesting KeyError...")
    try:
        garden_operations("3", plants, "Tulip", None)
    except KeyError as error:
        print(f"Caught KeyError: {error}")

    print("\nTesting multiple errors together...")
    try:
        garden_operations("2", plants, "plant_not_found", None)
    except (KeyError, ValueError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
