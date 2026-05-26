#!/usr/bin/env python3

# Debemos acceder usando todo el path
import alchemy.transmutation.recipes


if __name__ == "__main__":
    print("=== Transmutation 0 ===")

    print("Using file alchemy/transmutation/recipes.py directly")

    print("Testing lead to gold:", end=" ")
    print(alchemy.transmutation.recipes.lead_to_gold())
