def my_function(obj, attr):
    return obj[attr] if isinstance(obj, dict) else getattr(obj, attr)

# Test the function
obj = {"a": 1, "b": 2}
print(my_function(obj, "a")) # Output: 1
print(my_function(obj, "b")) # Output: 2

obj = MyClass()
print(my_function(obj, "x")) # Output: 3
print(my_function(obj, "y")) # Output: 4

class MyClass:
    def __init__(self):
        self.x = 3
        self.y =