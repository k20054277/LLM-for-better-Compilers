
# Function to divide two numbers with exception handling
def divide(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError as e:
        print("Error:", e)
        result = None
    else:
        print("Result:", result)

# Call the function with valid and invalid inputs
divide(10, 5)
divide(10, 0)
