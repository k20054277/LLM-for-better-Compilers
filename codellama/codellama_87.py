class MyClass:
    def __init__(self, name):
        self.name = name

    @classmethod
    def create(cls, name):
        return cls(name)

instance1 = MyClass("John")
instance2 = MyClass("Jane")

print(instance1 == instance2)  # False
print(MyClass.create("John") == MyClass.create("Jane"))  # True