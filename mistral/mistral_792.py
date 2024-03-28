
# A simple function to check if a number is within a given range
def is_in_range(number, start, end):
    # Check if the number is greater than or equal to the start and less than or equal to the end
    return start <= number <= end

# Function to perform some calculations and check conditions using and operator and assert statement
def calculate_and_check():
    a = 5
    b = 3
    c = a + b
    result = c * 2

    # Check if the condition is true, i.e., a and b are positive numbers and c is even
    if a > 0 and b > 0 and c % 2 == 0:
        assert result > 10, f"Error: The result ({result}) should be greater than 10"
        print("All conditions met!")
        print(f"The result is: {result}")
    else:
        print("One or more conditions are not met.")

# Test the function
calculate_and_check()
