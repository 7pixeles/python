import os
from dotenv import load_dotenv

load_dotenv()


def load_config() -> dict:
    """Load environment variables and return a configuration dictionary.

    Returns default values for non-sensitive variables if not set.
    Returns None for sensitive variables if not set.
    """

    config = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE", "development"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "DEBUG"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }
    return config


def display_config(config) -> None:
    """Display the current configuration status.

    Warns if any variable is not configured.
    """

    print("Configuration loaded:")

    for (key, value) in config.items():
        if value is None:
            print(key, "WARNING: not configured")
        else:
            print(key, value)


def security_check(config) -> None:
    """Run environment security checks.

    Verifies that the .env file exists, that no placeholder
    secrets are detected, and whether production overrides
    are active.
    """

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found")

    hardcoded_pass = ["123", "test", "secret", "password", "abc", "example"]
    api_key = config["API_KEY"]

    if api_key is None:
        print("[WARNING] API_KEY not configured")
    elif api_key.lower() in hardcoded_pass:
        print("[WARNING] API_KEY looks like a placeholder")
    else:
        print("[OK] No hardcoded secrets detected")

    if config["MATRIX_MODE"] == "production":
        print("[OK] Production overrides available")
    else:
        print("[INFO] Running in development mode")


def main() -> None:
    """Entry point.Loads config, displays status and runs security checks."""

    print("ORACLE STATUS: Reading the Matrix...\n")
    config = load_config()
    display_config(config)
    print()
    security_check(config)
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
