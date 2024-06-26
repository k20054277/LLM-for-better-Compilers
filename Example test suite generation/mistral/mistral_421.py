
# Function that returns the square root of a number if it's positive, and None otherwise
def compute_square_root(number):
    if number < 0:
        print("Error: Cannot compute square root of negative number")
        return None
    else:
        return number ** 0.5

# Function that tries to find the square root of a number and prints it out
def print_square_root(number):
    result = compute_square_root(number)
    if result is not None:
        print(f"The square root of {number} is {result}")

# Testing cases
print("Computing square root of 4:")
print_square_root(4)

print("\nComputing square root of -1:")
print_square_root(-1)
