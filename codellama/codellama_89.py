class MyClass:
    def __init__(self, x):
        self.x = x

    def get_x(self):
        return self.x

    def set_x(self, value):
        self.x = value

    def del_x(self):
        delattr(self, 'x')

my_obj = MyClass(5)
print(my_obj.get_x())  # prints 5
my_obj.set_x(10)
print(my_obj.get_x())  # prints 10
del my_obj.x
print(my_obj.get_x())  # prints None