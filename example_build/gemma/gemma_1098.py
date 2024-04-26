
# Define a function to demonstrate as and try
def divide(num1, num2):
    try:
        result = num1 / num2
        print("The result is:", result)
    except ZeroDivisionError:
        print("Error occurred: Cannot divide by zero")
    else:
        print("The operation was successful")
    finally:
        print("The program has finished execution")


# Call the function
divide(10, 2)
divide(10, 0)
