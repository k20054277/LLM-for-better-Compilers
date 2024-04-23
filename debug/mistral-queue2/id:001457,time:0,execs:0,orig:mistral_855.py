
# Defining some functions and classes for this example
def is_positive(num):
    """ checks if a number is positive """
    return num > 0

class MyNumber:
    def __init__(self, value):
        self.value = value

    def is_positive(self):
        """ checks if an instance of MyNumber is positive """
        return self.value > 0

# Testing the usage of and and isinstance()
num1 = 5
num2 = -3
num3 = MyNumber(7)

# Using 'and' to combine conditions
if is_positive(num1) and (isinstance(num2, int) or isinstance(num2, float)):
    print("Both conditions are met")
else:
    print("At least one condition is not met")

if num3.is_positive() and isinstance(num3, MyNumber):
    print("Both conditions for 'MyNumber' instance are met")
