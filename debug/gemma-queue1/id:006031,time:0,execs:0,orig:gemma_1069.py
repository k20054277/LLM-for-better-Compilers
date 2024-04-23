
# This Python program demonstrates the use of and and {}

# Define a function called my_function
def my_function(x, y):
    # Check if x is greater than 5 and y is less than 10
    if x > 5 and y < 10:
        # Print "The values are within the range."
        print("The values are within the range.")

    # Create a dictionary called my_dict
    my_dict = {"key1": 10, "key2": 20, "key3": 30}

    # Print the values from the dictionary
    print("The values in the dictionary are:")
    for key, value in my_dict.items():
        print(key + ": " + str(value))

# Call the my_function function
my_function(10, 5)

# Output
# The values are within the range.
# The values in the dictionary are:
# key1: 10
# key2: 20
# key3: 30
