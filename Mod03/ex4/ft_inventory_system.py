#!/usr/bin/env python3

import sys


def parse_args(args: list) -> dict:
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

    return inventory

def current_invent(inventory: dict) -> None:
    total = sum(inventory.values())
    for item, qty in inventory.items():
        percentage = (qty / total) * 100
        print(f"{item}: {qty} units ({percentage:.1f}%)")

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory = parse_args(sys.argv[1:])
    
    print("Total items in inventory:", sum(inventory.values()))
    print("Unique item types:", len(inventory))
    
    print("\n=== Current Inventory ===")
    current_invent(inventory)

    print("\n=== Inventory Statistics ===")
