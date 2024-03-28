
import threading
import time

# Define a semaphore with a limit of 1
semaphore = threading.Semaphore(1)

def worker_function(thread_name):
    """Function for each worker thread."""

    print(f"Thread {thread_name} started.")

    # Wait to acquire the semaphore before accessing the shared resource
    semaphore.acquire()

    # Perform some work on the shared resource here (not shown)
    time.sleep(1)

    print(f"Thread {thread_name} releasing semaphore and finished.")

    semaphore.release()

# Create 5 worker threads
for i in range(5):
    thread = threading.Thread(target=worker_function, args=(i,))
    thread.start()
