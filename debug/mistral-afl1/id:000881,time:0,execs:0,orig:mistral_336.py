
# Define my_function() to return None if no argument is passed, else return range object
def my_function(num=None):
    if num is None:
        print("No argument provided.")
        return None
    else:
        print(f"Argument provided: {num}")
        return range(num)

# Calling my_function() without arguments
print(my_function())

# Calling my_function() with an argument
print(list(my_function(5)))  # Convert the range object to a list for printing purpose.
