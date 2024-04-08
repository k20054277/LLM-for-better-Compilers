
import gc

def foo(x):
    assert x >= 0
    print(x)

# Create a large object
a = [1] * 100000

# The object is not collected
foo(a)

# Collect the garbage
gc.collect()

# The object is collected
assert a is None

print("The object is collected")
