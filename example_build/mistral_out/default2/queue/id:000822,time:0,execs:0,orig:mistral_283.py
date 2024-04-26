
# Assigning None to a variable
x = None
print("Value of x:", x)

# Function returning None as default value
def function():
    return None

print("Function returned:", function())

# Using None in conditional statements
if x is None:
    print("x is None")
else:
    print("x is not None")
    
# With statement for managing context of an object
class MyContextManager:
    def __init__(self, value):
        self.value = value

    def __enter__(self):
        print(f"Entering context with value: {self.value}")
        return self.value

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")

# Using with statement
with MyContextManager(None) as none_context:
    pass
