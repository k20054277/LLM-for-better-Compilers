
import threading
import time

# Define two resources with their respective locks
resource1_lock = threading.Lock()
resource2_lock = threading.Lock()

def function1():
    """Function 1 acquires resource 1, then attempts to acquire resource 2."""
    print("Function 1: Acquiring resource 1...")
    resource1_lock.acquire()
    time.sleep(0.5)
    print("Function 1: Trying to acquire resource 2...")
    resource2_lock.acquire()
    print("Function 1: Both resources acquired!")

def function2():
    """Function 2 acquires resource 2, then attempts to acquire resource 1."""
    print("Function 2: Acquiring resource 2...")
    resource2_lock.acquire()
    time.sleep(0.5)
    print("Function 2: Trying to acquire resource 1...")
    resource1_lock.acquire()
    print("Function 2: Both resources acquired!")

# Create and start threads
thread1 = threading.Thread(target=function1)
thread2 = threading.Thread(target=function2)

thread1.start()
thread2.start()

# Wait for threads to finish
thread1.join()
thread2.join()

print("All threads completed.")
