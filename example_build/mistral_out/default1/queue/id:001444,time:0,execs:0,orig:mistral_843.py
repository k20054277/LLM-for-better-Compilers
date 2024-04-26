
# Example 1: Using 'and' operator for Boolean expressions
def is_valid(age, height):
    # Check if age is greater than 18 and height is less than 5.5 (in meters)
    return age > 18 and height < 0.5

age = 25
height = 1.65
if is_valid(age, height):
    print("Valid")
else:
    print("Invalid")

# Example 2: Using 'and' operator with floating-point numbers
def is_number_close_to(num, target, tolerance=0.01):
    return abs(num - target) < tolerance

num = 3.14159
target = 3.14
if is_number_close_to(num, target):
    print("Number is close to the target")
else:
    print("Number is not close to the target")
