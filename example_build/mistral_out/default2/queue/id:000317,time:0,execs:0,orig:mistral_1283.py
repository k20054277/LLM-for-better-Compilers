
def factorial(n):
    """
    This function calculates the factorial of a given number n.
    """

    try:
        assert n >= 0, "Error: Number should be non-negative"
        result = 1
        for i in range(1, n + 1):
            result *= i
            if result > (2 ** 31 - 1): # Maximum value of a 32-bit signed integer
                print("Error: Factorial too large to represent as a Python int")
                break
        return result
    except AssertionError as e:
        print(e)

if __name__ == "__main__":
    num = int(input("Enter a non-negative number: "))
    fact = factorial(num)
    if fact is not None:
        print(f"The factorial of {num} is {fact}")
