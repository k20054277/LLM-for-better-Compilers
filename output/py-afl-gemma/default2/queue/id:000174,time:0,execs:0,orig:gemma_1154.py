
# Define a class called Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}"

# Create a person object
person = Person("John Doe", 30)

# Print the person object
print(person)

# Print the person object as a string
print(str(person))