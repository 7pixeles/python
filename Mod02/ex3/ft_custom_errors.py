#!/usr/bin/env python3

class GardenError(Exception):
    '''
    Base class for all garden-related errors.

    Parameters
    ----------
    message : str, optional
        Error message
    '''
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    '''
    Exception for plant-related problems.

    Parameters
    ----------
    message : str, optional
        Error message.
    '''
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)


class WaterError(GardenError):
    '''
    Exception for watering problems.

    Parameters
    ----------
    message : str, optional
        Error message.
    '''
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)


def check_plant() -> None:
    '''
    Raise a PlantError to simulate a plant issue.
    '''
    raise PlantError("The tomato plant is wilting!")


def check_water() -> None:
    '''
    Raise a WaterError to sumulate a water issue.
    '''
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    '''
    Demonstrate custom error handling behavior.
    '''
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        check_plant()
    except PlantError as error:
        print(f"Caught PlantError: {error}")

    print("\nTesting WaterError...")
    try:
        check_water()
    except WaterError as error:
        print(f"Caught WaterError: {error}")

    print("\nTesting catching all garden errors...")
    try:
        check_plant()
        check_water()
    except GardenError as error:
        print(f"Caught GardenError: {error}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()