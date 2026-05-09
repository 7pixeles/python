#!/usr/bin/env python3

import math


def get_player_pos() -> tuple:
    while True:
        user_input = input(
                            "Enter new coordinates "
                            "as floats in format 'x,y,z': ")

        try:
            x, y, z = user_input.split(",")

            coords = (
                float(x.strip()),
                float(y.strip()),
                float(z.strip())
            )

            return coords

        except ValueError as error:
            print(f"Invalid input: {error}")


def calc_distance(dest: tuple, origin: tuple) -> float:
    x1, y1, z1 = origin
    x2, y2, z2 = dest
    dist = float(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))
    return dist


if __name__ == "__main__":
    print("=== Game Coordinate System ===")

    print("\nGet a first set of coordinates")
    coord1 = get_player_pos()
    print(f"Got a first tuple: {coord1}")
    x, y, z = coord1
    print(f"It includes: X={x}, Y={y}, Z={z}")

    dist_center = calc_distance(coord1, (0, 0, 0))
    print(f"Distance to center: {dist_center:.4f}")

    print("\nGet a second set of coordinates")
    coord2 = get_player_pos()

    dist_between = calc_distance(coord2, coord1)
    print(f"Distance between the 2 sets of coordinates: {dist_between:.4f}")
