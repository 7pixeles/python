#!/usr/bin/env python3
import sys


def recovery_files():
    """
    Runs the data recovery system.

    Reads a file specified as a command-line argument and
    displays its contents.
    Prints an error if the file does not exist or no argument
    is provided.

    Returns:
        None
    """
    if len(sys.argv) > 1:
        try:
            file_source = sys.argv[1]
            print("\n[CONNECTING...]")
            file = open(file_source, 'r')
            print("Accessing Storage Vault:", file.name)
            print("\nRECOVERED DATA:")
            print(file.read())
            file.close()
            print("\n[COMPLETED] Data recovery complete. "
                  "Storage unit disconected")
        except FileNotFoundError:
            print("[ERROR] Storage vault not found")
    else:
        print("[FILE NOT FOUND] Please, insert an existing file")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    recovery_files()
