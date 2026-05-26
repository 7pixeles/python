#!/usr/bin/env python3

# importamos en la raíz de /alchemy,
# por lo que la función queda expuesta directamente
import alchemy

if __name__ == "__main__":
    print("=== Transmutation 2 ===")
    print("Import alchemy module only")
    print(f"Testing lead to gold: {alchemy.lead_to_gold()}")
