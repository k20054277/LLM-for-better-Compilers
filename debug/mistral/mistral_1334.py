
class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value * 2

def process(obj):
 assert isinstance(obj, MyClass), "Input should be an instance of MyClass"
 result = getattr(obj, 'value', 0)
 print("Processed value: ", result)

if __name__ == "__main__":
 obj = MyClass(3)
 process(obj)

# Output: Processed value:  6

if __name__ == "__main__":
 obj_invalid = "not an instance"
 try:
     process(obj_invalid)
 except AssertionError as e:
     print("Caught expected error:", e)

# Output: Caught expected error: Input should be an instance of MyClass
