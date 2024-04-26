
class MyNumber:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        assert self._value is not None, "Value cannot be None"
        return self._value

    @value.setter
    def value(self, new_value):
        self.assert_valid_number(new_value)
        self._value = new_value

    def assert_valid_number(self, num):
        if not isinstance(num, (int, float)):
            msg = f"Expected number type, got {type(num)} instead"
            raise TypeError(msg)
        self.value = num

if __name__ == "__main__":
    # Valid usage
    m = MyNumber(10)
    print("Valid usage: ", m.value)

    # Assertion in setter
    try:
        m.value = "invalid"
    except AssertionError as e:
        print(f"Assertion error: {e}")

    # Setting valid number
    m.value = 20
    print("Value after setting: ", m.value)
