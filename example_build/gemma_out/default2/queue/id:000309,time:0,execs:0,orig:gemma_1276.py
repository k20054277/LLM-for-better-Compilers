
import threading
import time

# Define a shared resource
shared_resource = 0

# Define a mutex to synchronize access to the shared resource
mutex = threading.Lock()

# Define a thread function
def thread_function(name):
    for _ in range(10):
        # Acquire the mutex
        with mutex:
            # Increment the shared resource
            shared_resource += 1

# Create two threads
thread_1 = threading.Thread(target=thread_function, name="Thread 1")
thread_2 = threading.Thread(target=thread_function, name="Thread 2")

# Start the threads
thread_1.start()
thread_2.start()

# Wait for the threads to complete
thread_1.join()
thread_2.join()

# Print the shared resource
print("Shared resource:", shared_resource)
