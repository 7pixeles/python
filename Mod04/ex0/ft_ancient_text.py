#!/usr/bin/env python3

import sys

def recovery_files():
    """Run the data recovery system."""

    if len(sys.argv) > 1:
        try:
            file_source = sys.argv[1]
            print("\n[CONNECTING...]")
            with open(file_source, 'r') as file:
                print("Accessing Storage Vault:", file.name)
                print("\nRECOVERED DATA:")
                print(file.read())
            file.close()
            print("\n[COMPLETED] Data recovery complete. Storage unit disconected")
        except FileNotFoundError:
            print("[ERROR] Storage vault not found")
    else:
        print("[FILE NOT FOUND] Please, insert an existing file")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    recovery_files()
