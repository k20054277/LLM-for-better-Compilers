
# Example program to demonstrate the use of None and exception

# Define a function to check if a number is even
def is_even(num):
    # If the number is None, return an error
    if num is None:
        raise ValueError("Number must be defined")

    # If the number is not even, return False
    return num % 2 == 0


# Try to check if 5 is even
try:
    is_even(5)
    print("5 is even")
except ValueError as e:
    # Catch the error and print it
    print("Error:", e)


# Try to check if None is even
try:
    is_even(None)
    print("None is even")
except ValueError as e:
    # Catch the error and print it
    print("Error:", e)
