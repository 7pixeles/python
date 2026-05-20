#!/usr/bin/env python3

# Debemos acceder usando todo el path
import alchemy.transmutation.recipes

print("=== Transmutation 0 ===")

print("Using file alchemy/transmutation/recipes.py directly")

print(f"Testing lead to gold: "
      f"{alchemy.transmutation.recipes.lead_to_gold()}")
