#!/usr/bin/env python3

def security_system():
    print("[SECURE ACCESS] Attempting vault connection...")
    print("[ACCESS GRANTED] Classified data retrieved successfully")
    try:
        classified_file = "classified_data.txt"
        print("\nSECURE EXTRACTION")
        with open(classified_file, "r") as extraction_file:
            print(extraction_file.read())
    except FileNotFoundError:
        print("[SECURITY ERROR] Vault not found")

    try:
        security_file = "security_protocols.txt"
        print("\nSECURE PRESERVATION")
        with open(security_file, "w") as preservation_file:
            entry_data = "[CLASSIFIED] New security protocols archived"
            preservation_file.write(entry_data)
            print(entry_data)

    except OSError:
        print("[ERROR] Operating System Error")

    print("\nCOMPLETED:"
          "[VAULT SEALED] Connection terminated securely")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    security_system()
