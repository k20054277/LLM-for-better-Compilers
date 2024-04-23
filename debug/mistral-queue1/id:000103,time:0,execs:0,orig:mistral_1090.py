
# Import math module and alias sin function as ms for demonstration purpose
import math as ms

def square_root(number):
    """This function calculates the square root of given number."""
     result = ms.sqrt(number)
     return result

# Assign the value of 100 to a variable named 'num' in the global scope
globals()['num'] = 100

if __name__ == "__main__":
    # In the main block, we use as keyword to assign an alias name 'sr' to the function square_root()
    sr as root = square_root
     print("The square root of {} is:".format(num))
     print(root(num))

# Now, let's demonstrate the usage of globals() function
print("\nUsing globals():")
print("Value of number: ", num)
print("Square root of number: ", ms.sqrt(globals()['num']))
