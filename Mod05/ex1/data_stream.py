#!/usr/bin/env python3

from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):

    def __init__(self):
        self._queue: list[str] = []
        self._counter: int = 0

    @abstractmethod
    def can_process(self, data) -> bool:
        pass

    @abstractmethod
    def process(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._queue:
            raise Exception("No data available.")
        value = self._queue.pop(0)
        count = self._counter
        self._counter += 1
        return (count, value)


class NumericProcessor(DataProcessor):

    def _is_valid_number(self, data: Any) -> bool:
        return isinstance(data, (int, float)) and not isinstance(data, bool)

    def can_process(self, data: Any) -> bool:
        if self._is_valid_number(data):
            return True

        if isinstance(data, list):
            return all(self._is_valid_number(value) for value in data)

        return False

    def process(self, data: Any) -> None:
        if isinstance(data, list):
            for value in data:
                self._queue.append(str(value))
        else:
            self._queue.append(str(data))


class TextProcessor(DataProcessor):

    def can_process(self, data: Any) -> bool:
        if isinstance(data, str):
            return True

        if isinstance(data, list):
            return all(isinstance(value, str) for value in data)

        return False

    def process(self, data: Any) -> None:
        if isinstance(data, list):
            self._queue.extend(data)
        else:
            self._queue.append(data)


class LogProcessor(DataProcessor):

    def _is_valid_log(self, data: Any) -> bool:
        if not isinstance(data, dict):
            return False

        return all(isinstance(key, str) and isinstance(value, str)
                   for key, value in data.items())

    def can_process(self, data: Any) -> bool:
        if self._is_valid_log(data):
            return True

        if isinstance(data, list):
            return all(self._is_valid_log(value) for value in data)

        return False

    def process(self, data: Any) -> None:
        if isinstance(data, list):
            for value in data:
                self._queue.append(value)
        else:
            self._queue.append(data)


class DataStream():

    def __init__(self):
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            # handled: evita procesar el mismo dato varias veces.
            handled = False

            for proc in self.processors:
                if proc.can_process(element):
                    handled = True
                    # break: en cuanto uno lo procesa, se termina.
                    break # importante: no seguir probando más processors

            if not handled:
                print("Error: No processor found for element: {element}")

    def print_processors_stats(self) -> None:
        for proc in self.processors:
            print(proc.stats())

def demo_stream():
    demo_batch = ["Hello world", [3.14, -1, 2.71],
                 [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'},
                 {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
                 42, ['Hi', 'five']]



if __name__ == "__main__":

    print("=== Code Nexus - Data Stream ===")
    print()
    demo_stream()
