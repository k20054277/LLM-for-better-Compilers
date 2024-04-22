class MyClass:
    def __init__(self, x):
        self.x = x
    
    def __str__(self):
        return f"MyClass({self.x})"
    
    def __repr__(self):
        return f"MyClass({self.x})"

obj1 = MyClass(3)
print(obj1) # Output: MyClass(3)
print(repr(obj1)) # Output: MyClass(3)

obj2 = MyClass("hello")
print(obj2) # Output: MyClass('hello')
print(repr(obj2)) # Output: MyClass('hello')