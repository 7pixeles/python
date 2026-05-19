#!/usr/bin/env python3

from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    '''Estructura común de todos los procesadores'''
    name: str
    total_processor: int
    buffer: list[any]

    @abstractmethod
    def can_process(self, data: Any) -> bool:
        pass

    @abstractmethod
    def process(self, data: Any) -> None:
        pass

    @abstractmethod
    def output(self) -> list[tuple[int, str]]:
        pass


class DataStream:
    def __init__(self):
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            handled = False

            for proc in self.processors:
                if proc.can_process(element):
                    proc.process(element)
                    handled = True
                    break

            if not handled:
                print(f"DataStream error - Can't process"
                      f"element in stream {element}")

    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==")

        if not self.processors:
            print("No processor found, no data")
            return

        for proc in self.processors:
            print(f"{proc.name}: total {proc.total_processed}"
                  f" items processed, remaining"
                  f" {len(proc.buffer)} on processor")


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        self.name = "Numeric Processor"
        self.total_processed = 0
        self.buffer: list[Any] = []

    def can_process(self, data: Any) -> bool:
        return (isinstance(data, (int, float)) or isinstance(data, list)
                and all(isinstance(value, (int, float)) for value in data))

    def process(self, data: Any) -> None:
        if isinstance(data, list):
            self.buffer.extend(data)
            self.total_processed += len(data)

    def output(self, n: int) -> list[Any]:
        taken = self.buffer[:n]
        self.buffer = self.buffer[n:]
        return taken


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        self.name = "Text Processor"
        self.total_processed = 0
        self.buffer: list[Any] = []

    def can_process(self, data: Any) -> bool:
        return (isinstance(data, str) or (isinstance(data, list)
                and all(isinstance(value, str) for value in data)))

    def process(self, data: Any) -> None:
        if isinstance(data, list):
            self.buffer.extend(data)
            self.total_processed += len(data)
        else:
            self.buffer.append(data)
            self.total_processed += 1

    def output(self, n: int) -> list[Any]:
        taken = self.buffer[:n]
        self.buffer = self.buffer[n:]
        return taken


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        self.name = "Log Processor"
        self.total_processed = 0
        self.buffer: list[Any] = []

    def can_process(self, data: Any) -> bool:
        return (isinstance(data, list)
                and all(isinstance(value, dict) for value in data))

    def process(self, data: Any) -> None:
        self.buffer.extend(data)
        self.total_processed += len(data)

    def output(self, n: int) -> list[Any]:
        taken = self.buffer[:n]
        self.buffer = self.buffer[n:]
        return taken


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")
    ds = DataStream()
    print()
    print("Initialize Data Stream...")
    ds.print_processors_stats()

    print("\nRegistering Numeric Processor")
    ds.register_processor(NumericProcessor())

    stream = [
        "Hello World",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING",
             "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO",
             "log_message": "User wil is connected"}], 42, ["Hi", "Five"]
        ]
    print("\nSend first batch of data on stream:", stream)
    ds.process_stream(stream)
    ds.print_processors_stats()

    print("\nRegistering other data processors")
    ds.register_processor(TextProcessor())
    ds.register_processor(LogProcessor())

    print("Send the same batch again")
    ds.process_stream(stream)
    ds.print_processors_stats()

    print(
        "\nConsume some elements from the data processors:"
        "Numeric 3, Text 2, Log 1"
    )

    num_proc = ds.processors[0]
    text_proc = ds.processors[1]
    log_proc = ds.processors[2]
    num_proc.output(3)
    text_proc.output(2)
    log_proc.output(1)
    ds.print_processors_stats()
