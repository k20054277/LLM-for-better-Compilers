
# Define a list with some boolean values and empty strings
my_list = [True, False, True, "", False, "", True]

# Iterate through the list and print the type and value of each element
for i in my_list:
    print(f"Element {my_list.index(i)}: Type={type(i)}, Value={i}")

# Use a for loop with as keyword to assign iterated values to variables
for value in (x for x in my_list if x):  # Filter out empty strings and False values
    print(f"Valid value: Type={type(value)}, Value={value}")

# Use bool function to check if an empty string or False is considered as False
print("False: ", bool(False))
print("Empty String: ", bool(""))
