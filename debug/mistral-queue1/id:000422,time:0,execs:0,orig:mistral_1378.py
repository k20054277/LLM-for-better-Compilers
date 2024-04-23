
import sys

def square_root(number):
    try:
        result = number ** 0.5
    except Exception:
        print("Error! Tried to find the square root of a negative number.")
        sys.exit(1)
    return result

assert square_root(9) == 3, "The square root of 9 is not equal to 3"
assert square_root(16) == 4, "The square root of 16 is not equal to 4"
assert square_root(25) == 5, "The square root of 25 is not equal to 5"

print("All tests passed!")

try:
    assert square_root(-1) == 0
except AssertionError as err:
    print(f"Assertion error: {err}")

print("Program ending...")
