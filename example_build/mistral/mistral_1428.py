
# Define a function that calculates the square root of a number
def compute_square_root(number):
    # Assuming the input is a non-negative number
    result = number ** 0.5
    return result

# Define a variable with a value
input_number = 25

# Use assert statement to ensure the input is non-negative
assert input_number >= 0, "Input must be non-negative"

# Calculate the square root using the compute_square_root function
result = compute_square_root(input_number)

# Use print statement to display the result
print("The square root of", input_number, "is:", result)
