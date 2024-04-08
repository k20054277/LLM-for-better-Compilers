
# This function takes an argument, but it doesn't need to have a value passed to it.
def print_message(message=None):
    if message is not None:
        print(message)
    else:
        print("No message provided.")

# Create an empty dictionary
my_dict = {}

# Add some key-value pairs to the dictionary
my_dict["key1"] = "value1"
my_dict["key2"] = 42
my_dict["key3"] = None

print("Dictionary: ", my_dict)

# Access values using keys
print("Value of key1: ", my_dict["key1"])
print("Value of key2: ", my_dict["key2"])
print("Value of key3: ", my_dict["key3"])

# Try to access a non-existent key
try:
    print("Value of key4: ", my_dict["key4"])
except KeyError as e:
    print(f"KeyError: {e}")

# Call the function with a message
print_message("Hello, world!")
# Call the function without a message
print_message()
