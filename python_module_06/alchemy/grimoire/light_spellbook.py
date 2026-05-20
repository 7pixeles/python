#!/usr/bin/env python3

from .light_validator import validate_ingredients


# Devuelve ingredientes válidos
def light_spell_allowed_ingredients() -> list[str]:
    return ("earth", "air", "fire", "water")


# Uso del validador
def light_spell_record(
        spell_name: str,
        ingredients: str
        ) -> str:
    validation = validate_ingredients(ingredients)

    return f"Spell recorded: {spell_name} ({validation})"
