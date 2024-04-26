
import resource

# Get the current memory usage in KB
current_usage = resource.usage()
print("Current memory usage:", current_usage[0])

# Allocate 10 MB of memory
resource.setrlimit(resource.RLIMIT_MEM, 10 * 1024)

# Get the memory usage again after allocation
current_usage_after_allocation = resource.usage()
print("Current memory usage after allocation:", current_usage_after_allocation[0])

# Release the allocated memory
resource.setrlimit(resource.RLIMIT_MEM, -1)

# Get the memory usage again after release
current_usage_after_release = resource.usage()
print("Current memory usage after release:", current_usage_after_release[0])
