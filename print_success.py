RED = '\033[31m'
GREEN = '\033[32m'
RESET = '\033[0m'

def print_success(message: str) -> None:
    """
    Prints a success message in green color.

    Args:
        message (str): The success message to print.
    """
    print(f"{GREEN}{message}{RESET}")
