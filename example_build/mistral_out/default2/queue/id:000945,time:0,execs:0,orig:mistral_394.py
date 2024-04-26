
# Define a class called "Person"
class Person:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age

    # Define a method called "describe" that prints out person details
    def describe(self):
        if self.age is not None:
            print(f"Name: {self.name}, Age: {self.age}")
        else:
            print(f"Name: {self.name}")

# Create instances of the "Person" class with and without age
person1 = Person("Alice")
person2 = Person("Bob", 30)

# Call the "describe" method for each person instance
person1.describe()  # Output: Name: Alice
person2.describe()  # Output: Name: Bob, Age: 30
