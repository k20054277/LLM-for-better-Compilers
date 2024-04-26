
# Defining base class
class Base:
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print("Value in Base is:", self.value)

# Defining derived class
class Derived(Base):
    def __init__(self, name, value):
        super().__init__(value)
        self.name = name

    def print_name(self):
        print("Name in Derived is:", self.name)

# Creating an instance of derived class
derived_instance = Derived("DerivedClass", 10)

# Using as keyword for inheritance
base_derived = Derived as Base  # This creates an alias 'base_derived' for the Derived class with Base as its base.
derived_instance_as_base = derived_instance as Base  # Creating an alias for derived_instance of Base class.

# Printing values using aliases
base_derived.print_value()
derived_instance_as_base.print_value()

# Check if Derived is a subclass of Base using issubclass()
print("Is Derived a subclass of Base?", issubclass(Derived, Base))
