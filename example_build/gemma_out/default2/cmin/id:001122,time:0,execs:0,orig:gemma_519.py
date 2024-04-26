
import time

# Define a function with a None return value
def function_with_none(n):
    if n % 2 == 0:
        return None

    # Perform some time-consuming operation
    time.sleep(1)

    return n

# Time the function with None return value
start_time = time.time()
function_with_none(10)
end_time = time.time()

# Print the time taken
print("Time taken:", end_time - start_time)

# Compare the time taken with and without None return value
start_time = time.time()
function_without_none(10)
end_time = time.time()

print("Time taken without None return value:", end_time - start_time)

# Define a function without a None return value
def function_without_none(n):
    if n % 2 == 0:
        return

    # Perform some time-consuming operation
    time.sleep(1)

    return n

# Time the function without None return value
start_time = time.time()
function_without_none(10)
end_time = time.time()

# Print the time taken
print("Time taken:", end_time - start_time)
