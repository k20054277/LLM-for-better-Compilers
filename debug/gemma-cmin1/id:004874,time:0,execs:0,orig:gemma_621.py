
# This Python program demonstrates the use of True and any

# Define a list of boolean values
my_list = [True, False, True, False, True]

# Check if any of the values in the list are True
if any(True in my_list):
    print("There is a True value in the list")

# Check if all of the values in the list are True
if all(True == my_list[i] for i in range(len(my_list))):
    print("All values in the list are True")

# Check if the list is empty
if not my_list:
    print("The list is empty")
