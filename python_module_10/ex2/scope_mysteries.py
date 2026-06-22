from typing import Callable


def mage_counter() -> Callable[[], int]:
    ''' Create a counting closure:
        Return: a function that counts how many times its been called
    '''
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    ''' Create power accumulator
        Return:
            A function that accumulates power over time
            Return the new total power after each addition
        Start with initial__power as the base
    '''
    total_power = initial_power

    def accumulator(amount: int) -> int:
        nonlocal total_power
        total_power += amount
        return total_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    '''Create enchantment functions
        Return: A function that applies the specified enchantment
                Takes an item name an returns enchanted description
        Format: "enchantment_type iten_name
        Each factory creates functions with diffeerent enchantment types
    '''
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict[str, Callable[..., object]]:
    '''
    Create a memory management system
    Return: dict with "store" and "recall" functions
            - "store": takes (key, value) and stores the memory
            - "recall": takes (key) and returns stored value
                        or "Memory not found"
    '''
    memory = {}

    def store(key: str, value: object) -> None:
        memory[key] = value

    def recall(key: str) -> object:
        if key in memory:
            return memory[key]
        return "Memory not found"
    return {
        "store": store,
        "recall": recall
        }


if __name__ == "__main__":

    print("Testing mage counter...")
    counter_a = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")

    counter_b = mage_counter()
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell acumulator...")
    power = spell_accumulator(100)
    print(f"Base 100, add 20: {power(20)}")
    print(f"Base 100, add 30: {power(30)}")

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    print("Store 'secret' = 42")
    vault["store"]("secret", 42)
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")
