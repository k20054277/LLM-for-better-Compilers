
# Define a class called Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __delattr__(self, attr):
        print("Attribute", attr, "deleted")

    def __str__(self):
        return "Name: " + self.name + ", Age: " + str(self.age)


# Create an instance of the Person class
person = Person("John Doe", 25)

# Print the person's information
print(person)

# Delete the person's age attribute
delattr(person, "age")

# Print the person's information after deleting the age attribute
print(person)
