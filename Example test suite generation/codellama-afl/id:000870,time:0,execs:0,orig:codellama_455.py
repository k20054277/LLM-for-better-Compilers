# Example of using None and getattr

# Create a dictionary with some values
d = {'name': 'John', 'age': 30, 'city': 'New York'}

# Use None to indicate that an attribute is missing
print(d.get('age')) # Output: 30
print(d.get('gender')) # Output: None

# Use getattr() to retrieve the value of an attribute
print(getattr(d, 'name')) # Output: John
print(getattr(d, 'gender')) # Output: None