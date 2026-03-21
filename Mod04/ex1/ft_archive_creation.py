#!/usr/bin/env python3

def create_archive() -> str | None:
    """
    Creates a new archive file with preset data.

    Returns:
        str: File name if creation succeeds.
        None: If creation fails (e.g., permissions or disk error).
    """
    file_name = "new_discovery.txt"
    print(f"\nInitializing new storage unit: {file_name}")
    try:
        with open(file_name, "w") as file:
            print("Storage unit created successfully...")
            print("\nInscribing preservation data...")

            content = (
                "[ENTRY 001] New quantum algorithm discovered\n"
                "[ENTRY 002] Efficiency increased by 347%\n"
                "[ENTRY 003] Archived by Data Archivist trainee"
            )
            file.write(content)

        return (file_name)

    except OSError:
        print("ERROR: Unable to create archive")
        return None


def read_archive(file_name: str) -> None:
    """
    Reads and prints the content of an archive file.

    Args:
        file_name (str): Archive file to read.

    Returns:
        None
    """
    try:
        with open(file_name, "r") as file:
            content = file.read()

            if not content:
                print("Archive is empty.")
            else:
                print(content)

        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{file_name}' ready for long-term preservation.")

    except OSError:
        print("ERROR: Unable to read archive")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    file = create_archive()
    if file is not None:
        read_archive(file)
