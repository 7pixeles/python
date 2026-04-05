#!/usr/bin/env python3

class Plant:
    """
    Base class representing a plant.

    Parameters
    ----------
    name : str
        Plant name.
    height : float
        Height in centimeters.
    age : int
        Age in days.
    """

    class _Stats:
        '''
        Internal class to track method usage statistics
        '''
        def __init__(self):
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self):
            '''Print Statistics'''
            print(f"Stats: {self.grow_calls} grow, "
                  f"{self.age_calls} age, "
                  f"{self.show_calls} show")

    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age
        self._stats = self._Stats()

    def grow(self, value: float) -> None:
        '''Increase plant height'''
        self.height += value
        self._stats.grow_calls += 1

    def age_up(self, value: int) -> None:
        '''Increase plant age'''
        self.age += value
        self._stats.age_calls += 1

    def show(self) -> None:
        '''Display plant information'''
        print(f"{self.name}: {self.height}cm, {self.age} days old.")
        self._stats.show_calls += 1

    def display_stats(self) -> None:
        '''Display plant statistics'''
        self._stats.display()

    @staticmethod
    def is_older(age: int) -> bool:
        '''
        Check if age exceeds one year.

        Parameters
        ----------
        age : int
            Age in days.

        Returns
        -------
        bool
            True if age > 365 days
        '''
        return age > 365

    @classmethod
    def anonymous(cls):
        '''
        Create an anonymous plant.

        Returns:
        -------
        Plant
            Default plant instance
        '''
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    '''Flower plant type'''

    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self):
        '''Make the flower bloom'''
        print(f"[asking the {self.name.lower()} to bloom]")
        self.is_blooming = True

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self.is_blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    '''Tree plant type'''

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade_calls = 0

    def produce_shade(self) -> None:
        '''Produce shade'''
        print(f"[asking the {self.name.lower()} to produce shade]")
        print(f"Tree {self.name} now produces a shade of "
              f"{self.height}cm long and "
              f"{self.trunk_diameter}cm wide.")
        self.shade_calls += 1

    def display_stats(self) -> None:
        super().display_stats()
        print(f"{self.shade_calls} shade")


class Seed(Flower):
    '''Flower that produces seeds'''

    def __init__(self, name: str, height: float, age: int,
                 color: str):
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self):
        super().bloom()
        self.seeds = 42

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")


def show_plant_stats(plant: Plant) -> None:
    '''
    Display statistics for any plant.

    Parameters:
    ----------
    plant : Plant
        Plant instance.
    '''

    print(f"[statistics for {plant.name}]")
    plant.display_stats()


if __name__ == "__main__":
    print("=== Garden Statistics ===")

    print("=== Check year-old")
    print("Is 30 days more than a year? ->",
          Plant.is_older(30))
    print("Is 400 days more than a year? ->",
          Plant.is_older(400))

    print("\n=== Flower")
    flwr = Flower("Rose", 15.0, 10, "red")
    flwr.show()
    show_plant_stats(flwr)

    flwr.grow(8)
    flwr.bloom()
    flwr.show()
    show_plant_stats(flwr)

    print("\n=== Tree")
    tr = Tree("Oak", 200.0, 365, 5.0)
    tr.show()
    show_plant_stats(tr)

    tr.produce_shade()
    show_plant_stats(tr)

    print("\n=== Seed")
    sd = Seed("Sunflower", 80.0, 45, "yellow")
    sd.show()

    sd.grow(30)
    sd.age_up(20)
    sd.bloom()
    sd.show()
    show_plant_stats(sd)

    print("\n=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    show_plant_stats(unknown)
