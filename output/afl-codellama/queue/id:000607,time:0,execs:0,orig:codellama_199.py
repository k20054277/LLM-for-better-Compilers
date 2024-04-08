class MyObject:
    def __init__(self, value):
        self.value = value
    
    @classmethod
    def from_value(cls, value):
        return cls(value)
    
    def print_value(self):
        print(self.value)