#!/usr/bin/env python

def main():
    # Example 1: Using assert with a condition
    x = 5
    y = 3
    assert x > y, "x is not greater than y"

    # Example 2: Using //= to divide two numbers and assign the result to a variable
    num1 = 10
    num2 = 5
    quotient = num1 //= num2
    print(quotient) # prints 2

if __name__ == "__main__":
    main()