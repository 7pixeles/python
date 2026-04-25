#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    argv = sys.argv
    argc = len(sys.argv)

    if argc == 1:
        print("Program name:", argv[0])
        print("No arguments provided!")
        print("Total arguments:", len(sys.argv))
    elif argc > 0:
        print("Program name:", argv[0])
        print("Arguments received:", argc - 1)
        i = 1
        while i < argc:
            print(f"Argument {i}: {argv[i]}")
            i += 1
        print("Total arguments:", argc)
