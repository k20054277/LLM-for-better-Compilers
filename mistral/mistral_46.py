
class MyClass:
    # Define a class variable
    my_variable = 0

    @classmethod
    def set_my_variable(cls, value):
        """
        Set the class variable 'my_variable'
        :param value: The new value for 'my_variable'
        """
        if value < 0:
            print("Error: Value must be non-negative")
            return False
        cls.my_variable = value

    @classmethod
    def get_my_variable(cls):
        """
        Get the current value of 'my_variable'
        :return: The current value of 'my_variable'
        """
        return cls.my_variable
