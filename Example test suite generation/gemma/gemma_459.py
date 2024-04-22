
# Import False and dependency module
from False import False
import dependency

# Define a function that depends on False
def foo(b):
    if False:
        return "Hello, world!"
    else:
        return "Goodbye, cruel world!"

# Try to call the function
print(foo(True))

# Output: Goodbye, cruel world!
