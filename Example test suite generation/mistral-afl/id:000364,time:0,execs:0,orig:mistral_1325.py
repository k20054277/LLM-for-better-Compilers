
class MyNumber:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def increment(self):
        self._value += 1

x = MyNumber(5)

# Using assert to check if an object is an instance of a specific class
assert isinstance(x, MyNumber), "x is not an instance of MyNumber"

# Using assert to check if the value attribute exists and is of the correct type
assert hasattr(x, 'value'), "x does not have a value attribute"
assert isinstance(x.value, int), "x's value attribute is not an integer"

# Using dir() to print out all attributes and methods of an object
print("Attributes and methods of x:")
print(dir(x))

# Testing the functionality of the class
x.increment()
assert x.value == 6
