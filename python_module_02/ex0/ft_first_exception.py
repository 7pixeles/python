#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")

    test_temp = ["25", "abc"]

    for value in test_temp:
        print(f"Input data is '{value}'")
        try:
            temp = input_temperature(value)
            print(f"Temperature is now {temp} ºC\n")
        except ValueError as error:
            print(f"Caught input_temperature error: {error} \n")

    print("All test completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
