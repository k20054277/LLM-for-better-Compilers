class MyClass:
    def __init__(self, x):
        self.x = x

    @classmethod
    def create_object(cls, x):
        return cls(x)

my_object = MyClass.create_object(10)
print(my_object.x) # prints