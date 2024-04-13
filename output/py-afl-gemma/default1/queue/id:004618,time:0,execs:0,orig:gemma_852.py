
# This Python program demonstrates the use of and and try

# Define a function to demonstrate the use of and and try
def demonstrate_and_try():
    # Use try and except to handle an exception
    try:
        # Attempt to execute a division operation
        result = 10 / 2
        print("The result is:", result)
    except ZeroDivisionError:
        # If the division operation fails, catch the exception and print an error message
        print("Error: division by zero is not allowed")
    else:
        # If the division operation succeeds, execute this code
        print("The operation was successful")
    finally:
        # This code will always execute, regardless of whether an exception occurs or not
        print("The program has completed")

# Execute the function
demonstrate_and_try()
