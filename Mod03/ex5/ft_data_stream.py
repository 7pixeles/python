#!/usr/bin/env python3
"""
Game event stream processing with analytics and generator demonstrations.

Provides generators for game events, Fibonacci numbers, and primes,
along with utilities to process and summarize game streams.
"""

from typing import Generator

Event = tuple[int, str, int, str]


def stream_processor(n: int) -> Generator[Event, None, None]:
    """Yield a sequence of game events for n iterations.

    Each event contains:
        - event_id (int)
        - player name (str)
        - player level (int)
        - event type (str)
    """
    players = ['alice', 'bob', 'charlie']
    event_types = (
        'found treasure',
        'killed monster',
        'leveled up'
    )
    for i in range(1, n + 1):
        player = players[(i - 1) % 3]
        level = (i * 7) % 20 + 1
        event_type = event_types[(i - 1) % 3]
        yield i, player, level, event_type


def fibonacci_stream(n: int) -> Generator[int, None, None]:
    """Generate an infinite Fibonacci sequence."""
    x = 0
    y = 1

    while True:
        yield x
        x, y = y, x + y


def prime_stream() -> Generator[int, None, None]:
    """Generate an infinite sequence of prime numbers."""
    num = 2
    while True:
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            yield num

        num += 1


def stream_analytics(
        count_event: int,
        high_level: int,
        treasure: int,
        level_up: int
        ) -> None:
    """Print summary statistics of processed game events."""

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {count_event}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {level_up}")


def generator_demo() -> None:
    """Demonstrate Fibonacci and prime number generators."""
    print("=== Generator Demonstration ===")
    seq_fibo = fibonacci_stream(10)
    fibo = [next(seq_fibo) for _ in range[10]]
    print("Fibonacci sequence (first 10):", *fibo)

    seq_prime = prime_stream()
    prime = [next(seq_prime) for _ in range(5)]
    print("Prime numbers (first 5):", *prime)


def processing_stream(n: int) -> None:
    """Process n game events, print first few, and summarize statistics."""
    count_event = 0
    count_high_level = 0
    count_treasure = 0
    count_level_up = 0

    print(f"Processing {n} game events...\n")
    for event_id, player, level, event in stream_processor(n):
        count_event += 1
        if level >= 10:
            count_high_level += 1
        if event == "found treasure":
            count_treasure += 1
        if event == "leveled up":
            count_level_up += 1
        if event_id <= 3:
            print(f"Event {event_id}: Player {player} (level {level})"
                  f" {event}")
    print("...")

    stream_analytics(
        count_event,
        count_high_level,
        count_treasure,
        count_level_up
    )

    print("\nMemory usage: Constant (streaming)")
    print("Processing time [simulated]: 0.045 seconds")


def main() -> None:
    """Run the game event stream processor and generator demonstration."""

    print("=== Game Data Stream Processor ===")
    processing_stream(1000)
    print()
    generator_demo()


if __name__ == "__main__":
    main()
