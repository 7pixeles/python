#!/usr/bin/env python3
"""
Inventory management and analysis system.

Provides utilities to parse item quantities, categorize items,
display inventory statistics, and suggest restocking.
"""
import sys
from typing import List, Dict


def parse_args(args: List[str]) -> Dict[str, int]:
    """Parse command-line arguments into an inventory dictionary.

    Args:
        args: List of strings formatted as 'item:quantity'.

    Returns:
        Dictionary mapping item names to total quantities.
    """
    inventory = {}

    for arg in args:
        if ":" not in arg:
            continue
        item, qty_str = arg.split(":", 1)
        try:
            qty = int(qty_str)
        except ValueError:
            print("Invalid quantity for item")
            continue
        current_qty = inventory.get(item, 0)
        inventory[item] = current_qty + qty

    if not inventory:
        print("Inventory is empty")

    return inventory


def categorize_items(inventory: Dict[str, int]) -> Dict[str, Dict[str, int]]:
    """Categorize inventory items by quantity levels.

    Args:
        inventory: Dictionary of item names to quantities.

    Returns:
        Dictionary with categories 'Scarce', 'Moderate', 'Legendary'.
    """
    categories = {
        "Moderate": {},
        "Scarce": {},
        "Legendary": {}
    }
    for value, qty in inventory.items():
        if qty <= 4:
            categories["Scarce"].update({value: qty})
        elif qty >= 5 and qty < 10:
            categories["Moderate"].update({value: qty})
        else:
            categories["Legendary"].update({value: qty})
    return categories


def current_invent(inventory: Dict[str, int]) -> None:
    """Print current inventory with quantities and percentage of total."""

    total = sum(inventory.values())
    for item, qty in inventory.items():
        percentage = (qty / total) * 100
        unit_label = "unit" if qty == 1 else "units"
        print(f"{item}: {qty} {unit_label} ({percentage:.1f}%)")


def get_max_value(inventory: Dict[str, int]) -> None:
    """Print the item with the highest quantity in the inventory."""
    max_value = ""
    max_qty = 0
    for value, qty in inventory.items():
        if qty > max_qty:
            max_qty = qty
            max_value = value
    unit_label = "unit" if max_qty == 1 else "units"
    print(f"Most Legendary: {max_value} ({max_qty} {unit_label})")


def get_min_value(inventory: Dict[str, int]) -> None:
    """Print the item with the lowest quantity in the inventory."""

    min_value = None
    min_qty = None
    for value, qty in inventory.items():
        if min_qty is None or qty < min_qty:
            min_value = value
            min_qty = qty
    unit_label = "unit" if min_qty == 1 else "units"
    print(f"Least Legendary: {min_value} ({min_qty} {unit_label})")


def get_restock(inventory: Dict[str, int]) -> List[str]:
    """Return a list of items that need restocking (quantity < 2)."""

    return [item for item, qty in inventory.items() if qty < 2]


def is_in_inventory(inventory: Dict[str, int], word: str) -> str:
    """Check if an item exists in the inventory.
    Returns:
        'True' if the item exists, 'False' otherwise.
    """
    return "True" if word in inventory else "False"


if __name__ == "__main__":
    inventory = parse_args(sys.argv[1:])

    print("=== Inventory System Analysis ===")
    print("Total items in inventory:", sum(inventory.values()))
    print("Unique item types:", len(inventory))

    print("\n=== Current Inventory ===")
    current_invent(inventory)

    print("\n=== Inventory Statistics ===")
    get_max_value(inventory)
    get_min_value(inventory)

    print("\n=== Item Categories ===")
    categories = categorize_items(inventory)
    print("Moderate:", categories["Moderate"])
    print("Scarce:", categories["Scarce"])

    print("\n=== Management Suggestions ===")
    restock_items = get_restock(inventory)
    print("Restock needed:", ", ".join(restock_items))

    print("\n=== Dictionary Properties Demo ===")
    word = "sword"
    print("Dictionary keys:", ", ".join(inventory.keys()))
    print("Dictionary values:", *list(inventory.values()))
    print(f"Sample lookup - '{word}' in inventory:",
          "{is_in_inventory(inventory, word)}")
