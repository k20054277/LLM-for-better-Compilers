import threading

# Initialize a lock object
lock = threading.Lock()

def critical_section(x):
    # Acquire the lock
    lock.acquire()
    try:
        # Perform some critical section of code that must be executed atomically
        print("Critical section:", x)
    finally:
        # Release the lock
        lock.release()

# Create a thread to run the critical section function
t = threading.Thread(target=critical_section, args=(10,))

# Start the thread and wait for it to finish
t.start()
t.join()