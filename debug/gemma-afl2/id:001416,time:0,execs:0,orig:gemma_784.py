
import threading
import semaphore

# Define a semaphore with a value of 5
sema = semaphore.Semaphore(5)

# Define a function that will acquire and release the semaphore
def worker(name):
    print(name + " is waiting...")
    sema.acquire()
    print(name + " is working...")
    sema.release()
    print(name + " has finished")

# Create a list of threads
threads = []

# Start 10 threads
for i in range(10):
    thread = threading.Thread(target=worker, args=("Thread %d" % i))
    threads.append(thread)

# Start all threads
for thread in threads:
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All threads have completed")
