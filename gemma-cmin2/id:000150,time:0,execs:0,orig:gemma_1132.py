
# Define a function named as_id
def as_id(x):
    return x.id

# Create a list of objects
objects = [
    {"name": "John Doe", "id": 1},
    {"name": "Jane Doe", "id": 2},
    {"name": "Peter Pan", "id": 3}
]

# Use as_id function to get the IDs of the objects
ids = [as_id(obj) for obj in objects]

# Print the IDs
print(ids)

# Output:
# [1, 2, 3]
