
import as

# Define a class named MyClass
class MyClass:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print("Entering MyClass")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting MyClass")

with as.MyClass("John Doe") as instance:
    print(instance.name)  # Output: John Doe
    print("Inside the with statement")

print("After the with statement")
