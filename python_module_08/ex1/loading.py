import sys

try:
    import numpy as np
except ModuleNotFoundError:
    np = None

try:
    import pandas as pd
except ModuleNotFoundError:
    pd = None

try:
    import matplotlib
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    matplotlib = None
    plt = None

try:
    import requests
except ModuleNotFoundError:
    requests = None


def check_dependencies() -> bool:
    """Check if required packages
    are installed and print their status."""
    list_packages = [
        ("pandas", pd, "Data manipulation"),
        ("numpy", np, "Numerical computation"),
        ("requests", requests, "Network access"),
        ("matplotlib", matplotlib, "Visualization"),
    ]

    available = True
    for (name, module, desc) in list_packages:
        if module is not None:
            print(f"[OK] {name} ({module.__version__}) - {desc} ready")
        else:
            print(f"[MISSING] {name} - {desc} not available")
            available = False

    return available


def gen_data_matrix() -> list:
    """Generate 1000 simulated Matrix data
    points using a normal distribution."""

    data = np.random.normal(loc=100, scale=100, size=1000)
    return data


def analyze_data(data):
    """Analyze data using pandas.
    Returns a DataFrame and basic statistics."""

    data_frame = pd.DataFrame(data, columns=["valor"])

    print("\nAnalyzing Matrix data...")
    print("Processing", len(data), "data points...")

    return data_frame


def print_install_instructions():
    """Print installation instructions for pip and Poetry."""

    print("\nMissing dependencies detected.")
    print("\nOption 1: Install with pip")
    print("  pip install -r requirements.txt")

    print("\nOption 2: Install with Poetry")
    print("  poetry install")
    print("  poetry run python loading.py")


def create_visualization(data) -> None:
    """Generate and save a histogram of the Matrix data
    as matrix_analysis.png."""

    print("Generating visualization...")

    plt.figure(figsize=(12, 8))
    plt.hist(data, bins=15, color='blue', edgecolor='white')

    plt.title("Matrix Data Analysis")
    plt.xlabel("Value")
    plt.ylabel("Frequency")

    plt.savefig("matrix_analysis.png")
    plt.close()

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    """Main entry point. Checks dependencies,
    generates data, and creates visualization."""

    print()
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    if check_dependencies() is False:
        print_install_instructions()
        sys.exit(1)

    data = gen_data_matrix()
    analyze_data(data)
    create_visualization(data)


if __name__ == "__main__":
    main()
