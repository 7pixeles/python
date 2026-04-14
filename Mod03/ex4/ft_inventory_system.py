#!/usr/bin/env python3

import sys
from typing import List, Dict


def parse_args(args: List[str]) -> Dict[str, int]:
    """Parse CLI args into an inventory dict.

    Parameters
    ----------
    args : list of str
        Items in 'name:quantity' format.

    Returns
    -------
    dict of str to int
        Parsed inventory with valid items.
    """
    inventory = {}

    for arg in args:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        name, s_qty = arg.split(":", 1)
        try:
            qty = int(s_qty)
        except ValueError as error:
            print(f"Quantity error for '{name}': {error}")
            continue

        if name not in inventory:
            inventory[name] = qty
        else:
            print(f"Redundant item '{name}' - discarding")
            continue

    if not inventory:
        print("Inventory is empty")

    return inventory


def statistics_inventory(inventory: Dict[str, int]) -> None:
    """Print percentage of each item in inventory.

    Parameters
    ----------
    inventory : dict of str to int
        Inventory with item quantities.
    """
    total = sum(inventory.values())

    for item, qty in inventory.items():
        percentage = (qty / total) * 100
        print(f"Item '{item}' represents {percentage:.1f}%")


def get_max_value(inventory: Dict[str, int]) -> None:
    """Print item with highest quantity.

    Parameters
    ----------
    inventory : dict of str to int
        Inventory with item quantities.
    """

    max_value = ""
    max_qty = 0

    for value, qty in inventory.items():
        if qty > max_qty:
            max_qty = qty
            max_value = value

    print(f"Item most abundant: {max_value} with quantity {max_qty}")


def get_min_value(inventory: Dict[str, int]) -> None:
    """Print item with lowest quantity.

    Parameters
    ----------
    inventory : dict of str to int
        Inventory with item quantities.
    """

    min_value = None
    min_qty = None

    for value, qty in inventory.items():
        if min_qty is None or qty < min_qty:
            min_value = value
            min_qty = qty

    print(f"Item least abundant: {min_value} with quantity {min_qty}")


if __name__ == "__main__":

    print("=== Inventory System Analysis ===")
    inventory = parse_args(sys.argv[1:])

    print("Got inventory:", inventory)
    print("Item list:", list(inventory.keys()))
    print(f"Total quantity of the {len(inventory)} items: ",
          f"{sum(inventory.values())}")

    statistics_inventory(inventory)
    get_max_value(inventory)
    get_min_value(inventory)

    inventory.update({"magic_item": 1})
    print("Updated inventory:", inventory)
