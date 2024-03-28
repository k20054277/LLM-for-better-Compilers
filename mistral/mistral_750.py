
import threading
import time

def worker(semaphore, condition):
    semaphore.acquire()

    print("Thread {} started".format(threading.current_thread().name))

    # Simulating some work by sleeping for a random period of time
    time.sleep(1 + 2 * (threading.randint(0, 1) % 2))

    condition.set()  # Signal that the thread has finished its job
    semaphore.release()

    print("Thread {} finished".format(threading.current_thread().name))
