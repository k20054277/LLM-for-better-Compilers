import threading

# Create a semaphore with an initial value of 0
sem = threading.Semaphore(0)

def worker():
    # Acquire the semaphore
    sem.acquire()
    print("Worker started")
    # Do some work
    time.sleep(2)
    print("Worker finished")
    # Release the semaphore
    sem.release()

# Create a thread that will execute the worker function
t = threading.Thread(target=worker)
t.start()

# Wait for the semaphore to be released by the worker thread
sem.acquire()

print("Main thread finished")