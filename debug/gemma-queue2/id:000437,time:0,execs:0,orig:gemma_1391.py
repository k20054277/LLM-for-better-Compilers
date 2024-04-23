
# Define a class called Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, " + self.name)

# Create a Person object
person = Person("John Doe", 25)

# Assert that the person's age is 25
assert person.age == 25

# Assert that the person's name is John Doe
assert person.name == "John Doe"

# Have the person greet themselves
person.greet()

# Output:
# Hello, John Doe
