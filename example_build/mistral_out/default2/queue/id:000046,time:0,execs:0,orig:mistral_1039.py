
class MyContextManager:
    def __init__(self, value):
        self.value = value

    def __enter__(self):
        print(f"Entering context manager with value: {self.value}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Exiting context manager with value: {self.value}")

if __name__ == "__main__":
    with MyContextManager("Hello") as cm:
        print("Inside the context block")
        raise ValueError("An error occurred")

# Output:
# Entering context manager with value: Hello
# Inside the context block
# Exiting context manager with value: Hello
