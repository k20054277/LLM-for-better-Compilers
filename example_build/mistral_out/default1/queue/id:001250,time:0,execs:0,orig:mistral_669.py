
# Assigning Boolean values to variables
bool_var_1 = True
bool_var_2 = False

print("bool_var_1 is:", bool_var_1)
print("bool_var_2 is:", bool_var_2)

# Using Boolean values in conditional statements
if 5 > 3:
    print("Five is greater than three")
elif bool_var_1:
    print("Some condition is true")
else:
    print("Both five is not greater than three and some condition is false")

# Using Boolean values in logical operations
bool_var_3 = (5 > 3) and (2 + 2 == 4)
print("( Five is greater than three ) and ( Two plus two is equal to four ) is:", bool_var_3)

# Using Boolean values as input to functions
def print_message(is_positive):
    if is_positive:
        print("The number is positive")
    else:
        print("The number is negative or zero")

print_message(-1)  # Output: The number is negative
print_message(3)   # Output: The number is positive
