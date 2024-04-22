
# Function to check if all numbers in a tuple are positive
def all_positive(numbers: tuple) -> None:
    for num in numbers:
        assert num > 0, f"Negative number found: {num}"
        # Your code here. If all numbers are positive, this function does nothing.
        print(f"Number: {num} is positive.")

# Test the function with positive numbers
all_positive((1, 2, 3, 4))

# Test the function with negative numbers
try:
    all_positive((-1, 2, 3, 4))
except AssertionError as e:
    print("Error:", e)
