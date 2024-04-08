class MyClass:
    def __init__(self):
        self.x = 5
        self.y = "hello"

    def setattr(self, name, value):
        setattr(self, name, value)

    def delattr(self, name):
        delattr(self, name)

# Test the methods
my_obj = MyClass()
print(my_obj.x)  # Output: 5
print(my_obj.y)  # Output: "hello"

my_obj.setattr("x", 10)
print(my_obj.x)  # Output: 10
print(my_obj.y)  # Output: "hello"

my_obj.delattr("y")
print(my_obj.x)  # Output: 10
print(my_obj.y)  # Output: None