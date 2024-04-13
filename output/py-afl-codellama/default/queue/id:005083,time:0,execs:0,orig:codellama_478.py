class MyClass:
    def __init__(self, x):
        self.x = x

    @staticmethod
    def my_function(x):
        print("Called static method with x =", x)

my_object = MyClass(None)

# Call the static method using the class name
MyClass.my_function(10)

# Call the static method using an instance of the class
my_object.my_function(20)