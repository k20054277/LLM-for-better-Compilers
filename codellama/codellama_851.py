class MyClass:
    def __init__(self, x):
        self.x = x
    
    @classmethod
    def combine(cls, a, b):
        return cls(a.x + b.x)
    
    @classmethod
    def add_one(cls, a):
        return cls(a.x + 1)