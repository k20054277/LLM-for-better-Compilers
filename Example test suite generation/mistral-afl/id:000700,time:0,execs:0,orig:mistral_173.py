
# Function to check if a number is even or odd
def is_even(num):
    # Intentionally put '=' instead of '==' for error
    if num = 0:
        return "Zero is neither even nor odd."
    elif num < 0:
        return "Negative numbers are neither even nor odd."
    elif num % 2 == 0:
        return f"{num} is an even number."
    else:
        return f"{num} is an odd number."

# Test the function with some input values
print(is_even(5))
print(is_even(-3))
print(is_even(0))

# Intentionally put a syntax error in the function for debugging
# Replace ':' with '='
# if num = 0:
