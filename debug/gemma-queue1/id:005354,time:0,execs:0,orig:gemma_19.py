
import threading

def thread1(lock):
    lock.acquire()
    print("Thread 1 acquired the lock")
    time.sleep(2)
    lock.release()
    print("Thread 1 released the lock")

def thread2(lock):
    lock.acquire()
    print("Thread 2 acquired the lock")
    time.sleep(2)
    lock.release()
    print("Thread 2 released the lock")

if __name__ == "__main__":
    lock = threading.Lock()
    thread1(lock)
    thread2(lock)

    print("Main program completed")
