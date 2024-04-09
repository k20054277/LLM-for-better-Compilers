
# False and list

my_list = [1, 2, 3, 4, 5]

# Check if the list is empty
if not my_list:
    print("The list is empty")

# Iterate over the list
for item in my_list:
    # Print each item
    print(item)

# Check if the list contains a False value
if False in my_list:
    print("The list contains a False value")

# Print the truth value of the list
print(bool(my_list))

# Output
# The list is empty
# 1
# 2
# 3
# 4
# 5
# The list contains a False value
# True
