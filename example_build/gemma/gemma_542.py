
import threading

# Define a function that will wait for a lock
def thread_wait(lock, name):
    with lock:
        print(name + " acquired the lock")
        # Wait for the lock to be released
        print(name + " is waiting...")

# Create a lock
lock = threading.Lock()

# Create two threads
thread1 = threading.Thread(target=thread_wait, args=(lock, "Thread 1"))
thread2 = threading.Thread(target=thread_wait, args=(lock, "Thread 2"))

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to complete
thread1.join()
thread2.join()

# Print the results
print("Both threads have completed")
