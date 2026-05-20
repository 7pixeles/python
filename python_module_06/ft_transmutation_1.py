#!/usr/bin/env python3

# Dado que en _init_ importamos, "subimos" un nivel la función
# y podemos usarla como alchemy.transmutation.lead_to_gold()
import alchemy.transmutation

print("=== Transmutation 1 ===")
print("Import transmutation module directly")

print(
    "Testing lead to gold: "
    f"{alchemy.transmutation.lead_to_gold()}"
)
