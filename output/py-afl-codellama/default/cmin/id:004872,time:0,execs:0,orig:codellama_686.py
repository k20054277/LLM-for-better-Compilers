class MyClass(object):
    def __init__(self):
        self.x = 5

    def my_method(self, y):
        if y > self.x:
            return True
        else:
            return False

class MySubclass(MyClass):
    def __init__(self):
        super().__init__()
        self.y = 10

    def my_subclass_method(self, z):
        if z > self.y:
            return True
        else:
            return False