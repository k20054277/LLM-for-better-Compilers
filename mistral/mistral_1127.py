
class Base:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello from Base: {self.name}"

class Derived(Base):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def greet(self):
        return f"Hello from Derived: {self.name}, age is {self.age}"
