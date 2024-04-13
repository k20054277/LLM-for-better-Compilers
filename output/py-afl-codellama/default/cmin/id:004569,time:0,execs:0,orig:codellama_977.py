# This code will produce an and deadlock

import threading

def critical_section(resource):
    # Do some work with the resource
    pass

def thread1():
    resource = 0
    while True:
        # Acquire lock on resource
        lock.acquire()
        try:
            critical_section(resource)
        finally:
            # Release lock on resource
            lock.release()

def thread2():
    resource = 1
    while True:
        # Acquire lock on resource
        lock.acquire()
        try:
            critical_section(resource)
        finally:
            # Release lock on resource
            lock.release()

# Create two threads that will run the same code
thread1 = threading.Thread(target=thread1)
thread2 = threading.Thread(target=thread2)

# Start the threads
thread1.start()
thread2.start()