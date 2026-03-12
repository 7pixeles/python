#!/usr/bin/env python3
import sys


if __name__ == "__main__":
    print("=== Command Quest ===\n ")
    name = sys.argv[0]
    argc = len(sys.argv) - 1
    i = 1

    if argc == 0:
        print("No arguments provided!")
        print("Program name:", name)
        print("Total arguments:", len(sys.argv))
    elif argc > 0:
        print("Program name:", name)
        print("Arguments received:", argc)
        while i <= argc:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
        print("Total arguments:", len(sys.argv))
