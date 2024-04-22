
# Define some variables
num1 = 5
num2 = 10
is_even_num1 = num1 % 2 == 0
is_even_num2 = num2 % 2 == 0

# Use and operator to check if both numbers are even
if is_even_num1 and is_even_num2:
    print(f"Both {num1} and {num2} are even numbers.")

# Use or operator to check if at least one of the numbers is even
elif is_even_num1 or is_even_num2:
    print(f"Either {num1} or {num2}, or both, are even numbers.")

# Check if neither number is even
else:
    print(f"Both {num1} and {num2} are odd numbers.")
