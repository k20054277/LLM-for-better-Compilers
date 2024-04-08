
class MyNumber:
    def __init__(self, value=0):
        self._value = value

    def set_value(self, new_value):
        self._value = new_value

    def adjust_value(self, amount):
        # Using assert statement to ensure 'amount' is a multiple of 3.
        assert amount % 3 == 0, "Amount should be a multiple of 3."

        # Using modulus operator '%=' to get the remainder of division operation.
        self._value %= amount

number = MyNumber()
number.set_value(4)
number.adjust_value(12)
print("Adjusted value:", number._value)

number.set_value(10)
number.adjust_value(3)
print("Adjusted value after adjusting with a multiple of 3:", number._value)

number.adjust_value(5)
# Assertion error will be raised since '5' is not a multiple of 3.
