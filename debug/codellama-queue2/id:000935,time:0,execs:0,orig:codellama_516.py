# This program demonstrates the use of None and the method method on an object

class MyClass:
    def __init__(self):
        self.x = 5

    def method(self, arg):
        if arg is None:
            print("arg is None")
        else:
            print("arg is not None")

my_obj = MyClass()

# Calling the method with a non-None argument
my_obj.method(10)  # Output: arg is not None

# Calling the method with a None argument
my_obj.method(None)  # Output: arg is None