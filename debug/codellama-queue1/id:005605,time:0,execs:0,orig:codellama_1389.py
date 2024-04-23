class AssertExample:
    def __init__(self, value):
        self.value = value
    
    def test(self):
        assert self.value == 5, "Value must be 5"
        print("Value is", self.value)

example = AssertExample(10)
example.test()