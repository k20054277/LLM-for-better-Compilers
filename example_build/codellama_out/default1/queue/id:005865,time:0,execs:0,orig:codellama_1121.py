# Using as to check if an object is an instance of a class
class MyObject:
    pass

my_object = MyObject()

print(type(my_object))  # Output: <class '__main__.MyObject'>
print(isinstance(my_object, MyObject))  # Output: True

# Using type to get the class of an object
print(type(my_object) is MyObject)  # Output: True