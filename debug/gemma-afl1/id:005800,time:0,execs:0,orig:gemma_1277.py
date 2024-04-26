
import semaphore

# Create a semaphore with a value of 5
sema = semaphore.Semaphore(5)

# Multiple threads trying to acquire the semaphore
for i in range(10):
    thread = threading.Thread(target=lambda:
        print("Thread %s is waiting..." % i)
        sema.acquire()
        print("Thread %s is executing..." % i)
        time.sleep(1)
        print("Thread %s is released..." % i)
        sema.release()
    )
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All threads have completed")
