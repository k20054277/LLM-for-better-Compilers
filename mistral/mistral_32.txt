
def divide_by_zero(num):
    result = False
    try:
        result = num / 0
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
     finally:
        return result

# Testing the function
print(divide_by_zero(10)) # Prints: Error: Division by zero is not allowed.
print(divide_by_zero(2 / 3)) # Prints: Result: 0.6666666666666667
