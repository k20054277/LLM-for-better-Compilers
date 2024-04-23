# Example of using and and garbage collection in Python

# Define a function to create a new object
def create_object():
  return object()

# Create an object
obj = create_object()

# Check if the object is alive
print(obj is not None)  # Output: True

# Use and operator to check if object is both alive and has reference count of 1
print(obj is not None and obj.isAlive())  # Output: True

# Assign a new value to the same variable
obj = create_object()

# Check if the object is alive again
print(obj is not None)  # Output: True

# Use and operator to check if object is both alive and has reference count of 1
print(obj is not None and obj.isAlive())  # Output: True

# Use garbage collection to free up memory
del obj

# Check if the object is no longer alive
print(obj is None)  # Output: True