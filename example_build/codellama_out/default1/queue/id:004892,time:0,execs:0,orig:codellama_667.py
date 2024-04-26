# Test if an object is an instance of a class
class MyClass:
    pass

x = 5
print(isinstance(x, int)) # False

y = MyClass()
print(isinstance(y, MyClass)) # True