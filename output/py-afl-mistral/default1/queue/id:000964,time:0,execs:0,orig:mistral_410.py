
# Function to calculate the square of a number, with None as default argument
def square(number=None):
    if number is None:
        print("Please provide a number")
        return
    result = number * number
    print("The square of", number, "is:", result)

# Calling the function with no argument
square()

# Calling the function with an argument
square(5)

# Assigning None to a variable and checking it with if statement
num = None
if num is None:
    print("Number is not assigned")
else:
    print("Number is:", num)
