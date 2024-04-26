
import threading
import time

def thread_one(n):
    for i in range(n):
        print("Thread one:", i)
        time.sleep(1)

def thread_two(n):
    for i in range(n):
        print("Thread two:", i)
        time.sleep(1)

if __name__ == "__main__":
    n = 10
    thread_one(n)
    thread_two(n)

    print("Main thread finished")
