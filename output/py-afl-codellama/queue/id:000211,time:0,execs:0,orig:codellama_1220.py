import threading
import time

# define a function to be executed by threads
def worker():
    print("Worker running")
    # acquire the semaphore
    with threading.Semaphore(value=1):
        print("Acquired semaphore, doing some work...")
        time.sleep(2)
        print("Released semaphore")

# create a list of threads
threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

# wait for all threads to finish
for t in threads:
    t.join()