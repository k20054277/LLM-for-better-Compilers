
# Define a function that returns None
def greet(name):
    print("Hello, " + name)
    return None

# Deploy the function
greet("John")
greet("Jane")

# Check if the function returned None
if greet( "Jack") is None:
    print("The function returned None")