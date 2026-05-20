#!/usr/bin/env python3

def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import (
        light_spell_allowed_ingredients
        )

    allowed = light_spell_allowed_ingredients()

    low_ingredients = ingredients.lower()

    is_valid = any(ingredient in low_ingredients
                   for ingredient in allowed)

    status = "VALID" if is_valid else "INVALID"

    return f"{ingredients} - {status}"
