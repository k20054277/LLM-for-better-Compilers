
# This function takes two arguments and returns a tuple with the sum and product of the numbers
def calculate(num1, num2):
    # Perform calculations and return a tuple containing the sum and product
    result_sum = num1 + num2
    result_product = num1 * num2
    return num1, num2, result_sum, result_product

# Call the function with some arguments
num1 = 3
num2 = 5
nums, arg1, sum_result, product_result = calculate(num1, num2)

print("Number 1 is:", num1)
print("Number 2 is:", num2)
print("Sum of numbers is:", sum_result)
print("Product of numbers is:", product_result)

# In Python, None represents the absence of a value or no value
# This variable doesn't have any assigned value
my_variable = None

if my_variable:
    print("Variable has a value:", my_variable)
else:
    print("Variable is empty or does not exist")

# Create a tuple with some values, including None
my_tuple = (1, 2, "Three", None)
print("Elements in the tuple are:", my_tuple)
