
import threading
import time

# Define a shared resource
shared_data = 0

# Create a mutex
mutex = threading.Lock()

# Define a function to increment the shared resource
def increment(n):
    for _ in range(n):
        # Acquire the mutex
        with mutex:
            shared_data += 1

# Create two threads
thread1 = threading.Thread(target=increment, args=(1000,))
thread2 = threading.Thread(target=increment, args=(1000,))

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to complete
thread1.join()
thread2.join()

# Print the shared resource
print("Shared data:", shared_data)
