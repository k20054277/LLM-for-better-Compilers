
# Define base class
class BaseClass:
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print("Base Class Value:", self.value)

# Define derived classes
class DerivedClass1(BaseClass):
    pass

class DerivedClass2(BaseClass):
    pass

# Instantiate objects
obj_base = BaseClass(10)
obj_derived1 = DerivedClass1(5)
obj_derived2 = DerivedClass2(7)

# Check isinstance()
print("Is obj_derived1 an instance of BaseClass?", isinstance(obj_derived1, BaseClass))  # True
print("Is obj_base an instance of DerivedClass1?", isinstance(obj_base, DerivedClass1))  # False

# Check issubclass()
print("Is DerivedClass1 a subclass of BaseClass?", issubclass(DerivedClass1, BaseClass))  # True
print("Is DerivedClass2 a subclass of BaseClass?", issubclass(DerivedClass2, BaseClass))  # True
