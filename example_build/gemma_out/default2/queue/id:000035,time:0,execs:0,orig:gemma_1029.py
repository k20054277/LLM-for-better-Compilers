
import threading
import time

def thread_one(lock):
    for i in range(10):
        with lock:
            print("Thread one is running")
            time.sleep(1)

def thread_two(lock):
    for i in range(10):
        with lock:
            print("Thread two is running")
            time.sleep(1)

if __name__ == "__main__":
    lock = threading.Lock()
    thread_one(lock)
    thread_two(lock)

    print("Main program is completed")
