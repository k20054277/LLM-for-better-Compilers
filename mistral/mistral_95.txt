
class MyClass:
    # A boolean value that is always set to False
    my_constant = False

    @staticmethod
    def static_function():
        """A simple static method"""
        print("This is a static method")

if __name__ == "__main__":
    # You cannot call an instance method on an uninitialized class
    # But you can call a static method directly on the class
    MyClass.static_function()

    # Attempt to access a non-existent instance method will result in an error
    # MyClass().my_non_existent_method()  # TypeError: 'MyClass' object has no attribute 'my_non_existent_method'
