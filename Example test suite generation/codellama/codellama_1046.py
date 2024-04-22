# Using "as" to assign a variable from a context manager
with open("example.txt") as file:
    contents = file.read()
print(contents)

# Using "try" to handle exceptions
try:
    do_something_that_might_raise_an_exception()
except Exception as e:
    print(f"An exception occurred: {e}")