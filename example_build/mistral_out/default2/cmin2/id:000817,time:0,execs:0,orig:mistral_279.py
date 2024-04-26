
def divide(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    else:
        return result

# Using the function
num1 = 10
num2 = 5
print(f"The result of {num1} divided by {num2} is {divide(num1, num2)}")

# Demonstrating raising an exception
def subtract(num1, num2):
    if num1 < num2:
        raise ValueError("Error: First number must be greater than second number")
    else:
        return num1 - num2

try:
    print(f"The result of subtracting {-5} from 5 is {subtract(-5, 5)}")
except ValueError as err:
    print(err)
