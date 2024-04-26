
# Function to check if list elements are numbers and sum them up
def process_input(input_list):
    # Use assertion to validate input list
    assert all(isinstance(i, (int, float)) for i in input_list), "Input list should only contain numeric types"
    
    # Sum up the elements of the list using sum function
    total = sum(input_list)
    
    # Return the total
    return total

# Testing the function with valid inputs
numbers = [1, 2.5, 3, 4]
print("Sum of the numbers:", process_input(numbers))

# Testing the function with an invalid input (list containing a string)
mixed_numbers = [1, 2.5, "three"]
try:
    print("Sum of the numbers:", process_input(mixed_numbers))
except AssertionError as e:
    print("Error:", e)
