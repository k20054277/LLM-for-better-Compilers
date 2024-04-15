
# Define some base classes
class BaseClass1:
    pass

class BaseClass2:
    pass

# Define a derived class
class DerivedClass(BaseClass1, BaseClass2):
    pass

# Function demonstrating the usage of None
def print_type(my_var):
    if my_var is not None:
        print("Variable type:", type(my_var))
    else:
        print("Variable is None")

# Demonstrating issubclass() function
print("Is BaseClass1 a base class of DerivedClass?:", issubclass(DerivedClass, BaseClass1))
print("Is BaseClass2 a base class of DerivedClass?:", issubclass(DerivedClass, BaseClass2))

# Using None in the program
my_var = 42
print_type(my_var)
my_var = None
print_type(my_var)
