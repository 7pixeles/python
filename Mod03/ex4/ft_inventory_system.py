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

    if not inventory:
        print("Inventory is empty")

    return inventory


def categorize_items(inventory: dict) -> dict:
    categories = {
        "Moderate": {},
        "Scarce": {},
        "Abundant": {}
    }
    for value, qty in inventory.items():
        if qty <= 4:
            categories["Scarce"].update({value: qty})
        elif qty >= 5 and qty < 10:
            categories["Moderate"].update({value: qty})
        else:
            categories["Abundant"].update({value: qty})
    return categories


def current_invent(inventory: dict) -> None:
    total = sum(inventory.values())
    for item, qty in inventory.items():
        percentage = (qty / total) * 100
        unit_label = "unit" if qty == 1 else "units"
        print(f"{item}: {qty} {unit_label} ({percentage:.1f}%)")


def get_max_value(inventory: dict) -> None:
    max_value = ""
    max_qty = 0
    for value, qty in inventory.items():
        if qty > max_qty:
            max_qty = qty
            max_value = value
    unit_label = "unit" if max_qty == 1 else "units"
    print(f"Most abundant: {max_value} ({max_qty} {unit_label})")


def get_min_value(inventory: dict) -> None:
    min_value = None
    min_qty = None
    for value, qty in inventory.items():
        if min_qty is None or qty < min_qty:
            min_value = value
            min_qty = qty
    unit_label = "unit" if min_qty == 1 else "units"
    print(f"Least abundant: {min_value} ({min_qty} {unit_label})")


def get_restock(inventory: dict) -> list:
    need_restock = []
    for item, qty in inventory.items():
        if qty < 2:
            need_restock.append(item)
    return need_restock


def is_in_inventory(inventory: dict, word: str) -> str:
    if word in inventory:
        return ("True")
    else:
        return ("False")


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
    print(f"Sample lookup - '{word}' in inventory: {is_in_inventory(inventory, word)}")