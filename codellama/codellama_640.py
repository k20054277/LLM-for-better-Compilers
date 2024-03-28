# Check if any element in a list is true
my_list = [False, False, False, True]
if any(my_list):
    print("At least one element is true")
else:
    print("No elements are true")

# Check if all elements in a list are true
my_list = [True, True, True, True]
if all(my_list):
    print("All elements are true")
else:
    print("Not all elements are true")