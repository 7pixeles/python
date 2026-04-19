#!/usr/bin/env python3
"""
Game event stream processing with analytics and generator demonstrations.

Provides generators for game events, Fibonacci numbers, and primes,
along with utilities to process and summarize game streams.
"""

from typing import Generator
import random


def gen_event() -> Generator[tuple, None, None]:
    """
    Generate an infinite stream of random game events.

    Yields
    ------
    tuple of str
        A tuple (player, action) representing a game event.
    """
    players = [
        "Alice",
        "Bob",
        "Charlie",
        "Dylan"
        ]

    actions = [
        "eat",
        "sleep",
        "climb",
        "run",
        "grab",
        "swim",
        "move",
        "release",
        "use"
    ]
    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield player, action


def consume_event(events: list):
    """
    Yield random events from a list until it becomes empty.

    Parameters
    ----------
    events : list of tuple
        List of (player, action) events to consume.

    Yields
    ------
    tuple of str
        Randomly selected event from the list.

    Notes
    -----
    The function does not remove items from the list. External mutation
    is required to eventually terminate the generator.
    """
    print(events)
    while events:
        random_item = random.choice(events)
        yield random_item


def main() -> None:
    """
    Run the game event stream processing demonstration.

    Generates a sequence of random events, builds a list of events, and
    consumes them using a generator to demonstrate streaming behavior.
    """
    print("=== Game Data Stream Processor ===")
    gen = gen_event()

    for i in range(1000):
        player, action = next(gen)
        print(f"Event {i}: Player {player} did {action}")

    ten_events = gen_event()
    new_list = []
    for _ in range(10):
        item_events = next(ten_events)
        new_list.append(item_events)
    print(f"Built list of 10 events: {new_list}")
    for random_item in consume_event(new_list):
        print(f"Got event from list: {random_item}")
        for random_item in new_list:
            new_list.remove(random_item)
        print(f"Remains in list: {new_list}")


if __name__ == "__main__":
    main()
