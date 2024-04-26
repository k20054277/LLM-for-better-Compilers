
# This Python program demonstrates the use of False and all

# Create a list of boolean values
my_list = [True, False, True, False, True]

# Check if all elements in the list are False
if all(x == False for x in my_list):
    print("All elements in the list are False")

# Check if any element in the list is False
if any(x == False for x in my_list):
    print("There is a False element in the list")

# Print the list
print(my_list)
