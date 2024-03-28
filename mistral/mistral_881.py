
class MyClass:
    @staticmethod
    def static_method(a, b):
        """This method demonstrates the usage of @staticmethod"""
        return a > b and a > 0 and b > 0

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

if __name__ == "__main__":
    # Calling static method on the class using class name
    print(MyClass.static_method(3, 5))

    # Creating an instance of MyClass and calling the same method on it
    my_instance = MyClass(10, -2)
    print(my_instance.static_method(10, -2))
    print(my_instance.static_method(10, 5))
    print(my_instance.static_method(5, 10))
