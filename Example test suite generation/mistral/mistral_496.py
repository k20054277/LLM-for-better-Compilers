
# Define a function that takes one argument which is optional and has a default value of None
def greet(name=None):
    if name is not None:
        print("Hello, " + name)
    else:
        print("Hello!")

# Call the greet function without an argument, it will print "Hello!"
greet()

# Call the greet function with an argument, it will print "Hello, <argument>"
greet("Alice")

# Assign None to a variable
none_var = None
print(none_var)  # prints: None

# Using () (parentheses) in Python is used for different purposes such as function calls, tuples, etc. Here's an example of using () with a tuple:

# Define a tuple using ()
numbers = (1, 2, 3, 4, 5)
print(type(numbers))  # prints: <class 'tuple'>

# Accessing elements in a tuple using index and ()
print(numbers[0])  # prints: 1
print(numbers[-1])  # prints: 5
