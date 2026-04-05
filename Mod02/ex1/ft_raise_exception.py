#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    '''
    Convert a string to an integer temperature

    Parameters
    ----------
    temp_str : str
        Input temperature as string

    Returns
    -------
    int
        Converted temperature

    Raises:
    ------
    ValueError
        if conversion fails
    '''
    temp = int(temp_str)

    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")

    return temp


def test_temperature() -> None:
    """
    Test temperature validation with multiple inputs.
    """
    print("=== Garden Temperature Checker ===\n")

    tests = ["25", "abc", "100", "-50"]

    for value in tests:
        print(f"Input data is '{value}'")
        try:
            temp = input_temperature(value)
            print(f"Temperature is now {temp} ºC\n")
        except ValueError as error:
            print(f"Caught input_temperature error: {error} \n")

    print("All test completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
