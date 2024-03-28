
class MyClass:
    @staticmethod
    def my_static_method():
        print("Static method called")

    def my_method(self):
        print("Instance method called")

    def __init__(self):
        print("Constructor called")

# Create an instance of MyClass
my_instance = MyClass()

# Call static method
MyClass.my_static_method()

# Call instance method
my_instance.my_method()

# Output:
# Constructor called
# Static method called
# Instance method called
