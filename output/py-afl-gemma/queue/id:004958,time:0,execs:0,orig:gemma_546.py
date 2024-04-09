
import semaphore
import threading

# Define a semaphore with a value of 5
semaphore = semaphore.Semaphore(5)

# Define a function that will wait for the semaphore
def worker(name):
    # Acquire the semaphore
    semaphore.acquire()

    # Simulate some work
    print(name + " is working...")

    # Release the semaphore
    semaphore.release()

# Create a list of threads
threads = []

# Start a number of threads
for i in range(10):
    thread = threading.Thread(target=worker, args=("Thread %s" % i))
    threads.append(thread)

# Start all the threads
for thread in threads:
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Print completion message
print("All threads completed")
