#!/usr/bin/python3
import sys

def factorial(n):
    """Return the factorial of n using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    # Vérification du nombre d'arguments
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <non-negative integer>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 0:
            print("Error: Factorial is not defined for negative numbers.")
            sys.exit(1)

        print(factorial(n))

    except ValueError:
        print("Error: Please provide a valid integer.")
        sys.exit(1)

