"""
Simple Calculator
------------------
A command-line calculator that performs basic arithmetic operations
(addition, subtraction, multiplication, division) with proper input
validation and error handling.

Author: <YOUR NAME HERE>
"""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """
    Return the quotient of a and b.
    Raises ZeroDivisionError if b is 0 (handled by the caller).
    """
    return a / b


def get_number(prompt):
    """
    Keep asking the user for input until a valid float is entered.
    This prevents the program from crashing on bad input like letters.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value (e.g. 10 or 3.5).")


def get_operation():
    """Ask the user which operation they want to perform."""
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    choice = input("Enter choice (1/2/3/4): ").strip()
    return choice


def main():
    print("=" * 40)
    print("        SIMPLE CALCULATOR")
    print("=" * 40)

    while True:
        choice = get_operation()

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Please select 1, 2, 3, or 4.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        try:
            if choice == "1":
                result = add(num1, num2)
                symbol = "+"
            elif choice == "2":
                result = subtract(num1, num2)
                symbol = "-"
            elif choice == "3":
                result = multiply(num1, num2)
                symbol = "*"
            elif choice == "4":
                result = divide(num1, num2)  # may raise ZeroDivisionError
                symbol = "/"

            print(f"\nResult: {num1} {symbol} {num2} = {result}")

        except ZeroDivisionError:
            # Handles the case where the user tries to divide by zero
            print("\nError: Division by zero is not allowed.")

        again = input("\nDo you want to perform another calculation? (y/n): ").strip().lower()
        if again != "y":
            print("\nThank you for using the calculator. Goodbye!")
            break


if __name__ == "__main__":
    main()
