#!/usr/bin/env python3

COLORS = ["red", "white", "yellow", "pink", "purple", "orange"]

class Plant:
    '''Base class for all garden items'''
    def __init__(self, name:str, height:int):
        self.name = name
        self.height = height

    def grow(self, value):
        height = height + value
        print(f"{self.name} grew {value} cm")

class FLoweringPlant(Plant):
    '''Plant specialized with flowering capabilities

        FloweringPlant IS A Plant
        Plant.__init__()
        ↓
        FloweringPlant add color & bloom
    '''
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        index = self.height % len(COLORS)
        self.color = color
        self.is_blooming = True

class PrizeFlower(FLoweringPlant):
    '''The highest tier in the plant family tree'''
    def __init__(self, name: str, height: int, color:str, points: int ):
        super().__init__(name, height, color)

def GardenManager():
    '''
    - Guarda varios jardines
    - Cuántos jardines hay
    - Puede operar sobre todos
        GardenManager
        ├── Garden A
        ├── Garden B
        ├── Garden C
    '''
    def GardenStats():
        '''
        GardenStats: Clase anidada. Calculate statistics of Garden
            - Contar plantas
            - Calcular estadísticas
            - Sumar crecimiento
        '''

