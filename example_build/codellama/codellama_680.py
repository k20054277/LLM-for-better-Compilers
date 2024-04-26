# Test whether an object is true

class MyObject:
    def __init__(self, x):
        self.x = x

    def __bool__(self):
        return self.x > 0

my_object = MyObject(5)
print(bool(my_object)) # Output: True

# Test whether an object has a property

class MyObject2:
    def __init__(self, x):
        self.x = x

my_object2 = MyObject2({"a": 1, "b": 2})
print(hasattr(my_object2, "a")) # Output: True