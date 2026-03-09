#!/usr/bin/env python3
"""
Simple Python Project
A basic application for GitHub Actions practice.
"""

def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


def calculate_sum(numbers: list[int]) -> int:
    """Calculate the sum of numbers."""
    return sum(numbers)


def main():
    """Main entry point."""
    print("Welcome to the Python Project!")
    print(greet("GitHub Actions"))
    
    result = calculate_sum([1, 2, 3, 4, 5])
    print(f"Sum of [1, 2, 3, 4, 5] = {result}")


if __name__ == "__main__":
    main()
