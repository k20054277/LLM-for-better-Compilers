class MyClass:
    def __init__(self, x):
        self.x = x
    
    def __eq__(self, other):
        return self.x == other.x
    
    def __hash__(self):
        return hash(self.x)

my_list = [MyClass(1), MyClass(2), MyClass(3)]
print(id(my_list[0])) # 456789
print(as_list[1]) # MyClass object at 0x10c9da