#!/usr/bin/env python3

def crisis_protocol():
    """
    Simulates archive crisis scenarios and logs system responses
    for missing files, permission errors, and successful access.
    """
    print("\n[CRISIS ALERT] Attempting access to 'lost_archive.txt'...")
    try:
        with open("lost_archive.txt", "r") as lost_file:
            print(lost_file.read())
        print("[STATUS] Normal operations resumed")
    except FileNotFoundError:
        print("[RESPONSE] Archive not found in storage matrix")
    print("[STATUS]: Crisis handled, system stable")

    print("\n[CRISIS ALERT] Attempting access to 'classified_vault.txt'...")
    try:
        with open("classified_vault.txt", "r") as classified_file:
            print(classified_file.read())
        print("[STATUS] Normal operations resumed")
    except FileNotFoundError:
        print("[RESPONSE] Archive not found in storage matrix.")
    except PermissionError:
        print("[RESPONSE] Security protocols deny access")
    print("[STATUS]: Crisis handled, security maintained")

    print("\n[ROUTINE ALERT] Attempting access to 'standard_archive.txt'...")
    try:
        with open("standard_archive.txt", "r") as standard_file:
            print("[SUCCESS] Archive recovered - ", end="")
            print(f"'''{standard_file.read()}'''")
        print("[STATUS] Normal operations resumed")
    except Exception:
        print("[ERROR] Unexpected error")
    print("[STATUS]: Crisis handled, security maintained")

    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    crisis_protocol()
