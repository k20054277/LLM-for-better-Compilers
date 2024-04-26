
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = 0

    def enable_c(self):
        self.c = 1

    def disable_c(self):
        delattr(self, 'c')

if __name__ == "__main__":
    obj = MyClass(1, 2)
    print("Initial state: a={}, b={}, c={}".format(obj.a, obj.b, hasattr(obj, 'c')))

    obj.enable_c()
    print("After enabling c: a={}, b={}, c={}".format(obj.a, obj.b, hasattr(obj, 'c')))

    obj.disable_c()
    print("After disabling c: a={}, b={}, c={}".format(obj.a, obj.b, hasattr(obj, 'c')))

# Output:
# Initial state: a=1, b=2, c=False
# After enabling c: a=1, b=2, c=True
# After disabling c: a=1, b=2, c=False
