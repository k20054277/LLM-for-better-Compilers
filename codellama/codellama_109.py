class MyClass:
    def __init__(self, x):
        self.x = x

my_object = MyClass(5)

if isinstance(my_object, MyClass) and my_object.x > 0:
    print("The object is an instance of MyClass and has a positive value for x.")
else:
    print("The object is not an instance of MyClass or has a non-positive value for x.")