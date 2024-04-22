
import threading
import time

# Define a mutex
mutex = threading.Mutex()

# Define a function that will be executed by multiple threads
def thread(n):
    # Acquire the mutex
    mutex.acquire()

    # Simulate some work
    time.sleep(n)

    # Release the mutex
    mutex.release()

# Create a list of threads
threads = []

# Start multiple threads
for i in range(10):
    thread = threading.Thread(target=thread, args=(i,))
    threads.append(thread)

# Start all threads
for thread in threads:
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Print the results
print("All threads completed!")
