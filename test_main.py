"""
Unit tests for the main module.
"""

from main import greet, calculate_sum


def test_greet():
    """Test the greet function."""
    assert greet("World") == "Hello, World!"
    assert greet("Python") == "Hello, Python!"


def test_calculate_sum():
    """Test the calculate_sum function."""
    assert calculate_sum([1, 2, 3]) == 6
    assert calculate_sum([10, 20, 30]) == 60
    assert calculate_sum([]) == 0
    assert calculate_sum([-5, 5]) == 0
