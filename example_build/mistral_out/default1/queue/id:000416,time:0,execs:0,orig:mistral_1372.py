
# Base class with __init__ method
class BaseClass:
    def __init__(self, value):
        self.value = value

    # Method that should be implemented by the subclass
    def operation(self):
        raise NotImplementedError("Subclass must implement operation()")

# Derived class implementing base class and overriding operation method
class DerivedClass(BaseClass):
    def __init__(self, value, another_value):
        super().__init__(value)
        self.another_value = another_value

    def operation(self):
        assert self.value > 0, "Value in base class constructor should be positive"
        result = self.value * self.another_value
        print("Result of operation:", result)
        return result

if __name__ == "__main__":
    derived_obj = DerivedClass(3, 2)
    derived_obj.operation()
