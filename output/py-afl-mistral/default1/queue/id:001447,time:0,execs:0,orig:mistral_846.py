
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = None

    def method_1(self):
        return self.a + self.b

    def method_2(self):
        self.c = 42

def main():
    obj = MyClass(3, 5)
    
    # Check if 'obj' has both 'method_1' and 'method_2' attributes using getattr()
    if not (hasattr(obj, 'method_1') and hasattr(obj, 'method_2')):
        print("Error: Object does not have method_1 and method_2.")
        return
    
    # Call methods using getattr()
    print("Result of method_1():", getattr(obj, 'method_1')())
    getattr(obj, 'method_2')()
    print("Value of c after method_2() call:", obj.c)

if __name__ == "__main__":
    main()
