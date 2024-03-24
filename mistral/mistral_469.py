
class MyClass:
    def my_method(self):
        """
        This method returns None by default.
        """
        return None

def main():
    # Create an instance of MyClass
    obj = MyClass()

    # Call the my_method() and assign the result to a variable 'result'
    result = obj.my_method()

    # Print out the type of 'result'
    print(type(result))

if __name__ == "__main__":
    main()
