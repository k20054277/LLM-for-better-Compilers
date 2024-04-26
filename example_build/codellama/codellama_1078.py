class MyClass:
    def __init__(self):
        self.my_attribute = "Hello, world!"

obj = MyClass()

# using as
print(obj.my_attribute)

# using hasattr
if hasattr(obj, "my_attribute"):
    print("The object has an attribute named 'my_attribute'")
else:
    print("The object does not have an attribute named 'my_attribute'")