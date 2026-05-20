#!/usr/bin/env python3

# Importa un módulo mediante el uso de un alias
from alchemy.potions import strength_potion, healing_potion as heal

print("=== Distillation 0 ===")

print("Using: 'import alchemy' structure to access potions")

print(f"Testing strength_potion: {strength_potion()}")
print(f"Testing heal alias: {heal()}")
