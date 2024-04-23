
# Define Base Class
class Base:
    def __init__(self):
        self.base_attribute = "Base attribute"

# Define Derived Classes
class Derived1(Base):
    def __init__(self):
        super().__init__()
        self.derived1_attribute = "Derived1 attribute"

class Derived2:
    def __init__(self):
        self.derived2_attribute = "Derived2 attribute"

# Test the relationships using assert and issubclass
def test_relationships():
    base_instance = Base()
    derived1_instance = Derived1()
    derived2_instance = Derived2()

    # Using assert to check if instances of Derived classes are also instances of Base
    assert isinstance(derived1_instance, Base)
    assert isinstance(derived2_instance, Base)

    # Using issubclass to check the class relationships
    assert issubclass(Derived1, Base)
    assert issubclass(Derived1, Base)
    assert not issubclass(Derived2, Base)

# Run the tests
test_relationships()
