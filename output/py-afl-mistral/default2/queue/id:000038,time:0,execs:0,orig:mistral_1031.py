
# Define two variables with boolean values
num1 = 5
num2 = 10
is_even_num1 = num1 % 2 == 0
is_even_num2 = num2 % 2 == 0

# Use the 'and' operator to check if both conditions are true
if is_even_num1 and is_even_num2:
    print("Both numbers are even.")
else:
    print("At least one number is odd.")
