
# Define some variables
num1 = 5
num2 = 10
is_even_num1 = num1 % 2 == 0
is_even_num2 = num2 % 2 == 0

# Use and for conditional expressions
if is_even_num1 and is_even_num2:
    print("Both numbers are even.")
else:
    print("One or both numbers are odd.")

# Use format for string formatting
name = "John Doe"
age = 30
print("Name: {0} \nAge: {1}".format(name, age))
