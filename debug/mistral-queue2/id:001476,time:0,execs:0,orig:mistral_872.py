
class MyClass:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def __truthvalue__(self):
        if self.value1 and self.value2:
            return True
        else:
            return False

a = MyClass(True, True)
print(bool(a))  # Output: True

b = MyClass(False, True)
print(bool(b))  # Output: False

c = MyClass(False, False)
print(bool(c))  # Output: False
