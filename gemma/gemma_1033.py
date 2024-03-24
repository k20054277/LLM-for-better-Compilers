
import gc

# Define a class to demonstrate garbage collection
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

# Create a person object
person = Person("John Doe", 30)

# Print the person object
print(person)

# Let the person object go out of scope
person = None

# Run the garbage collector
gc.collect()

# Check if the person object has been garbage collected
if person is None:
    print("Person object has been garbage collected")
else:
    print("Person object has not been garbage collected")
