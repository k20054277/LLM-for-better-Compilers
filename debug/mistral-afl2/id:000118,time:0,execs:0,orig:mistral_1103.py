
# Function that takes multiple key-value pairs as arguments
def process_args(*args):
    # Unpack the argument list into separate variables using as keyword
    key1, value1 = args[0], args[1]
    key2, value2 = args[2:]

    # Print unpacked variables
    print("Key 1: ", key1)
    print("Value 1: ", value1)
    print("Key 2: ", key2)
    print("Value 2: ", value2)

# Local function with some local variables
def local_function():
    local_var1 = "Local Variable 1"
    local_var2 = "Local Variable 2"

# Calling the process_args function and passing arguments using tuples
process_args(("Key1", "Value1"), ("Key2", "Value2"))

# Calling the local_function and getting local variables using locals()
locals_dict = locals()
print("\nLocals in the local_function:")
for key, value in locals_dict.items():
    if not (key.startswith("__") or callable(key)):  # ignore special names and functions
        print(f"{key}: {value}")
