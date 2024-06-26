# Demonstrate the use of False and all() in Python

# Define a list with 3 elements
my_list = [1, 2, 3]

# Check if any element in the list is less than 0 using all()
print("Using all():")
if all(x >= 0 for x in my_list):
    print("All elements are non-negative.")
else:
    print("At least one element is negative.")

# Check if any element in the list is less than 0 using False
print("\nUsing False:")
if False in (x < 0 for x in my_list):
    print("At least one element is negative.")
else:
    print("All elements are non-negative.")