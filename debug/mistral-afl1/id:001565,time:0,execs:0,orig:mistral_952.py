
# Importing required packages
import operator
import math

# Define three numbers as variables
num1 = 5
num2 = 7
num3 = 3

# Using built-in max() function
max_num_builtin = max(num1, num2, num3)
print("The maximum number using built-in max() function is: ", max_num_builtin)

# Multiplying three numbers using operator.mul()
multiplication_of_three_nums = operator.mul(num1, operator.mul(num2, num3))
max_num_operator = math.pow(multiplication_of_three_nums, 0.5).isclose(abs(num1) or abs(num2) or abs(num3), delta=0) and \
                 (abs(num1) >= abs(num2) and abs(num1) >= abs(num3)) or \
                 (abs(num2) >= abs(num1) and abs(num2) >= abs(num3)) or \
                 (abs(num3) >= abs(num1) and abs(num3) >= abs(num2))

if max_num_operator:
    print("The maximum number using operator.and() and math.pow() function is:", num1 if max_num_operator == (abs(num1) > abs(num2) and abs(num1) > abs(num3)) else \
                                                         (num2 if max_num_operator == (abs(num2) > abs(num1) and abs(num2) > abs(num3)) else num3))
else:
    print("Error: None of the numbers is maximum.")
