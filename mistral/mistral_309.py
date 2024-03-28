
class MyClass:
    def __init__(self, attribute1=None, attribute2=None):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def my_method(self):
        if self.attribute1 is not None:
            print("Attribute 1 has a value:", self.attribute1)
        else:
            print("Attribute 1 has no value.")
        
if __name__ == "__main__":
    instance = MyClass()
    print("Instance of MyClass created without initializing any attributes.")
    instance.my_method()

    another_instance = MyClass(attribute1="Value1")
    print("Instance of MyClass initialized with Attribute 1.")
    another_instance.my_method()

    del another_instance.attribute1
    print("Instance of MyClass with Attribute 1 deleted.")
    another_instance.my_method()

    uninitialized_instance = MyClass(attribute2="Value2")
    print("Instance of MyClass initialized with Attribute 2.")
    getattr(uninitialized_instance, 'my_method')() # Using getattr to call my_method without dot notation
