
# Define a function that returns None if an even number is not provided
def divide_by_two(number):
    if number % 2 == 0:
        result = number / 2
    else:
        print("Error: Invalid even number provided.")
        return None
    return result

# Test the function with some inputs
print(divide_by_two(4))   # Output: 2.0
print(divide_by_two(5))   # Error: Invalid even number provided.
print(divide_by_two(None)) # None
