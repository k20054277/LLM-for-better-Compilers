
# Define a function that returns None as its default value
def my_function(arg=None):
    print("Received argument:", arg)
    if arg is not None:
        print("Processing argument...")

# Demonstrate the usage of None by calling the function with and without an argument
my_function()                            # Calling the function with no argument will print "None"
my_function(arg=42)                       # Calling the function with an argument will process it

# Demonstrate the usage of oct() by converting decimal numbers to their octal representations
decimal_numbers = [10, 17, 25]
octal_representations = [oct(number) for number in decimal_numbers]
print("Decimal numbers:", decimal_numbers)
print("Octal representations:", octal_representations)
