
# Define a class that implements a context manager
class MyContextManager:
    def __init__(self, value):
        self.value = value

    def __enter__(self):
        print("Entering context")
        self.original_value = self.value
        self.value = self.value + 10

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")
        self.value = self.original_value


# Use the context manager
with MyContextManager(5):
    print(f"The value is: {MyContextManager.value}")

# Print the value after exiting the context
print(f"The value is: {MyContextManager.value}")
