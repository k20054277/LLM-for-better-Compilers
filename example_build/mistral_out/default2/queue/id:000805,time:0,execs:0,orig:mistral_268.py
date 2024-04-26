
# Define a Person class with __init__ method that accepts optional parameters
class Person:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

# Import some modules and alias specific functions or constants using 'from'
from math import sqrt, pi

# Create a new Person instance with None values for name and age
person = Person(None, None)

print("Person:")
if person.name is not None:
    print(f"Name: {person.name}")
else:
    print("Name is None.")

if person.age is not None:
    print(f"Age: {person.age}")
else:
    print("Age is None.")

# Demonstrate usage of 'None' and imported functions
if person.name is None:
    new_name = input("Enter name: ")
    person = Person(new_name, None)
    
print(f"Square root of 16: {sqrt(16)}")
print(f"Pi value: {pi}")
