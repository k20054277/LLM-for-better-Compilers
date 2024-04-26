
import sys

# Define a class called Foo
class Foo:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, " + self.name)

# Create an instance of the Foo class
foo = Foo("John")

# Use getattr to access the say_hello method and call it
getattr(foo, "say_hello")()

# Output: Hello, John
print(foo.name)
print(getattr(foo, "name"))

# False check
if getattr(foo, "say_goodbye") is False:
    print("say_goodbye does not exist")

# Output: say_goodbye does not exist
