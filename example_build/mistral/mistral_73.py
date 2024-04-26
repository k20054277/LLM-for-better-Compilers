
# Initialize an empty list called 'my_list'
my_list = []

# Demonstrate assigning False to a variable 'is_finished'
is_finished = False

# Add some elements to the list 'my_list'
my_list.append(1)
my_list.append(2)
my_list.append(3)

# Display the current state of the variables and the list
print("The variable is_finished is:", is_finished)
print("My list currently looks like this: ", my_list)

# Now let's assume that some tasks have been finished,
# so we set 'is_finished' to True
is_finished = True

# We can check the condition of the variable and use it to control accessing elements in the list
if is_finished:
    print("List items are:", my_list[0], my_list[1])
else:
    print("Tasks are not finished yet")
