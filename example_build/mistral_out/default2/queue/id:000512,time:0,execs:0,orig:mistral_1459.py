
import math
import cProfile

def sum_of_squares(n):
    """Calculate sum of squares of numbers from 1 to n"""
    assert n >= 0, "Number must be greater than or equal to zero"

    result = 0
    for i in range(1, n + 1):
        result += i * i
    return result

if __name__ == "__main__":
    numbers = [0, -3, 5, 10]

    for num in numbers:
        sum_of_squares(num)
        
    print("Results:")
    for num, result in ((num, sum_of_squares(num)) for num in numbers):
        print(f"The square of numbers from 1 to {num} is {result}")

    # Profiling
    print("\nProfiling results:")
    cProfile.run("sum_of_squares(1000)")
