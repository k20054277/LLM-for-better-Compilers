
import gc

# Define a class to demonstrate garbage collection
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("Goodbye,", self.name)

# Create a few Person objects
person1 = Person("John Doe", 25)
person2 = Person("Jane Doe", 30)
person3 = Person("Bob Doe", 40)

# The following line will cause person2 to be garbage collected
person2 = None

# Run the garbage collector
gc.collect()

# Check if person2 has been garbage collected
if person2 is None:
    print("Person 2 has been garbage collected")

# Output
# Goodbye, Jane Doe
# Person 2 has been garbage collected
