#!/usr/bin/env python3

# Acceso a una sola función del paquete alchemy
from alchemy.elements import create_air

print("=== Alembic 2 ===")
print("Accessing alchemy/elements.py using 'from ... import ...' structure")
print(f"Testing create_air: {create_air()}")
