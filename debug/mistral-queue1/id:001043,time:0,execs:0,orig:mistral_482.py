
# Define a function that takes two arguments and returns their bitwise AND if they're not None, otherwise returns None
def bitwise_and(num1, num2):
    if num1 is not None and num2 is not None:
        return num1 & num2
    else:
        return None

# Define some variables that will be used as inputs to the function
num1 = 5  # binary: 101
num2 = 3  # binary: 011
num3 = None
num4 = 7  # binary: 0111

# Call the bitwise_and() function with different combinations of inputs
result1 = bitwise_and(num1, num2)
print("num1 = {} and num2 = {}, their bitwise AND is: {}".format(num1, num2, result1))  # Output: 0

result2 = bitwise_and(num1, num3)
print("num1 = {} and num3 = None, their bitwise AND is: {}".format(num1, num3, result2))  # Output: None

result3 = bitwise_and(None, num2)
print("None and num2 = {}, their bitwise AND is: {}".format(num2, result3))  # Output: None

result4 = bitwise_and(num1, num4)
print("num1 = {} and num4 = {}, their bitwise AND is: {}".format(num1, num4, result4))  # Output: 0
