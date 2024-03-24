#!/usr/bin/env python

class MyClass:
    def __init__(self):
        self.x = 5
        self.y = False

    def my_method(self, arg1, arg2):
        if getattr(self, arg1) == True and getattr(self, arg2) == True:
            return "Hello"
        else:
            return "Goodbye"

my_object = MyClass()
print(my_object.my_method("x", "y")) # should print "Hello"
print(my_object.my_method("x", False)) # should print "Goodbye"