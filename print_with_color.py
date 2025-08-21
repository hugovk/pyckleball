RED = '\033[31m'
GREEN = '\033[32m'
RESET = '\033[0m'
YELLOW = '\033[33m'
BLUE = '\033[34m'

def print_success(message: str) -> None:
    print(f"{GREEN}{message}{RESET}")

def print_yellow(message: str) -> None:
    print(f"{YELLOW}{message}{RESET}")

def print_blue(message: str) -> None:
    print(f"{BLUE}{message}{RESET}")

if __name__ == "__main__":
    print_success("This is a success message.")
    print_yellow("This is a yellow message.")
    print_blue("This is a blue message.")
