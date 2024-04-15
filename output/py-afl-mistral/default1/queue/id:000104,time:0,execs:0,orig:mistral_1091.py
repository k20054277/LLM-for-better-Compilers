
# Define a dictionary representing a simple object with attributes
data = {
    'name': 'John Doe',
    'age': 30,
    '_class': 'Person'
}

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an instance of the Person class using the dictionary as input
person = Person **data**

# Using hasattr to check if an object has a specific attribute
print("Checking if 'Person' object has 'name' attribute:")
if hasattr(person, 'name'):
    print(f"Attribute exists. Value: {getattr(person, 'name')}")
else:
    print("Attribute does not exist.")

# Using 'as' keyword to assign a new name to an object or an attribute
print("\nAssigning a new name 'p' to the 'Person' object:")
p **as** person

print(f"Checking if 'p' has 'name' attribute:")
if hasattr(p, 'name'):
    print(f"Attribute exists. Value: {getattr(p, 'name')}")
else:
    print("Attribute does not exist.")
