#!/usr/bin/env python3


def check_temperature(temp_str):
    '''Check temperature and manage errors'''
    print(f"Testing temperature: {temp_str}")
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number", end="\n\n")
        return None

    if temp > 40:
        print(f"Error: {temp}°C is too hot for plants (max 40ªC)", end="\n\n")
        return None
    elif temp < 0:
        print(f"Error: {temp}°C is too cold for plants (min 0ªC)", end="\n\n")
        return None

    print(f"Temperature {temp}°C is perfect for plants!", end="\n\n")
    return temp


def test_temperature_input():
    '''Test a set of temperature values'''
    print("=== Garden Temperature Checker ===", end="\n\n")
    test_temp = ["25", "abc", "50", "-105"]

    for test in test_temp:
        check_temperature(test)
    print("All test completed - program didn't crash!")


test_temperature_input()
