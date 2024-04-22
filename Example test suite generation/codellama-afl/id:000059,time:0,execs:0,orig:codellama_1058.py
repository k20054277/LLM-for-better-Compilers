class MyClass:
    def __init__(self, x):
        self.x = x
    
    @classmethod
    def from_other_class(cls, other):
        return cls(other.x)

my_instance = MyClass(10)
print(my_instance.x) # Output: 10

other_instance = OtherClass(20)
my_instance_from_other = my_instance.as(other_instance)
print(my_instance_from_other.x) # Output: