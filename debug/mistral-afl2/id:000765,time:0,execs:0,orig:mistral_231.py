
# Define some variables
num1 = 10
num2 = 5
is_even = True

# Check if num1 is even using the modulus operator
if num1 % 2 == 0:
    is_even = True
else:
    is_even = False

print(f"Number {num1} is even: {is_even}")

# Perform some arithmetic operations using false value
if not is_even:
    num1 = num1 % 2 + 1
    print(f"If number {num1} is odd, then add 1 and it becomes {num1}")
else:
    num2 = num2 // 2
    print(f"If number {num1} is even, then divide number {num2} by 2 and it becomes {num2}")

# Use false value in a comparison
if False:
    print("This statement will not be executed")
else:
    print("This statement will be executed instead")
