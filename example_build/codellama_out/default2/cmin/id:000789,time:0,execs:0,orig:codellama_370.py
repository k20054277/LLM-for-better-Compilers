import threading

# Create a semaphore with initial value 1
sem = threading.Semaphore(value=1)

# Define a function that will acquire the semaphore and then release it after running
def my_function():
    # Acquire the semaphore
    sem.acquire()
    try:
        # Do some work here that needs to be protected by the semaphore
        print("Working...")
        # Release the semaphore
        sem.release()
    except Exception as e:
        # If there is an exception, release the semaphore anyway
        sem.release()
        raise e

# Create a thread that will run the function and then exit
thread = threading.Thread(target=my_function)
thread.start()

# Create another thread that will also run the function and then exit
thread2 = threading.Thread(target=my_function)
thread2.start()

# Wait for both threads to finish
thread.join()
thread2.join()