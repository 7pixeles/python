import time
from collections.abc import Callable
from functools import wraps


# Recibe una función
def spell_timer(func: Callable) -> Callable:
    '''
    Time execution decorator:
    Create a decorator that measures function execution time.
    Return: the original function's result
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")

        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(
            f"Spell completed in "
            f"{end - start:.3f} seconds"
        )
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    '''
    Parameterized validation decorator:
    Create a decorator factory that validates power levels.
    '''

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = args[-1]

            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"

        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    '''
    Retry decorator if spells failed
    '''
    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args, **kwargs):

            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)

                except Exception:
                    if attempt < max_attempts - 1:
                        print(
                            "Spell failed, retrying..."
                            f" ({attempt + 1}/{max_attempts})"
                        )

            return (
                "Spell casting failed after "
                f"{max_attempts} attempts"
            )

        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (
            len(name) >= 3
            and name.replace(" ", "").isalpha()
        )

    @power_validator(10)
    def cast_spell(
        self,
        spell_name: str,
        power: int
    ) -> str:
        return (
            "Successfully cast "
            f"{spell_name} with {power} power"
        )


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"
    print("Result:", fireball())

    print("\nTesting retrying spell...")

    @retry_spell(3)
    def failed_spell() -> str:
        raise Exception("Spell failed")
    print(failed_spell())
    print("Waaaaaaagh spelled !")

    print("\nTesting MageGuild...")
    print(
        MageGuild.validate_mage_name("Gandalf")
    )
    print(
        MageGuild.validate_mage_name("R2")
    )

    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))
