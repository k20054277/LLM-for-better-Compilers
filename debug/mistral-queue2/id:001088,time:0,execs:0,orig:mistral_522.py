
# This is a simple function that returns the larger of two numbers using lambda and True
def larger_number(num1, num2):
    # Using lambda to create a small anonymous function that returns the larger number
    is_larger = lambda: num1 if num1 > num2 else num2
    
    # Using True to call the lambda function
    return is_larger()

# Testing the larger_number function with some numbers
print(larger_number(5, 3))         # Output: 5
print(larger_number(-1, 5))       # Output: 5
print(larger_number(0, -1))       # Output: 0
