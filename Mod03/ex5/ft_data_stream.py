#!/usr/bin/env python3

from typing import Generator
import random


def gen_event() -> Generator[tuple, None, None]:
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
    print(events)
    while events:
        random_item = random.choice(events)
        yield random_item


def main() -> None:
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
