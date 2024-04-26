
# Define some variables
num1 = 5
num2 = 3
is_even_num1 = num1 % 2 == 0
is_even_num2 = num2 % 2 == 0

# Use the and operator to check if both conditions are true
if is_even_num1 and is_even_num2:
    print("Both numbers are even")
else:
    print("One or both of the numbers is odd")
