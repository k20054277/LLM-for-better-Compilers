
# Defining some base classes
class BaseClass1:
    def __init__(self, value):
        self.value = value

class BaseClass2:
    pass

class DerivedClass(BaseClass1, BaseClass2):
    pass

# Function demonstrating the usage of and and issubclass
def check_inheritance(base1, base2, derived):
 if (isinstance(derived, base1) and issubclass(derived, base2)):
 print(f"Derived class '{derived.__name__}' is both an instance of {base1.__name__} and a subclass of {base2.__name__}")
 else:
 print(f"Derived class '{derived.__name__}' is not an instance of {base1.__name__} or a subclass of {base2.__name__}")

# Instantiating base classes and derived class
base1_instance = BaseClass1("Base1 value")
base2_instance = BaseClass2()
derived_instance = DerivedClass("Derived value")

# Calling check_inheritance function
check_inheritance(BaseClass1, BaseClass2, BaseClass1) # This should print: BaseClass1 is both an instance of BaseClass1 and a subclass of BaseClass2 (False due to type mismatch)
check_inheritance(BaseClass1, BaseClass2, DerivedClass) # This should print: Derived class 'DerivedClass' is both an instance of BaseClass1 and a subclass of BaseClass2
check_inheritance(BaseClass1, BaseClass2, BaseClass1) # This should print: BaseClass1 is both an instance of BaseClass1 and a subclass of BaseClass2 (False due to type mismatch)
