
class MyContextManager:
    def __init__(self, value):
        self.value = value

    def __enter__(self):
        print(f"Entering context with value: {self.value}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"An error occurred: {exc_type}, {exc_val}")
        else:
            print("Leaving context")

def function_that_might_raise():
    try:
        raise Exception("An error occurred")
    finally:
        print("Finally block is always executed")

if __name__ == "__main__":
    value = 10
    
    with MyContextManager(value) as context:
        function_that_might_raise()

    print("Function call completed successfully, current value is: ", value)
