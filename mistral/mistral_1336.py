
class MyNumber:
    def __init__(self, value):
        self.value = value

def is_positive(number):
    assert hasattr(number, 'value'), "MyNumber instance must have a 'value' attribute"
    if number.value > 0:
        return True
    else:
        raise ValueError("Number must be positive")

# Test the function
num1 = MyNumber(5)
assert is_positive(num1), "Number should be positive"

num2 = MyNumber(-3)
assert is_positive(num2), "Number should be positive" # This will raise an AssertionError since num2's value is negative
