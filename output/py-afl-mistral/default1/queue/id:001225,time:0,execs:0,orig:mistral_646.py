
# Simple Calculator Function (Abstraction)
def add(x, y):
    """This function takes two arguments and returns their sum"""
    return x + y

def subtract(x, y):
    """This function takes two arguments and returns the difference between them"""
    return x - y

# Main Program
if __name__ == "__main__":
    num1 = 5
    num2 = 3

    print("The sum is: ", add(num1, num2))
    print("The difference is: ", subtract(num1, num2))

    # Using True as a condition in an if statement
    if (add(num1, num2) > 5):
        print("The sum of {} and {} is greater than 5".format(num1, num2))
    else:
        print("The sum of {} and {} is less than or equal to 5".format(num1, num2))
