
# Define some variables
num1 = 5
num2 = 3
is_even1 = num1 % 2 == 0
is_even2 = num2 % 2 == 0

# Use the 'and' operator to combine conditions
if is_even1 and is_even2:
    print("Both numbers are even.")
elif is_even1 or is_even2:
    print("One of the numbers is even.")
else:
    print("Both numbers are odd.")
