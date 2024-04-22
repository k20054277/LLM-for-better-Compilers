
# Define a custom class named 'MyNumber'
class MyNumber:
    def __init__(self, value):
        self.value = value

# Function that checks if given argument is True or not
def is_boolean(arg):
    return isinstance(arg, bool) and arg

# Function that checks if given number is an instance of 'MyNumber' class
def is_my_number(num):
    return isinstance(num, MyNumber)

# Test cases
print("is_boolean(True) =", is_boolean(True))        # True
print("is_boolean(5) =", is_boolean(5))            # False
print()

print("is_my_number(MyNumber(3)) =", is_my_number(MyNumber(3)))      # True
print("is_my_number(3) =", is_my_number(3))          # False
