'''Lambda: Si la función cabe en una sola expresión y solo se usa una vez,
Def: Si empieza a ser difícil de leer..'''

from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    '''
        Use sorted() with a lambda to sort by "power" level (descending)
        Parameters: Artifact = dict: {"name": str, "power": int, "type": str}
        Return: A sorted list
    '''

    return sorted(
        artifacts,
        key=lambda artifact: artifact["power"],
        reverse=True
    )


def power_filter(mages: list[dict[str, Any]],
                 min_power: int) -> list[dict[str, Any]]:
    '''
        filter(function, iterable): returns a special filter object
        Use filter() with a lambda to find mages with power >= min_power
        Parameters: Mage = dict: {"name": str, "power": int, "element": str}
        Return: A list of filtered mages
    '''

    return list(
        filter(
            lambda mage: mage["power"] >= min_power,
            mages
        )
    )


def spell_transformer(spells: list[str]) -> list[str]:
    '''
        map(function, iterable, ...):
            Applies a specified function to every item in an iterable.
            Returns an iterator with the transformed results
        Use map() with a lambda to add "* " prefix and " *" suffix
        Input: list of spell names (strings)
        Return: A list of transformed spell names
    '''

    return list(
        map(
            lambda spell: f"* {spell} *",
            spells
        )
    )


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    '''
        Use lambdas with max(), min() to find:
        - The mage with the highest power
        - The mage with the lowest power
        - The average power of all mages
        Parameters: Mage = dict: {"name": str, "power": int, "element": str}
        Return: A dictionary with the results
    '''

    max_power = max(
        mages,
        key=lambda mage: mage["power"]
    )

    min_power = min(
        mages,
        key=lambda mage: mage["power"]
    )

    average_power = round(
        sum(mage["power"] for mage in mages) / len(mages),
        2
    )

    return {
        "max_power": max_power,
        "min_power": min_power,
        "average_power": average_power
    }


def test_sorted(artifacts: list[dict[str, Any]]) -> None:

    sorted_artifacts = artifact_sorter(artifacts)

    print("\nTesting artifact sorter...")

    print(
        f"{sorted_artifacts[0]['name']} "
        f"({sorted_artifacts[0]['power']} power)"
        f" comes before "
        f"{sorted_artifacts[1]['name']} "
        f"({sorted_artifacts[1]['power']} power)"
    )


def test_transform(spells: list[str]) -> None:
    print("\nTesting spell transformer...")

    transformed_spells = spell_transformer(spells)
    print(" ".join(transformed_spells))


def test_stats(mages: list[dict[str, Any]]) -> None:
    print("\nTesting mages stats...")

    stats = mage_stats(mages)
    print(
        f"[Max power]\n"
        f"Name: {stats['max_power']['name']}\n"
        f"Power: {stats['max_power']['power']}\n"
        f"Element: {stats['max_power']['element']}\n"
    )

    print(
        f"[Min power]\n"
        f"Name: {stats['min_power']['name']}\n"
        f"Power: {stats['min_power']['power']}\n"
        f"Element: {stats['min_power']['element']}\n"
    )
    print(
        f"[Average power]\n"
        f"{stats.get("average_power")}"
    )


if __name__ == "__main__":

    artifacts = [
        {'name': 'Ice Wand', 'power': 76, 'type': 'focus'},
        {'name': 'Storm Crown', 'power': 81, 'type': 'focus'},
        {'name': 'Storm Crown', 'power': 117, 'type': 'accessory'},
        {'name': 'Ice Wand', 'power': 106, 'type': 'armor'}
        ]

    mages = [
        {'name': 'Casey', 'power': 55, 'element': 'fire'},
        {'name': 'Rowan', 'power': 87, 'element': 'lightning'},
        {'name': 'River', 'power': 98, 'element': 'light'},
        {'name': 'Zara', 'power': 92, 'element': 'water'},
        {'name': 'Sage', 'power': 79, 'element': 'water'}
        ]

    spells = [
        'fireball',
        'darkness',
        'tornado',
        'blizzard']

    test_sorted(artifacts)
    test_transform(spells)
    test_stats(mages)
