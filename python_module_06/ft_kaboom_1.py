#!/usr/bin/env python3


if __name__ == "__main__":

    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")

    # Import dentro de main, no da error de flake8
    from alchemy.grimoire.dark_spellbook import dark_spell_record

    print(f"{dark_spell_record('Fantasy', ' Earth, water and air')}")
