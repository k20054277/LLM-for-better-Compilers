import threading
import time

def task1():
    # Acquire the lock
    global_lock.acquire()
    
    print("Task 1 is running")
    
    # Release the lock
    global_lock.release()

def task2():
    # Acquire the lock
    global_lock.acquire()
    
    print("Task 2 is running")
    
    # Release the lock
    global_lock.release()

# Create a mutex object
global_lock = threading.Lock()

# Create two threads that will run concurrently
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

# Start the threads
t1.start()
t2.start()

# Wait for the threads to finish
t1.join()
t2.join()