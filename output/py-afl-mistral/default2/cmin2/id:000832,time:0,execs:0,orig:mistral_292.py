
def function_returns_none():
    """A simple function that returns None."""
    return None

def function_creates_bytes(length):
    """Function to create a bytes object of given length."""
    return bytes([i for i in range(length)])

# Function with no return statement (implicitly returns None)
def no_return_function():
    print("This is a function without a return statement.")

# Main program
if __name__ == "__main__":
    # Assigning None to a variable
    none_value = function_returns_none()
    print(f"Variable 'none_value' contains: {none_value}")

    # Creating an empty bytes object and assigning it to a variable
    empty_bytes = bytes()
    print(f"Length of empty_bytes: {len(empty_bytes)}")

    # Creating a bytes object with a length and printing its contents
    my_bytes = function_creates_bytes(5)
    print(f"Length of 'my_bytes': {len(my_bytes)}")
    print("Contents of 'my_bytes':", my_bytes.hex())

    # Manipulating bytes object using slicing and addition
    extended_bytes = b'\x01' + my_bytes + b'\x05'
    print("\nLength of 'extended_bytes':", len(extended_bytes))
    print("Contents of 'extended_bytes':", extended_bytes)

    # None vs empty bytes comparison
    empty_none = (None, bytes())
    print("\nComparing empty_none and None:")
    print(empty_none == (None,))
    print(empty_none == ())

    print("\nComparing empty_none and empty_bytes:")
    print(empty_none == (bytes(),))
    print(empty_none == (b'',))

no_return_function()
