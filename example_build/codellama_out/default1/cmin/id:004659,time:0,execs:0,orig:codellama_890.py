class MyClass:
    @staticmethod
    def my_static_method(x, y):
        return x and y

print(MyClass.my_static_method(True, False)) # Output: False
print(MyClass.my_static_method(False, True)) # Output: False
print(MyClass.my_static_method(True, True)) # Output: True