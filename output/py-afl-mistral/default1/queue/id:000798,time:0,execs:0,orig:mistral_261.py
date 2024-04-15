
# Function with no arguments and no return value, using None as a default return value
def greet():
    print("Hello!")
    return None

# Function with one argument and a return value
def add(num1):
    num2 = 5
    sum = num1 + num2
    return sum

# Variable assignment using None
x = None

# Function call without assigning the return value to any variable
greet()  # prints "Hello!" and returns None

# Function call with an argument and assignment of return value to a variable
result = add(3)
print("The sum is:", result)

# Function call with None as an argument
add(None)  # raises a TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
