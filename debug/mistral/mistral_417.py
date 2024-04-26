
# Define a simple function that returns None
def my_function():
    print("This function will return None.")
    return None

# Define a dictionary as a namespace for our custom objects
custom_namespace = {
    "my_variable": 42,
    "another_function": lambda: "Hello, World!"
}

# Call the function and assign its result to a variable
result = my_function()
print("The result of my_function is:", result)

# Access the custom namespace and use its contents
print("Value of my_variable in the custom namespace:", custom_namespace["my_variable"])
print("Another function in the custom namespace returns:", custom_namespace["another_function"]())
