# Define a function that returns True if the user input is "yes" or "y", False otherwise
def check_input(input):
    return input.lower() in ("yes", "y")

# Use exec to execute a string of code that uses the check_input function
exec("print('Hello, world!') if check_input('yes') else print('Goodbye, world!')")