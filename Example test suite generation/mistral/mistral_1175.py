
# Base classes
class BaseClass1:
    def __init__(self, value):
        self.value = value

    def base_method1(self):
        print("Base method 1 from BaseClass1")

class BaseClass2:
    def __init__(self, value):
        super().__init__(value)

    def base_method2(self):
        print("Base method 2 from BaseClass2")

# Inheriting classes using multiple inheritance
class DerivedClass(BaseClass1, BaseClass2):

    def derived_method(self):
        print("Derived method in DerivedClass")

# Instantiate the object and demonstrate usage of as keyword
if __name__ == "__main__":
    obj = DerivedClass(42)
    obj.derived_method()  # Output: Derived method in DerivedClass
    obj.base_method1()    # Output: Base method 1 from BaseClass1
    obj.base_method2()    # Output: Base method 2 from BaseClass2

    # Using as keyword to access base classes
    BaseClass1_obj = obj.__getattribute__("BaseClass1")
    BaseClass1_obj.base_method1()     # Output: Base method 1 from BaseClass1
    BaseClass2_obj = obj.__getattribute__("BaseClass2")
    BaseClass2_obj.base_method2()     # Output: Base method 2 from BaseClass2
