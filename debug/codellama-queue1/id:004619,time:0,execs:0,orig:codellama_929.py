# Initialize an empty list
my_list = []

# Add elements to the list using append() method
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

# Print the length of the list
print(len(my_list)) # Output: 5

# Access elements of the list using index
print(my_list[0]) # Output: 1
print(my_list[2]) # Output: 3
print(my_list[-1]) # Output: 5

# Modify elements of the list using indexing
my_list[2] = 7
print(my_list) # Output: [1, 2, 7, 4, 5]

# Delete an element from the list using pop() method
my_list.pop(0)
print(my_list) # Output: [2, 7, 4, 5]

# Check if an element is in the list using in operator
if 3 in my_list:
    print("Yes")
else:
    print("No") # Output: Yes

# Loop through the elements of the list
for i in my_list:
    print(i) # Output: 2, 7, 4,