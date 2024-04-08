
class MyContextManager:
    def __init__(self):
        self.value = "Initial value"

    def __enter__(self):
        print(f"Entering context manager with value: {self.value}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"An exception occurred: {exc_val}.")
        else:
            print("Exiting context manager with value:", self.value)

if __name__ == "__main__":
    # Using False in an assignment and comparison
    a = False
    b = 0
    if not a:
        print("False is considered as an empty or false value.")
    elif b > 5:
        print(f"Number {b} is greater than 5.")
    else:
        print("The conditions are not met.")

    # Using with statement for context manager
    with MyContextManager() as cm:
        cm.value = "New value"
        print("Before exiting context manager, the value is:", cm.value)
