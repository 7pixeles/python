import sys
import os
import site


def print_instructions() -> None:
    code_unix = r'''source matrix_env/bin/activate # On Unix'''
    code_win = r'''matrix_env\Scripts\activate # On Windows'''
    code_start = r'''python -m venv matrix_env'''

    print("To enter the construct, run:",
          code_start, code_unix, code_win, sep='\n')
    print("\nThen run this program again.")


def detect_env() -> None:
    current_path = sys.executable
    if sys.prefix == sys.base_prefix:
        print("MATRIX STATUS: You're still plugged in\n")

        print("Current Python:", current_path)
        print("Virtual Environment: None detected")

        print()
        print("WARNING: You're in the global environment! "
              "The machines can see everything you install.")
        print_instructions()

    else:
        print("MATRIX STATUS: Welcome to the construct\n")
        print("Current Python:", current_path)
        virtual_env = os.path.basename(sys.prefix)
        path_packages = site.getsitepackages()[0]
        print("Virtual environment:", virtual_env)
        print("Environment path:", sys.prefix)

        print()
        print("SUCCESS: You're in an isolated environment!\n"
              "Safe to install packages without affecting the global system.")

        print()
        print("Package installation path:", path_packages)


if __name__ == "__main__":
    detect_env()
