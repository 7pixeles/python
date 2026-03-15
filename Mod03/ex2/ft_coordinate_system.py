#!/usr/bin/env python3

import sys
import math


def parse_args(arg: str) -> tuple:
    parts = arg.split(",")
    if len(parts) != 3:
        raise ValueError("Coordinates must be x,y,z")
    coord = []
    for value in parts:
        coord.append(int(value))
    return tuple(coord)


def calc_distance(dest: tuple, origin: tuple):
    x1, y1, z1 = origin
    x2, y2, z2 = dest
    dist = float(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))
    print(f"Distance between {origin} and {dest}: {dist:.2f}")


def unpacked_tuple(demo: tuple):
    print("\nUnpacking demonstration:")
    x, y, z = demo
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    origin = (0, 0, 0)
    pos = (10, 20, 5)
    print(f"Position created: {pos}")
    calc_distance(origin, pos)

    if len(sys.argv) != 2:
        print("Usage: script 'x,y,z'")
        sys.exit(1)

    print(f'\nParsing cordinates: "{sys.argv[1]}"')
    try:
        coord = parse_args(sys.argv[1])
        print(f"Parsed position: {coord}")
        calc_distance(origin, coord)
        unpacked_tuple(coord)
    except ValueError as error:
        print(f'Parsing invalid coordinates: "{sys.argv[1]}"')
        print("Error parsing coordinates:", error)
        print("Error details - Type:",
              type(error).__name__,
              "Args:", error.args)
