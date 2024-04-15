
# Function that returns None if division by zero is attempted
def divide_by_two(number):
    try:
        result = number / 2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
        return None
    else:
        return result

# Function that calculates the square root of a number, or returns None if number is negative
def find_square_root(number):
    try:
        result = number ** 0.5
    except (ValueError, TypeError):
        print("Error: '{}' is not a valid number".format(number))
        return None
    else:
        return result

# Main program logic
num1 = 10
num2 = 5
num3 = -3.5

print("Result of dividing {} by 2: {}".format(num1, divide_by_two(num1)))
print("Result of finding the square root of {}: {}".format(num2, find_square_root(num2)))
print("Result of finding the square root of {}: {}".format(num3, find_square_root(num3)))
