
# List of tuples - first name and last name
full_names = [("John", "Doe"), ("Jane", "Smith"), ("Mike", "Johnson")]

# Extracting first names into one list and last names into another list using zip()
first_names, last_names = zip(*full_names)

# Converting tuples to lists using the 'as' keyword
first_names = list(map(lambda x: x[0], first_names))
last_names = list(map(lambda x: x[0], last_names))

# Printing the extracted first and last names
print("First Names: ", first_names)
print("Last Names :", last_names)
