class MyClass:
    def __init__(self, x):
        self.x = x
    
    @staticmethod
    def double(x):
        return 2 * x
    
    @staticmethod
    def triple(x):
        return 3 * x
    
    def print_double(self):
        print(MyClass.double(self.x))
    
    def print_triple(self):
        print(MyClass.triple(self.x))

my_obj = MyClass(5)
my_obj.print_double()   # Output: 10
my_obj.print_triple()   # Output: