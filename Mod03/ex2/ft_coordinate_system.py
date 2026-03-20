#!/usr/bin/env python3
"""
Parse 3D coordinates from the command line and compute distances.

Provides utilities to convert a string "x,y,z" into a tuple and
calculate the Euclidean distance between two 3D points.
"""
import sys
import math


def parse_args(arg: str) -> tuple:
    """Convert a string 'x,y,z' into a tuple of three integers.

    Raises:
        ValueError: If the input does not contain exactly three values.
    """
    parts = arg.split(",")
    if len(parts) != 3:
        raise ValueError("Coordinates must be x,y,z")
    coord = []
    for value in parts:
        coord.append(int(value))
    return tuple(coord)


def calc_distance(dest: tuple, origin: tuple) -> float:
    """Return the Euclidean distance between two 3D coordinate tuples."""

    x1, y1, z1 = origin
    x2, y2, z2 = dest
    dist = float(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))
    return dist


def unpacked_tuple(demo: tuple):
    """Demonstrate tuple unpacking using a 3D coordinate."""

    print("\nUnpacking demonstration:")
    x, y, z = demo
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    origin = (0, 0, 0)
    dest = (10, 20, 5)
    print(f"Position created: {dest}")
    calc_distance(origin, dest)

    if len(sys.argv) != 2:
        print("\nPlease, enter a validate coordinate: 'x,y,z'")
        sys.exit(1)

    print(f'\nParsing cordinates: "{sys.argv[1]}"')
    try:
        coord = parse_args(sys.argv[1])
        print(f"Parsed position: {coord}")
        print(f"Distance between {origin} and {dest}:",
              "{calc_distance(origin, coord):.2f}")
        unpacked_tuple(coord)
    except ValueError as error:
        print(f'Parsing invalid coordinates: "{sys.argv[1]}"')
        print("Error parsing coordinates:", error)
        print("Error details - Type:",
              type(error).__name__,
              "Args:", error.args)
