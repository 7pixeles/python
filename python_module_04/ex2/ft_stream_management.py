#!/usr/bin/env python3

import sys


def transform_data(file_name: str) -> str:
    result = ""
    file = None

    file = open(file_name, "r")
    for line in file:
        result += line.rstrip("\n") + "#\n"

    file.close()
    return result


def read_archive(file_name: str) -> bool:
    file = None
    success = True

    try:
        file = open(file_name, "r")
        content = file.read()
        print(content)

    except Exception as error:
        sys.stderr.write(
            f"[STDERR] Error opening file '{file_name}': {error}\n")
        success = False

    finally:
        if file:
            file.close()
            print("\n---\n")
            print(f"File '{file_name}' closed")

    return success


if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===")
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <filename.txt>")
        sys.exit(1)

    file_name = sys.argv[1]
    print(f"Accessing file '{file_name}'")
    print("\n---\n")
    if not read_archive(file_name):
        sys.exit(1)

    print("\nTransform data:")
    print("---\n")
    transformed_content = transform_data(file_name)
    print(transformed_content, end="")
    print("\n---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()

    new_name = sys.stdin.readline().rstrip("\n")

    if new_name:
        print(f"Saving data to '{new_name}'")
        file = None
        try:
            file = open(new_name, "w")
            file.write(transformed_content)
            print(f"Data saved in file '{new_name}'.")
        except Exception as error:
            sys.stderr.write(
                f"[STDERR] Error opening file '{new_name}': {error}\n")
            sys.stderr.write("Data not saved\n")
        finally:
            if file:
                file.close()
    else:
        print("Not saving data.")
