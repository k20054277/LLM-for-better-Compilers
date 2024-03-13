
import threading
import semaphore

# Define a semaphore with a value of 5
sema = semaphore.Semaphore(5)

# Define a function that will wait for the semaphore
def worker(name):
    # Acquire the semaphore
    sema.acquire()

    # Simulate some work
    print(name + " is working")

    # Release the semaphore
    sema.release()

# Create a list of threads
threads = []

# Create and start each thread
for i in range(10):
    thread = threading.Thread(target=worker, args=("Thread %d" % i))
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Print completion message
print("All threads completed")
