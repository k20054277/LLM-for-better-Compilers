class MyClass:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

my_object = MyClass("Alice")
print(my_object.get_name()) # Output: Alice
my_object.set_name("Bob")
print(my_object.get_name()) # Output: Bob