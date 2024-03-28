
import threading
import time

def thread_one(n):
    for i in range(n):
        print("Thread One: Iteration", i)
        time.sleep(0.5)

def thread_two(n):
    for i in range(n):
        print("Thread Two: Iteration", i)
        time.sleep(0.5)

if __name__ == "__main__":
    n = 10
    thread_one(n)
    thread_two(n)

    print("Main Thread: Completed")
