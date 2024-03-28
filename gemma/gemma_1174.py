
import time

start_time = time.time()

# Perform some action that takes a long time, such as looping through a large list
for i in range(100000):
    print(i)

end_time = time.time()

# Calculate the time taken for the action
time_taken = end_time - start_time

# Print the time taken
print("Time taken:", time_taken)
