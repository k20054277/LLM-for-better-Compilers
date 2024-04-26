
import threading
import time

# Define a function to be threaded
def thread(num):
    for i in range(num):
        print("Thread:", num, "is running")
        time.sleep(1)

# Create a list of threads
threads = []

# Start multiple threads
for i in range(5):
    thread_num = i + 1
    thread(thread_num)
    threads.append(thread_num)

# Wait for all threads to complete
for thread_num in threads:
    print("Thread", thread_num, "has completed")

print("All threads have completed")
