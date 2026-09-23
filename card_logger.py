"""Simple console demo: read card numbers, validate 16 digits, append to a log."""

# ANSI colour codes - these are just strings the terminal interprets.
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
CYAN = "\033[36m"


def colour(text, code):
    """Wrap text in an ANSI colour code."""
    return f"{code}{text}{RESET}"


def is_sixteen_digits(number):
    """True if the input is exactly 16 characters, all digits."""
    return len(number) == 16 and number.isdigit()


def mask(number):
    """Keep only the BIN (first 6) and last 4: '411111******1111'."""
    return number[:6] + "*" * 6 + number[-4:]


def log_card(number):
    """Append the masked card to the log file."""
    with open("cards.log", "a", encoding="utf-8") as log:
        log.write(f"{mask(number)}\n")


def main():
    print(colour("\n=== Card Entry Demo ===", BOLD + CYAN))
    print(colour("Enter a 16-digit card number, or 'q' to quit.\n", CYAN))

    while True:
        raw = input(colour("Card number: ", BOLD))

        if raw.strip().lower() == "q":
            print(colour("\nGoodbye!\n", CYAN))
            break

        number = raw.strip()

        if not is_sixteen_digits(number):
            print(colour("  X  Must be exactly 16 digits.", RED))
            continue

        log_card(number)
        print(colour("  OK  Saved.", GREEN))


if __name__ == "__main__":
    main()
