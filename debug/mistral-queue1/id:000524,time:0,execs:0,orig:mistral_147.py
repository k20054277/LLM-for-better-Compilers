
class Base:
    def __bool__(self):
        return False

    def operation(self):
        print("Base class operation called")

class Derived1(Base):
    def __bool__(self):
        return True

class Derived2(Base):
    pass

# Polymorphic function that takes a Base instance and tries to call the 'operation' method
def polymorphic_function(instance):
    if instance:
        instance.operation()

if __name__ == "__main__":
    # Creating instances of derived classes
    derived1 = Derived1()
    derived2 = Derived2()

    # Demonstrating False and polymorphism
    print("Calling function with Derived1 instance:")
    polymorphic_function(derived1) # Will call the 'operation' method of Derived1 because it is truthy (bool returns True)

    print("Calling function with Derived2 instance:")
    polymorphic_function(derived2) # Since Derived2 instance is falsy (bool returns False), the 'if statement' condition fails and no operation will be called.
