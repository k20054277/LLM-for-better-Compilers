
class Parent:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, " + self.name)

class Child(Parent):
    def say_hello(self):
        print("Hello, " + self.name + "!")

    def test(self):
        assert self.name == "John Doe"
        super().say_hello()

child = Child("John Doe")
child.test()
