
class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, " + self.name)

class Child(Parent):
    def say_hello(self):
        print("Hello, " + self.name + ". I am " + str(self.age) + " years old")

# Create an instance of the Parent class
parent = Parent("John Doe", 30)

# Create an instance of the Child class
child = Child("Jane Doe", 20)

# Call the say_hello method on each instance
parent.say_hello()
child.say_hello()
