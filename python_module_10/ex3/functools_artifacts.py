from typing import Any, Callable
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul


operations: dict[str, Callable[[int, int], int]] = {
    "add": add,
    "multiply": mul,
    "max": max,
    "min": min
}


def spell_reducer(spells: list[int], operation: str) -> int:
    """
    Reduce spell power.
    Support operations: add, multiply, max, min
    Return: the final reduced value
        if spells is empty, return 0
        if operation is unknown, handle the error
    """
    if not spells:
        return 0

    if operation not in operations:
        raise ValueError("Unknown operation")

    return reduce(operations[operation], spells)


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str]
) -> dict[str, Callable[[str], str]]:
    """
    Create partial applications.
    Take a base enchantment function with concrete signature
    Use functool.partial to create 3 specialized versions
    Each version pre-filling power=50 and the element
    partial fixed two first arguments
    """
    return {
        "fire": partial(base_enchantment, 50, "fire"),
        "ice": partial(base_enchantment, 50, "ice"),
        "lightning": partial(base_enchantment, 50, "lightning")
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """
    Computes Fibonacci numbers using memoization.

    Args:
        n: Index of Fibonacci sequence.

    Returns:
        Fibonacci number at position n.
    """
    if n < 2:
        return n

    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    """
    Returns a type-dispatched spell function.

    The returned function behaves differently depending on input type:
    - int -> damage spell
    - str -> enchantment
    - list -> multi-cast
    - other -> unknown spell type
    """

    @singledispatch
    def spell(value: Any) -> str:
        return "Unknown spell type"

    @spell.register
    def _(value: int) -> str:
        return f"Damage spell: {value} damage"

    @spell.register
    def _(value: str) -> str:
        return f"Enchantment: {value}"

    @spell.register
    def _(value: list) -> str:
        return f"Multi-cast: {len(value)} spells"

    return spell


if __name__ == "__main__":

    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]

    print("Sum:", spell_reducer(spells, "add"))
    print("Product:", spell_reducer(spells, "multiply"))
    print("Max:", spell_reducer(spells, "max"))
    print("Min:", spell_reducer(spells, "min"))

    print("\nTesting partial enchanter...")

    def enchantment(power: int, element: str, target: str) -> str:
        return f"{element} attack with {power} power on {target}"

    enchantments = partial_enchanter(enchantment)
    print(enchantments["fire"]("dragon"))
    print(enchantments["ice"]("goblin"))
    print(enchantments["lightning"]("wizard"))

    print("\nTesting memoized fibonacci...")
    print("Fib(0):", memoized_fibonacci(0))
    print("Fib(1):", memoized_fibonacci(1))
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))

    print("\nCache info:")
    print(memoized_fibonacci.cache_info())

    print("\nTesting spell dispatcher...")

    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher([1, 2, 3]))
    print(dispatcher(3.14))
