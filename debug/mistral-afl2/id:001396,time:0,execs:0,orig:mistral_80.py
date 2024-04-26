
class MyObject:
    def __init__(self, value):
        self.value = value

# Creating instances of MyObject
obj1 = MyObject(True)
obj2 = MyObject(False)

# Demonstrating False and object comparison
print(type(False))       # <class 'bool'>
print(type(obj1))       # <class '__main__.MyObject'>
print(False == obj1.value)   # False
print(False is obj1)    # False

# Comparing two objects with different values
print(obj1 == obj2)    # False
print(obj1 is obj2)    # False
