
import threading
import time

def thread1(n):
    for i in range(n):
        print("Thread 1:", i)
        time.sleep(0.5)

def thread2(n):
    for i in range(n):
        print("Thread 2:", i)
        time.sleep(0.5)

if __name__ == "__main__":
    n = 10
    thread1(n)
    thread2(n)

    # This line may not execute properly due to the race condition
    print("Main:", n)

    time.sleep(2)
