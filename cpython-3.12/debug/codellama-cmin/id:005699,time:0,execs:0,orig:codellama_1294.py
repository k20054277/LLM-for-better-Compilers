class MyClass:
    def __init__(self, x):
        self.x = x

    @classmethod
    def from_string(cls, string):
        assert isinstance(string, str)
        return cls(int(string))

obj1 = MyClass.from_string("10")
print(obj1.x) # Output: 10

obj2 = MyClass.from_string(10)
print(obj2.x) # Output: 10

try:
    obj3 = MyClass.from_string(None)
except AssertionError as e:
    print("Assertion error:", e)
# Output: Assertion error: string must be a string, not NoneType