def demonstrate_assert_hasattr():
    # Define a class with an attribute 'x'
    class MyClass:
        def __init__(self):
            self.x = 5
    
    # Create an instance of the class
    my_instance = MyClass()
    
    # Use assert to check if the attribute 'y' exists on the object
    assert not hasattr(my_instance, 'y')
    
    # Use assert to check if the attribute 'x' exists and its value is 5
    assert hasattr(my_instance, 'x') and my_instance.x ==