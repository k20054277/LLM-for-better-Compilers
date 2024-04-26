
class MyNumber:
    def __init__(self, value):
        self.value = value
        assert value >= 0, "Value should be non-negative"

# Using the MyNumber class and the assert statement
if __name__ == "__main__":
    number1 = MyNumber(5)
    number2 = MyNumber(-3)

    print("number1.value =", number1.value)
    print("number2.value =", number2.value)
