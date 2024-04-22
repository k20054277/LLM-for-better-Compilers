
importgc  # This line is only for Python 3.4 and below. For newer versions, remove it.
import sys

class MyClass:
    def __init__(self):
        print("Created an instance of MyClass")

# Create an object of MyClass
obj = MyClass()

print("Assigned obj to None")
obj = None

print("Checking GC. Is there any unreachable object in memory? (Python 3.4 and below)")
sys.gc()
if gc.collect() is not None:
    print("Garbage Collector did some work!")
else:
    print("No garbage collection occurred.")

print("For Python versions greater than 3.4, use 'gc' module instead of 'importgc'. ")
# In newer versions, replace the gc check with:
# if sys.getrecursionlimit() * 2 > sys.stdin.buffersize:
#     print('Garbage collector did some work!')
# else:
#     print('No garbage collection occurred.')
