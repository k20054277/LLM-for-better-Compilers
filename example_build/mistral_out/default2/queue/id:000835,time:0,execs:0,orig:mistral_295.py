
class MyClass:
    # Define a class variable with an initial value of None
    _instance = None

    @classmethod
    def from_string(cls, string_representation):
        """Create and return a new instance of this class given a string representation."""
        if cls._instance is None:
            cls._instance = MyClass()
        return cls._instance

    def __init__(self):
        self.data = []

    @classmethod
    def class_method(cls, argument):
        """A simple class method that takes an argument and prints it."""
        print(f"You called the class method with argument: {argument}")

if __name__ == "__main__":
    # Call the class method directly
    MyClass.class_method("directly")

    # Create two instances using the string representation
    inst1 = MyClass.from_string('instance1')
    inst2 = MyClass.from_string('instance2')

    # Check that only one instance was created
    assert inst1 is inst2
