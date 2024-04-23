
# Define a variable with None value
none_value = None
print(none_value)

# Function returning None as default value
def greet():
    return None
print(greet())

# Using None as an argument for a function
def print_if_not_none(data=None):
    if data is not None:
        print("Data:", data)
print_if_not_none()
