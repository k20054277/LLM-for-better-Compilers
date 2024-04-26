
import threading
import semaphore

# Create a semaphore with a value of 5
sema = semaphore.Semaphore(5)

# Define a function that will acquire and release the semaphore
def worker(i):
    for _ in range(10):
        print("Thread %s is waiting..." % i)
        sema.acquire()
        print("Thread %s is working..." % i)
        sema.release()

# Create and start 10 threads
threads = []
for i in range(10):
    thread = threading.Thread(target=worker, args=(i,))
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All threads completed!")
