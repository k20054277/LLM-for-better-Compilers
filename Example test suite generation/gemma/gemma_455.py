
import time

# Define a function to measure time taken by False comparisons
def time_false_comparison(n):
    start_time = time.time()
    for _ in range(n):
        if False:
            pass
    end_time = time.time()
    return end_time - start_time

# Measure time taken by False comparisons for different number of iterations
times = []
for i in range(1000, 10001, 1000):
    time_taken = time_false_comparison(i)
    times.append(time_taken)

# Plot the time taken
import matplotlib.pyplot as plt
plt.plot(times)
plt.xlabel("Number of iterations")
plt.ylabel("Time taken (seconds)")
plt.title("Time taken by False comparisons")
plt.show()
