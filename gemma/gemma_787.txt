
import sys
import gc

# Define a class that uses a lot of memory
class BigMemoryUser:
    def __init__(self, size):
        self.data = [x for x in range(size)]

    def __del__(self):
        print("Goodbye, big memory user!")

# Create a big memory user
big_user = BigMemoryUser(100000)

# Do something with the big memory user
big_user.data[0] = 10

# Check the memory usage
print(sys.getsizeof(big_user))

# Delete the big memory user
del big_user

# Run the garbage collector
gc.collect()

# Check if the memory has been freed
print(sys.getsizeof(big_user))

# Output:
# Goodbye, big memory user!
# 4000
# 0
