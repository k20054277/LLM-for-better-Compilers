# Demonstrate the use of 'as' and garbage collection in Python

class Person:
    def __init__(self, name):
        self.name = name

# Create a new object of class Person
person1 = Person("Alice")

# Use 'as' to create an alias for person1
person2 = person1

print(id(person1))  # Print the id of person1
print(id(person2))  # Print the id of person2 (should be the same as person1)

# Modify the name attribute of person2
person2.name = "Bob"

print(person1.name)  # Print the name attribute of person1
print(person2.name)  # Print the name attribute of person2

# Use 'del' to delete the reference to person2
del person2

# Try to print the name attribute of person2 (should raise an error)
try:
    print(person2.name)
except NameError as e:
    print("NameError:", e)