class MyClass:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

my_object = MyClass(10)
print(my_object.get_value()) # prints 10

# demonstrate None object
none_object = None
if none_object is not None:
    print("None object exists")
else:
    print("None object does not exist")