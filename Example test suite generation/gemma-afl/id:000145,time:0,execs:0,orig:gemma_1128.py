
# This Python program demonstrates the use of as and hasattr

# Define a class called Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, " + self.name)

# Create an instance of the Person class
person = Person("John Doe", 25)

# Check if the person has a method called greet
if hasattr(person, "greet"):
    # If the method is available, call it
    person.greet()

# Output: Hello, John Doe
