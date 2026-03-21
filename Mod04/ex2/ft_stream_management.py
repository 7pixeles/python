#!/usr/bin/env python3
import sys


def communication_system() -> None:
    """
    Simulates archive communication by prompting for ID and status,
    then outputs messages to "stdout" and "stderr".

    Returns:
        None
    """
    print("Input Stream active.", end=" ")
    input_id = input("Enter archivist ID: ")
    print("Input Stream active.", end=" ")
    input_status = input("Enter status report: ")

    print(f"\n[STANDARD] Archive status from '{input_id}', '{input_status}'",
          file=sys.stdout)
    print("[ALERT] System diagnostic: Communication channels verified",
          file=sys.stderr)
    print("[STANDARD] Data transmission complete")
    print("\n12Three-channel communication test successful...")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    communication_system()
