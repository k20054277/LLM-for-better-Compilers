
import threading
import time

def task(name):
    print(f"{name} task started")
    time.sleep(3)
    print(f"{name} task completed")

if __name__ == "__main__":
    # Create two threads for two tasks
    thread1 = threading.Thread(target=task, args=("Task 1",))
    thread2 = threading.Thread(target=task, args=("Task 2",))

    # Start both threads
    thread1.start()
    thread2.start()

    # Wait for both threads to complete before exiting the program
    thread1.join()
    thread2.join()

    print("All tasks completed")
