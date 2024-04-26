
# Define a class called Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Define a method to set the age of a person
    def set_age(self, new_age):
        self.age = new_age

# Create a person object
person = Person("John Doe", 25)

# Set the age of the person to 30
person.set_age(30)

# Print the name and age of the person
print("Name:", person.name)
print("Age:", person.age)
