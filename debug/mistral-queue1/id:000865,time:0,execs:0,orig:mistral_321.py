
# An empty list
my_list = []

# Assigning None to a variable
none_value = None

# Assigning values to the list
my_list.append(1)
my_list.append(2)
my_list.append(3)

print("List: ", my_list)

# Check if a variable is None using 'is' keyword
if my_list is None:
    print("The list is None")
else:
    print("The list has", len(my_list), "elements.")

# Using None as an argument to a function
def greet(name=None):
    if name is None:
        print("Hello, Stranger!")
    else:
        print("Hello, ", name)

greet()  # prints 'Hello, Stranger!'
greet("Alice")  # prints 'Hello, Alice'
