#!/usr/bin/env python3

# Busca elements.py dentro del MISMO paquete
# Intencionadamente, solo exportamos un solo módulo
from . import elements
from .potions import strength_potion, healing_potion as heal
from .transmutation import lead_to_gold

# Crea un alias para que se pueda usar este elemento directamente (alembic4)
# Create_earth = elements.create_earth
create_air = elements.create_air

__all__ = ["create_air",
           "strength_potion",
           "heal",
           "lead_to_gold"]
