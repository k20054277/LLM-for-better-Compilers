
# Function definition with input validation using assert and isinstance
def divide(num1, num2):
    assert (isinstance(num1, (int, float)) and
            isinstance(num2, (int, float))), "Both numbers should be either int or float"
     if isinstance(num1, int) and isinstance(num2, int):
         result = num1 / num2
     else:
         result = num1 // num2  # For floating point division use 'divide' operator
     return result

# Test cases for divide function
if __name__ == "__main__":
    try:
        print("Result of dividing 5 by 2.5: ", divide(5, 2.5))
    except AssertionError as e:
        print("Error:", e)

    try:
        print("Result of dividing 7 by 3: ", divide(7, 3))
    except TypeError as e:
        print("Error:", e)

    try:
        print("Result of dividing a string by an integer: ", divide("10", 2))
    except AssertionError as e:
        print("Error:", e)
