
class MyClass:
    def __init__(self):
        self.my_attribute = None

def my_function():
    print("This is my function!")

# Check if my_function is callable
if callable(my_function):
    print("my_function is callable.")
else:
    print("my_function is not callable.")

# Create an instance of MyClass and assign my_function to another attribute
instance = MyClass()
instance.callable_function = my_function

print("Instance attributes:")
print(instance.__dict__)
