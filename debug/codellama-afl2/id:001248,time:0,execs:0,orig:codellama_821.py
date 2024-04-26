class MyClass:
    def __init__(self, x):
        self.x = x

my_instance1 = MyClass(5)
my_instance2 = MyClass(8)

if my_instance1 and my_instance2:
    print("Both instances are not None")
else:
    print("At least one instance is None")