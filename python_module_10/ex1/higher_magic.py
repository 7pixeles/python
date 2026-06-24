from typing import Callable

Spell = Callable[[str, int], str]


def yeet(target: str, power: int) -> str:
    return f"Yeet launches {target} {power} feet into the air (╯°□°）╯"


def bonk(target: str, power: int) -> str:
    return f"Bonk deals {power} damage and embarrasses {target} (｡•́︿•̀｡)"


def confuse(target: str, power: int) -> str:
    return (
        f"Confuse causes {target} to forget what "
        f"they were doing for {power} seconds"
    )


def enough_power(target: str, power: int) -> bool:
    return power >= 20


def spell_combiner(
        spell1: Spell, spell2: Spell
) -> Callable[[str, int], tuple[str, str]]:

    ''' Combine two spells
        Return: a new function that calls
                both spells with the same arguments.
        The combined spell should return a tuple of both results
    '''

    return lambda target, power: (
        spell1(target, power),
        spell2(target, power)
    )


def power_amplifier(base_spell: Spell, multiplier: int) -> Spell:
    ''' Amplify spell power:
        Return: a function with the same signature as the original spell
        Return: a new spell where the power is multiplied before casting.

        Example: mega_fireball = power_amplifier(fireball, 3)
    '''

    return lambda target, power: base_spell(target, power * multiplier)


def conditional_caster(
        condition: Callable[[str, int], bool],
        spell: Spell
) -> Callable[[str, int], str]:

    ''' Cast spell conditionally:
        Return: a new spell that only casts if a condition is True.
            If condition fails, return "Spell fizzled"
            Both condition and spell receive the same arguments
    '''

    return lambda target, power: (
        spell(target, power)
        if condition(target, power)
        else "Spell fizzled"
    )


def spell_sequence(
        spells: list[Spell]
) -> Callable[[str, int], list[str]]:
    ''' Create spell sequence:
        Return: a function that casts all spells in order
            Each spell receives the same arguments
        Return: a list of all spell results
    '''

    return lambda target, power: [
        spell(target, power) for spell in spells
    ]


if __name__ == "__main__":

    print("\nTesting spell combiner...")
    combo = spell_combiner(yeet, bonk)
    result1, result2 = combo("Dragon", 10)
    print(f"Combined spell result:\n"
          f"- {result1}\n- {result2}")

    print("\nTesting power amplifier...")
    mega = power_amplifier(confuse, 3)
    original_power = 10
    amplified_power = original_power * 3
    print(
        f"Original: {original_power}, "
        f"Amplified: {amplified_power}"
    )

    print("\nTesting conditional caster...")
    conditional = conditional_caster(enough_power, yeet)
    print(conditional("Dragon", 5))
    print(conditional("Dragon", 30))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([yeet, bonk, confuse])
    for result in sequence("Dragon", 10):
        print(result)
