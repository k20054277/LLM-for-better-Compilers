
# Define a class called Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

# Create a person object
person = Person("John Doe", 25)

# Assert that the person's name is John Doe
assert person.get_name() == "John Doe"

# Set the person's age to 30
person.age = 30

# Assert that the person's age has changed to 30
assert person.get_age() == 30

# Print the person's name and age
print("Name:", person.get_name())
print("Age:", person.get_age())
