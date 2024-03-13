import threading

# create a semaphore with initial value of 1
s = threading.Semaphore(1)

def critical_section():
    # acquire the semaphore
    s.acquire()
    try:
        # do some work in the critical section
        print("Critical Section")
    finally:
        # release the semaphore
        s.release()

# create a thread that will execute the critical_section function
thread = threading.Thread(target=critical_section)

# start the thread
thread.start()

# wait for the thread to finish
thread.join()