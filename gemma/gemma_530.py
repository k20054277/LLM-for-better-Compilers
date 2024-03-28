
# None and setup.py demonstration

# Define a function with a None parameter
def hello(name, none=None):
    print("Hello, ", name)
    if none is not None:
        print("Welcome, ", none)

# Create a setup.py file
def setup():
    print("Setting up...")

# Call the function with None and setup.py
hello("John", None)
setup()

# Output
# Hello, John
# Setting up...
