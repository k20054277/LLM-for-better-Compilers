
# False and pass demonstration

# Define a function that returns True if the input is even, False otherwise
def is_even(n):
    return n % 2 == 0

# Pass a variable to the function and check if it's even
number = 6
if is_even(number):
    print("The number is even")

# False condition
if False:
    print("This code will not execute")

# True condition
if True:
    print("This code will execute")
