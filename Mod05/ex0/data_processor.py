#!/usr/bin/env python3

from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):

    def __init__(self):
        self._stack: list[str] = []
        self._counter: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._stack:
            raise Exception("No data available.")
        value = self._stack.pop(0)
        count = self._counter
        self._counter += 1
        return (count, value)


class NumericProcessor(DataProcessor):

    def _is_valid_number(self, data: Any) -> bool:
        return isinstance(data, (int, float)) and not isinstance(data, bool)

    def validate(self, data: Any) -> bool:
        # Comprueba que los elementos sean números válidos
        if self._is_valid_number(data):
            return True
        # Comprueba que todos los elementos de data (list) sean válidos
        # return all(self._is_valid_number(value) for value in data)
        if isinstance(data, list):
            for value in data:
                if not self._is_valid_number(value):
                    return False
            return True
        return False

    def ingest(self, data: Any) -> None:
        # Validar otra vez
        if not self.validate(data):
            raise Exception("Improper numeric data")
        # Añade al stack de almacenaje
        if isinstance(data, list):
            for value in data:
                self._stack.append(str(value))
            else:
                self._stack.append(str(data))


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True

        if isinstance(data, list):
            for value in data:
                if not isinstance(value, str):
                    return False
            return True

        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")
        '''
        lista = [1, 2]; lista.append([3, 4]) -> Resultado: [1, 2, [3, 4]]
        lista = [1, 2]; lista.extend([3, 4]) -> Resultado: [1, 2, 3, 4]
        '''
        # Desempaqueta el iterable y añade sus elementos uno a uno
        if isinstance(data, list):
            self._stack.extend(data)
        # Añade el argumento tal cual, como un único elemento
        else:
            self._stack.append(data)


class LogProcessor(DataProcessor):

    def _is_valid_log(self, data: Any) -> bool:

        if not isinstance(data, dict):
            return False

        return all(isinstance(key, str) and isinstance(value, str)
                   for key, value in data.items())

    def validate(self, data: Any) -> bool:

        if self._is_valid_log(data):
            return True

        if isinstance(data, list):
            return all(self._is_valid_log(value) for value in data)

        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")

        def format_log(d: dict[str, str]) -> str:
            return f"{d.get('log_level')}: {d.get('log_message')}"

        if isinstance(data, list):
            for value in data:
                self._stack.append(format_log(value))
        else:
            self._stack.append(format_log(data))


def demo_nexus():

    demo_np = NumericProcessor()
    demo_tp = TextProcessor()
    demo_lp = LogProcessor()

    demo_range_3 = 3
    demo_range_2 = 2
    demo_range_1 = 1

    demo_int_list = [1, 2, 3, 4, 5]
    demo_str_list = ["Hello", "Nexus", "World"]
    demo_log_dict = [
                    {"log_level": "NOTICE",
                     "log_message": "Connection to server"},
                    {"log_level": "ERROR",
                     "log_message": "Unauthorized access!!"}
                    ]
    demo_int = 42
    demo_str = "Hello"
    demo_foo = "foo"

    print("Testing Numeric Processor...")
    print(f"Trying to validate input '{demo_int}':",
          demo_np.validate(demo_int))
    print(f"Trying to validate input '{demo_str}':",
          demo_np.validate(demo_str))
    print(f"Test invalid ingestion of string"
          f" '{demo_foo}' without prior validation:")
    try:
        demo_np.ingest(demo_foo)
    except Exception as error:
        print("Got Exception:", error)

    print("Processing data:", demo_int_list)
    demo_np.ingest(demo_int_list)
    print(f"Extracting {demo_range_3} values...")
    for _ in range(demo_range_3):
        rank, value = demo_np.output()
        print(f"Numeric value {rank}: {value}")

    print()
    print("Testing Text Processor...")
    print(f"Trying to validate input '{demo_int}':",
          demo_tp.validate(demo_int))
    print("Processing data:", demo_str_list)
    demo_tp.ingest(demo_str_list)
    print(f"Extracting {demo_range_1} values...")
    for _ in range(demo_range_1):
        rank, value = demo_tp.output()
        print(f"Text value {rank}: {value}")

    print()
    print("Testing Log Processor...")
    print(f"Trying to validate input '{demo_str}':",
          demo_lp.validate(demo_str))
    print("Processing data:", demo_log_dict)
    demo_lp.ingest(demo_log_dict)
    print(f"Extracting {demo_range_2} values...")
    for _ in range(demo_range_2):
        rank, value = demo_lp.output()
        print(f"Log entry {rank}: {value}")


if __name__ == "__main__":

    print("=== Code Nexus - Data Processor ===")
    print()
    demo_nexus()
