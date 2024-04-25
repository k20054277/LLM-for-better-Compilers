
import threading
import time

# Define a function to demonstrate True and lock
def thread_function(lock, shared_variable):
    for i in range(10):
        # Acquire the lock
        lock.acquire()
        # Update the shared variable
        shared_variable.value += 1
        # Release the lock
        lock.release()
        time.sleep(0.5)

# Create a shared variable
shared_variable = threading.shared_variable(0)

# Create a lock
lock = threading.Lock()

# Create and start threads
threads = []
for i in range(5):
    thread = threading.Thread(target=thread_function, args=(lock, shared_variable))
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Print the final value of the shared variable
print("Final value of shared variable:", shared_variable.value)
