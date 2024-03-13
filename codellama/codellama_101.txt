class MyClass:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

my_object = MyClass(3, 4)

if hasattr(my_object, "x") and hasattr(my_object, "y"):
    print("Both attributes are present.")
else:
    print("One or both attributes are missing.")