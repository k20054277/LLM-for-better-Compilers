
# Define a class called Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, " + self.name)

# Create an object of the Person class called john
john = Person("John Doe", 25)

# Call the greet method on the john object
john.greet()

# Print the name and age of john
print("Name:", john.name)
print("Age:", john.age)
