
import semaphore

# Define a semaphore with a value of 5
sema = semaphore.Semaphore(5)

# Multiple threads will attempt to acquire the semaphore
# Each thread will block until the semaphore's value becomes available
for i in range(10):
    thread = threading.Thread(target=lambda: print("Thread %s acquired the semaphore" % i))
    thread.start()

    # The thread will acquire the semaphore, blocking until the value is available
    sema.acquire()

    # After acquiring the semaphore, the thread prints its number
    print("Thread %s released the semaphore" % i)

# The main thread will wait for all threads to complete
for thread in threads:
    thread.join()

# The semaphore's value is now available for other threads to acquire
print("All threads have completed")
