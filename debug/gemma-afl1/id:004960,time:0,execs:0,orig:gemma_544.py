
import threading
import time

# Define a function that will be executed by the thread
def thread_function(lock, number):
    # Acquire the lock
    lock.acquire()

    # Print the number of the thread
    print("Thread:", number)

    # Hold the lock for 2 seconds
    time.sleep(2)

    # Release the lock
    lock.release()

# Create a lock object
lock = threading.Lock()

# Create a list of threads
threads = []

# Create and start each thread
for i in range(5):
    thread = threading.Thread(target=thread_function, args=(lock, i))
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Print the completion message
print("All threads completed")
