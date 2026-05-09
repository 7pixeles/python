#!/usr/bin/env python3

def secure_archive(file_name: str, action="read", content=None) -> tuple:
    if action not in ("read" "write"):
        return (False, "Invalid action")

    if action == "write" and content is None:
        return (False, "No content to write")

    try:
        mode = "r" if action == "read" else "w"

        with open(file_name, mode) as file:

            if action == "read":
                result = file.read()
            else:
                file.write(content)
                result = "Content successfully written to file."

        return (True, result)

    except FileNotFoundError:
        return (False, "File not found.")

    except PermissionError:
        return (False, "Permission denied.")

    except Exception as error:
        return (False, str(error))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file.txt"))
    print()
    print("Using 'secure_archive' to read from a innaccesible file:")
    print(secure_archive("/etc/master.passwd"))
    print()
    print("Using 'secure archive' to read from a regular file:")
    success, data = secure_archive("ancient_fragment.txt")
    print(success, data)
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    if success:
        print(secure_archive("new_file.txt", "write", data))
    else:
        print("Failed read")
