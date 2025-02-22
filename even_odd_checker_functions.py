"""
Even or Odd Checker
Handles user input and determines if a number is even or odd.
"""
def get_integer_input() -> int:
    """Prompt user for an integer input with validation."""
    while True:
        try:
            return int(input("Enter an integer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def check_even_odd(number: int) -> str:
    """Check if the number is even or odd and return a message."""
    return f"{number} is an {'Even' if number % 2 == 0 else 'Odd'} number."

if __name__ == "__main__":
    num = get_integer_input()
    print(check_even_odd(num))
