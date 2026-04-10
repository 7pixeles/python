#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    """
    Execute faulty operations to trigger different exceptions.

    Parameters
    ----------
    operation_number : int
        Determines which error to trigger.
    """
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("non_existent_file.txt")
    elif operation_number == 3:
        "text" + 5
    else:
        print("Operation completed successfully")


def test_error_types() -> None:
    """
    Test different exception types and ensure program continues.
    """
    print("=== Garden Error Types Demo ===")

    for n in range(8):
        print(f"Testing operation {n}...")
        try:
            garden_operations(n)
        except ValueError as error:
            print(f"Caught ValueError: {error}")
        except ZeroDivisionError as error:
            print(f"Caught ZeroDivisionError: {error}")
        except FileNotFoundError as error:
            print(f"Caught FileNotFoundError: {error}")
        except TypeError as error:
            print(f"Caught TypeError: {error}")

    print("\nTesting multiple catch...")
    try:
        garden_operations(0)
    except (ValueError, TypeError):
        print("Caught multiple types")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
