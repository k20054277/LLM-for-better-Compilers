class MyClass:
    def __init__(self):
        self.x = 5

    def my_method(self):
        assert hasattr(self, "x"), "Object does not have attribute x"
        delattr(self, "x")

my_obj = MyClass()
assert hasattr(my_obj, "x"), "Object does not have attribute x"
delattr(my_obj, "x")