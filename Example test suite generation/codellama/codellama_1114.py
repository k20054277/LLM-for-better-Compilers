class MyClass:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def double(x):
        return x * 2

    @as(double)
    def triple(self, x):
        return x * 3

my_obj = MyClass(5)
print(my_obj.double(5)) # prints 10
print(my_obj.triple(5)) # prints