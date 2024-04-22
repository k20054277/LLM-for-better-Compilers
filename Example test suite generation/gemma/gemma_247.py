
import datetime

# Define the start time
start_time = datetime.datetime.now()

# Perform some task that takes time, for example, looping through a large list
for i in range(100000):
    print(i)

# Define the end time
end_time = datetime.datetime.now()

# Calculate the time taken
time_taken = end_time - start_time

# Print the time taken
print("Time taken:", time_taken)
