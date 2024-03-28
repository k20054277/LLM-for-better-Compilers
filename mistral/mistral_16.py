
try:
    # Define a list with one element, which is not a number
    numbers = [42]
    non_number = "hello"
    new_list = numbers + [non_number]
    
except TypeError as error:
    print(f"An error occurred: {error}")
    # In this example, we'll just print the error message, but in a real application, you would want to handle it appropriately
    
else:
    # This block is executed if no exceptions are raised during try execution
    print("The list was successfully modified.")
    print(new_list)
    
finally:
    # This block is always executed, regardless of exception handling
    print("Cleanup operations go here, such as closing files or releasing resources.")

# Since adding a non-number to a list raises a TypeError, the except block will be executed
