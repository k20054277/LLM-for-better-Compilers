
def factorial(n):
    # Assertion to validate input
    assert n >= 0, "Input must be non-negative integer"
    
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

try:
    number = int(input("Enter a non-negative integer: "))
    result = factorial(number)
    print(f"The factorial of {number} is {result}")
except AssertionError as e:
    print(e)
except Exception as e:
    print("An error occurred:", e)
