
import contextlib

@contextlib.contextmanager
def my_custom_context():
    print("Entering custom context")
    yield
    print("Exiting custom context")

def custom_function():
    print("Function is executing...")
    raise Exception("An error occurred during function execution.")

if __name__ == "__main__":
    try:
        with my_custom_context():
            custom_function()
    except Exception as e:
        print(f"Error occurred: {e}")
        # handle the exception here

    print("Program continues execution...")

# This program will enter the custom context, execute the function and an error occurs.
# Then it will print the error message and exit the context, printing "Exiting custom context".
# Finally, it will continue executing the rest of the program.
