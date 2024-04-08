
# Importing the 'assert' module from 'pytest'
import pytest

def test_add():
    # Given two numbers
    num1 = 5
    num2 = 3

    # When we add these two numbers
    result = num1 + num2

    # Then the sum should be equal to the expected value
    assert num1 + num2 == 8, f"The sum of {num1} and {num2} is not equal to 8."

def test_multiply():
    # Given two numbers
    num1 = 3
    num2 = 5

    # When we multiply these two numbers
    result = num1 * num2

    # Then the product should be equal to the expected value
    assert num1 * num2 == 15, f"The product of {num1} and {num2} is not equal to 15."

def test_is_even():
    # Given a number
    num = 6

    # When we check if the number is even using 'and' keyword
    is_even = (num % 2 == 0) and (num > 0)

    # Then the result should be True
    assert is_even is True, f"{num} is not an even positive number."
