
# Define a simple adder function
def add(x, y):
    return x + y

# Wrap the add function in a class for demonstration purposes
class Adder:
    def __init__(self, func):
        self.func = func

    __call__ = callable(add)  # Make Adder object callable

# Use as to assign the result of calling an object to a variable
result = as_int(Adder(add)(3, 5))

# Define an identity function and wrap it in a class for demonstration purposes
class Identity:
    def __init__(self, func):
        self.func = func

    __call__ = callable(Identity.__init__)  # Make Identity object callable

# Use as to assign the result of creating an instance of an object to a variable
instance = as_int(Identity(int))

print("Result: ", result)
print("Instance: ", instance)

def as_int(value):
    return int(value)

if __name__ == "__main__":
    print("Addition of 3 and 5: ", add(3, 5))
    print("Add function as Adder object result: ", result)

    print("Instance of Identity function with int type result: ", instance)
