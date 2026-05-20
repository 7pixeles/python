#!/usr/bin/env python3

# import relativo -> .. (sube dos niveles)
# import absoluto -> busca desde la raí<
from elements import create_fire
from ..elements import create_air
from ..potions import strength_potion


def lead_to_gold() -> str:
    return (
        f"Recipe transmuting Lead to Gold: "
        f"brew '{create_air()}' "
        f"and '{strength_potion()}' "
        f"mixed with '{create_fire()}'"
    )
