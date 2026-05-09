#!/usr/bin/env python3
import sys


def recovery_files():
    if len(sys.argv) > 1:
        try:
            file_source = sys.argv[1]
            print(f"\nAccessing file '{file_source}'")
            file = open(file_source, 'r')
            print("Accessing Storage Vault:", file_source)
            print("\nRECOVERED DATA:")
            print(file.read())
            file.close()

            print("\n[COMPLETED] Data recovery complete. "
                  "Storage unit disconected")

        except FileNotFoundError:
            print("[ERROR] Storage vault not found")

    else:
        print("Usage: ft_ancient_text.py <file>")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    recovery_files()
