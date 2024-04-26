
# Function with an optional None argument
def greet(name=None):
    if name is not None:
        print("Hello, " + name)
    else:
        print("Hello")

# Function using ** for unpacking a dictionary into keyword arguments
def process_settings(settings):
    key1, value1 = settings.items()[0]
    key2, value2 = settings.items()[1:]

    print(f"Key 1: {key1}, Value 1: {value1}")
    print(f"Key 2: {key2}, Value 2: {value2}")

# Test cases
settings_1 = {"key1": "John", "key2": "Doe"}
greet()                       # Output: Hello
greet("Alice")                 # Output: Hello, Alice
process_settings(settings_1)  # Output: Key 1: key1, Value 1: John
                             #        Key 2: key2, Value 2: Doe

none_dict = {None: "default_value"}
greet()                       # Output: Hello
process_settings(none_dict)   # Output: Key 1: None, Value 1: default_value
