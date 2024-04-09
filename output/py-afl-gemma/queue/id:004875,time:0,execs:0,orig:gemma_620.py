
# This Python program demonstrates the use of True and all

# Create a list of boolean values
my_list = [True, False, True, False, True]

# Check if all elements in the list are True
if all(my_list[i] is True for i in range(len(my_list))):
    print("All elements in the list are True")

# Check if all elements in the list are False
if all(my_list[i] is False for i in range(len(my_list))):
    print("All elements in the list are False")

# Check if there is any True element in the list
if any(my_list[i] is True for i in range(len(my_list))):
    print("There is at least one True element in the list")

# Check if there is any False element in the list
if any(my_list[i] is False for i in range(len(my_list))):
    print("There is at least one False element in the list")
