import threading

# Define a function that will be executed by multiple threads
def critical_section():
    print("Entering critical section")
    # Acquire the lock before entering the critical section
    with lock:
        # Do some work here
        print("Doing some work in the critical section")
    # Release the lock after exiting the critical section
    print("Exiting critical section")

# Create a lock object
lock = threading.Lock()

# Start multiple threads that will execute the function concurrently
threads = []
for i in range(5):
    t = threading.Thread(target=critical_section)
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()