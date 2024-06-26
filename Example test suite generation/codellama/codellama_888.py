# Define a function that takes two numbers as arguments and returns their sum
def add(x, y):
  return x + y

# Define a function that takes two numbers as arguments and returns their difference
def subtract(x, y):
  return x - y

# Define a function that takes two numbers as arguments and returns their product
def multiply(x, y):
  return x * y

# Define a function that takes two numbers as arguments and returns their quotient
def divide(x, y):
  return x / y

# Create a dictionary to store the functions
functions = {
  "add": add,
  "subtract": subtract,
  "multiply": multiply,
  "divide": divide
}

# Use setattr to assign the functions to variables
setattr(functions, "sum", add)
setattr(functions, "difference", subtract)
setattr(functions, "product", multiply)
setattr(functions, "quotient", divide)

# Use and to call the functions and print their results
print("2 + 3 =", functions.add(2, 3))
print("5 - 2 =", functions.subtract(5, 2))
print("4 * 6 =", functions.multiply(4, 6))
print("10 / 2 =", functions.divide(10, 2))