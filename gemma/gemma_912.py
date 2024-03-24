
# Define a class called Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

# Create a person object
person = Person("John Doe", 25)

# Use the setattr method to modify the person's age
setattr(person, "age", 30)

# Print the person's information
print(person)
