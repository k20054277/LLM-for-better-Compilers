
# This function takes one parameter 'num' which is an integer
# The default value for this parameter is 0 if no argument is passed
def square(num=0):
    # If num is less than or equal to 0, then the following block is executed
    if num <= 0:
        print("Square root of negative number cannot be calculated.")
        return -1
    
    # Calculate the square of the given number
    result = num ** 2
    print(f"The square of {num} is {result}")

# Calling the function with positive numbers
square(4)
square(5)

# Calling the function without any argument, so 'num' will have its default value '0'
square()

# Calling the function with a negative number
square(-3)
