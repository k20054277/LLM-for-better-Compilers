
# Define a dictionary with some keys and values
my_dict = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
}

# Use an if statement with the 'and' keyword to check if a condition is met
if my_dict and 'name' in my_dict:
    print("The name is:", my_dict['name'])
else:
    print("Dictionary is empty or 'name' key is not present.")

# Use the dir() function to list all attributes and methods of an object or built-in functions
print("\nListing all attributes and methods of the dictionary object using dir():")
print(dir(my_dict))
