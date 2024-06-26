
import gc

def create_large_object(size=10000):
    """Create a large list for demonstration purposes."""
    large_list = [i for i in range(size)]
    return large_list

# Create a large object
large_object = create_large_object()

# Use the 'and' operator in a conditional statement
if condition():
    # Some code here
    pass
else:
    print("Else block executed")
    
# Manually invoke garbage collection to ensure that our large object is collected.
gc.collect()
