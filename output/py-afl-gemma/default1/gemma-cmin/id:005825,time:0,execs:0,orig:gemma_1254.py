
# Define a function to demonstrate as and dependency
def demonstrate_as_and_dependency(name, age):
    print(f"Hello, {name}. You are {age} years old.")

# Create an object
person = {"name": "John Doe", "age": 25}

# Use as and dependency to access attributes of the object
demonstrate_as_and_dependency(person["name"], person["age"])
