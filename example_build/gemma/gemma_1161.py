
class MyClass:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def greet(name):
        print("Hello, " + name)

    def say_hello(self):
        MyClass.greet(self.name)

# Create an instance of the MyClass class
my_object = MyClass("John")

# Call the static method
MyClass.greet("Jane")

# Call the instance method
my_object.say_hello()
