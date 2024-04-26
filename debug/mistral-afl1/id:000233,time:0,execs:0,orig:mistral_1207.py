
# Define a function that may raise an exception
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print("An error occurred:", e)
        return None
    else:
        print("Result of division:", result)
        return result

# Call the divide_numbers function with valid input
divide_numbers(10, 2)

# Call the divide_numbers function with invalid input
try:
    divide_numbers(5, 0)
except Exception as e:
    print("An error occurred:", e)
finally:
    print("Division is now complete")
