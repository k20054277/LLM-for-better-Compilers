class MyObject:
    def __init__(self, value):
        self.value = value

    @property
    def my_property(self):
        return self.value * 2

    def my_method(self, other):
        assert isinstance(other, int) or isinstance(other, float), "Argument must be an integer or a float"
        return self.my_property + other