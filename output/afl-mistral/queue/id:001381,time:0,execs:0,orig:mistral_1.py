
# An empty list
my_list = []

# False is a boolean value representing false
print("Is the list empty? ", bool(my_list))  # Is the list empty?  True

# Assigning False to a variable
false_value = False

# Check if a variable is False
print("Is false_value False? ", false_value)  # Is false_value False?  True

# Comparison operators also return False if conditions are not met
print("Is 10 greater than 20? ", 10 > 20)  # Is 10 greater than 20?  False

# None is a special value representing the absence of any object or data
my_number = None

# Check if a variable is None
print("Is my_number defined? ", my_number is not None)  # Is my_number defined?  False

# Assigning None to a list
my_list = None

# Check if a list is None
print("Is my_list None? ", my_list is None)  # Is my_list None?  True

# Comparison of None with other values
print("Is None equal to an empty list? ", None == [])  # Is None equal to an empty list?  False
print("Is None less than an empty list? ", None < [])  # Is None less than an empty list?  False
print("Is None greater than an empty list? ", None > [])  # Is None greater than an empty list?  False
--- 85.3 seconds ---
