class MyObject:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def get_value(self):
        return self.value

my_object = MyObject()
print(my_object.get_value()) # Output: 0
my_object.increment()
print(my_object.get_value()) # Output: 1
my_object.decrement()
print(my_object.get_value()) # Output: