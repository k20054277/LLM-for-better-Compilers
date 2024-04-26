
import sys
import gc
import time

# Function to get current memory usage
def get_memory_usage():
    process = sys.argv[-1]
    py_stats = gc.get_stats()
    rss = sum(stat['heap_used_in_bytes'] for stat in py_stats if 'heap' in stat)
    return rss, process

# Create a large list of True values
def create_large_list():
    return [True] * 1000000

if __name__ == "__main__":
    # Initialize the large list
    large_list = create_large_list()
    
    print("List created. Current memory usage:")
    current_memory, current_process = get_memory_usage()
    print(f"Process '{current_process}': {current_memory/1024/1024} MB")

    # Let the garbage collector run
    gc.collect()

    print("\nGarbage collection finished. Current memory usage:")
    after_memory, _ = get_memory_usage()
    print(f"Process '{current_process}': {after_memory/1024/1024} MB")
