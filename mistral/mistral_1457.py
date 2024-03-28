
import math

def basic_sqrt(number):
    """Calculate the square root using the basic method"""
    assert number >= 0, "Error: The input number must be non-negative"
    guess = number / 2.0
    while abs(guess*guess - number) > 0.01:
        guess = (guess + number/guess) / 2.0
    return round(guess, 2)

def optimized_sqrt(number):
    """Calculate the square root using the optimized method with Newton-Raphson technique"""
    assert number >= 0, "Error: The input number must be non-negative"
    guess = number / 2.0

    while abs(guess*guess - number) > 0.001:
        guess = (guess + number/guess) / 2.0

    return round(guess, 2)

if __name__ == "__main__":
    print("Calculate square root using the basic method:")
    num = float(input("Enter a positive number: "))
    result = basic_sqrt(num)
    print(f"The square root of {num} is approximately {result}")
    
    print("\nCalculate square root using the optimized method:")
    num = float(input("Enter a positive number: "))
    result = optimized_sqrt(num)
    print(f"The square root of {num} is approximately {result}")
