#!/usr/bin/env python3

# Importa un módulo mediante el uso de un alias
import alchemy


if __name__ == "__main__":
    print("=== Distillation 0 ===")

    print("Using: 'import alchemy' structure to access potions")

    print(f"Testing strength_potion: {alchemy.strength_potion()}")
    print(f"Testing heal alias: {alchemy.heal()}")
