
# Define a function with try, except, and finally blocks
def foo():
    try:
        print("Inside try block")
        raise ValueError("Error occurred")
    except ValueError as e:
        print("Inside except block, error:", e)
    finally:
        print("Inside finally block")

# Call the function
foo()

# Output:
# Inside try block
# Inside except block, error: Traceback (most recent call last):
#   File "program.py", line 4, in foo
#     raise ValueError("Error occurred")
# Inside finally block
