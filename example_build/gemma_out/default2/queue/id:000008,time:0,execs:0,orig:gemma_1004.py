
import sys
import time

# Define a function to measure the time taken by the and operator
def measure_and(n):
    start_time = time.time()
    for _ in range(n):
        a = 5 and 10
    end_time = time.time()
    return end_time - start_time

# Measure the time taken by the and operator for different values of n
times = []
for i in range(1000, 10001, 1000):
    times.append(measure_and(i))

# Plot the time taken by the and operator against the number of iterations
import matplotlib.pyplot as plt
plt.scatter(times, range(1000, 10001, 1000))
plt.xlabel("Number of iterations")
plt.ylabel("Time taken (seconds)")
plt.title("Time taken by the and operator")
plt.show()

# Print the average time taken by the and operator
avg_time = sum(times) / len(times)
print("Average time taken by the and operator:", avg_time)
