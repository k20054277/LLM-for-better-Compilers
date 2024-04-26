
class ContextManager:
    def __init__(self, value):
        self.value = value

    def __enter__(self):
        print("Entering context with value:", self.value)

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context with value:", self.value)

with ContextManager(10):
    print("Inside context:")
    print("Value:", ContextManager.value)

print("After context:")
print("Value:", ContextManager.value)
