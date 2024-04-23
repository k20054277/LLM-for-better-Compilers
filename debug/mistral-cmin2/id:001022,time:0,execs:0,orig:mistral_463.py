
class MyClass:
    def __init__(self, data=None):
        self.data = data
        
# Function to allocate large list
def create_large_list(size):
    return [i for i in range(size)]

# Function to measure memory usage with sys.getsizeof()
import sys

def measure_memory(obj):
    return sys.getsizeof(obj)

# Program entry point
if __name__ == "__main__":
    instance = MyClass()  # Creating an instance of MyClass with default value None

    print("Memory usage of None: ", measure_memory(None))
    print("Memory usage of empty class instance: ", measure_memory(instance))

    large_list = create_large_list(10000)  # Allocating a large list

    print("Memory usage of large list: ", measure_memory(large_list))

    del large_list  # Deallocating the large list

    print("Memory usage of empty class instance after Garbage Collection: ", measure_memory(instance))
