
import threading
import time

def thread_one(n):
    for i in range(n):
        print("Thread one: Hello, world!")
        time.sleep(1)

def thread_two(n):
    for i in range(n):
        print("Thread two: Greetings, friend!")
        time.sleep(1)

if __name__ == "__main__":
    n = 5
    thread_one(n)
    thread_two(n)

    print("Main: Completed")
    time.sleep(n)
