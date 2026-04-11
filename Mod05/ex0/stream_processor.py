#!/usr/bin/env python3

from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        ''' Extrae los datos de la lista
            longitud, suma, average
        '''
        if not self.validate(data):
            return "Validation: Non numeric data error"
        size = len(data)
        suma = sum(data)
        avg = suma / size
        result = f"Processed {size} numeric values, sum={suma}, avg={avg:.1f}"
        return result

    def validate(self, data: Any) -> bool:
        '''#1 Comprueba que los datos sean una lista
           #2 Comprueba que cada parte de la lista sea un número
           return: True / False
        '''
        if not isinstance(data, list):
            return False
        if not data:
            return False
        return all(isinstance(each, (int, float)) for each in data)


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        '''Debe validar que es una string válida
            return: True / False
        '''
        pass

    def process(self, data: Any) -> str:
        ''' cuenta longitud y palabras '''
        pass

    def format_output(self, result):
        '''Devuelve el resultado en una cadena válida'''
        pass


class LogProcess(DataProcessor):
    def validate(self, data: Any) -> bool:
        ''' Debe comprobar la conexión'''
        pass

    def process(self, data: Any) -> str:
        pass

    def format_output(self, result):
        pass


def demo_nexus():
    nbr_data = [1, 2, 3, 4, 5]
    str_data = "Hello Nexus World"
    log_data = "ERROR: Connection Timeout"

    print("\nInitializing Numeric Processor...")
    print("Processing data:", nbr_data)
    nbr_processor = NumericProcessor()
    nbr_result = nbr_processor.process(nbr_data)
    print(nbr_processor.format_output(nbr_result))

    # print("\nInitializing Text Processor...")
    # print("Processing data:", str_data)
    # str_processor = TextProcessor
    # str_result = str_processor.process(str_data)
    # if str_processor.validate(str_data):
    #     print(str_result)

    # print("\nInitializing Log Processor...")
    # print("Processing data:", log_data)
    # log_processor = LogProcess
    # log_result = log_processor.process(log_data)
    # if log_processor.validate(str_data):
    #     print(log_result)
    # print("\nFoundation systems online. Nexus ready for advanced streams.")


def demo_polymorphic():
    print("=== Polymorphic Processing Demo ===")

    print("Processing multiple data types through same interface...")

    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    demo_nexus()
    # demo_polymorphic()
