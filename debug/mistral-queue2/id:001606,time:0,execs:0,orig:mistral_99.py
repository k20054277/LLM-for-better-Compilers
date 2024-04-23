
# Define a tuple with some values
my_tuple = (1, "apple", 3.14, True)

# Use False value in a conditional statement
if not my_tuple[2]:  # checking if the second element is False (false is considered as 0 in Python)
    print("The second element is False or 0")
else:
    print("The second element is not False or 0")

# Use False value to check if a tuple is empty
if not my_tuple:
    print("The tuple is empty")
else:
    print("The tuple has some elements")

# Use False as default value for a function
def greet(name=""):
    if not name:
        name = "Anonymous"
    print("Hello, " + name)

greet()  # prints "Hello, Anonymous"
greet("Alice")  # prints "Hello, Alice"
