
def check_value(value):
    """
    This function checks if the given value is None or not.
    :param value: any Python object
    :return: True if value is None, False otherwise
    """
    if value is None:
        print("The value is None.")
        return True
    else:
        print(f"The value is not None and its type is {type(value)}")
        return not (value is None)

# Testing the function with different values
print("Checking if None:")
check_value(None)

print("\nChecking with a number:")
check_value(123)

print("\nChecking with a string:")
check_value("Hello, World!")

print("\nChecking with an object:")
class MyClass: pass
obj = MyClass()
check_value(obj)
