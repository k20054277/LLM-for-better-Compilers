class MyClass:
    def __init__(self):
        self.__my_private_variable = 0

    def get_my_private_variable(self):
        return self.__my_private_variable

    def set_my_private_variable(self, value):
        self.__my_private_variable = value

if __name__ == "__main__":
    obj = MyClass()
    print(obj.get_my_private_variable())  # Output: 0
    obj.set_my_private_variable(5)
    print(obj.get_my_private_variable())  # Output: