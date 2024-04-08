def assert_staticmethod():
    assert False, "This is an assertion"
    
@staticmethod
def static_function(x):
    return x**2

assert_staticmethod()
static_function(5)