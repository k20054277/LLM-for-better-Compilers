
# Defining a function that returns None
def none_function():
    return None

# Using None as a default value for a function argument
def greet(name=None):
    if name is not None:
        print("Hello, " + name)
    else:
        print("Hello, World!")

# Using lambda with None and default arguments
add = lambda x, y=0: x + y

if __name__ == "__main__":
    # Calling a function that returns None
    print(none_function())

    # Calling a function with an argument
    greet("John")

    # Calling a function without an argument
    greet()

    # Adding numbers using lambda function
    print(add(3))
    print(add(3, 4))
