
# Define some variables with different values, including None
num1 = 5
num2 = 10
num3 = None
num4 = 15

# Use max() to find the maximum between num1, num2 and num3 (which is assumed to be None)
max_num = max(num1, num2, num3)

print("The maximum number among", num1, ",", num2, ", and", num3,"is: ", max_num)

# When max() function is called with one argument which is None, it returns None.
none_check = max(None)
print("Maximum of None is:", none_check)

# We can also use max() with a list or tuple
numbers = [3, 6, None, 8, 12]
max_number = max(numbers)
print("The maximum number in the list is:", max_number)
