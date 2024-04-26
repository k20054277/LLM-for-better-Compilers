
# Assigning None to a variable
my_variable = None
print("Value of my_variable: ", my_variable)

# Functions can return None as well
def divide(numerator, denominator):
    if denominator == 0:
        return None
    else:
        result = numerator / denominator
        return result

print("Divide 5 by 2: ", divide(5, 2))
print("Divide 5 by 0: ", divide(5, 0))

# Using None as a placeholder in a dictionary
my_dict = {"key1": 1, "key2": None}
print("Dictionary: ", my_dict)

# Checking if a variable is equal to None
if my_variable is None:
    print("my_variable is None")
else:
    print("my_variable is not None and has the value:", my_variable)
