# Demonstrate the use of False and any() in Python

print("Demonstrating the use of False and any() in Python")

# Example 1: Using False as an argument to any()
my_list = [1, 2, 3, 4, 5]
result = any(False for x in my_list)
print(result) # Output: False

# Example 2: Using a list of booleans as an argument to any()
my_list = [True, True, False, True]
result = any(my_list)
print(result) # Output: True