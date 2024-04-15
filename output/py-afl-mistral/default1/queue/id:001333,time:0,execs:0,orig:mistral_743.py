
import threading
import time

def worker(name):
    """ A simple worker function to demonstrate multithreading """
    print(f"Thread {name} started")
    time.sleep(3)
    print(f"Thread {name} finished")

if __name__ == "__main__":
    thread1 = threading.Thread(target=worker, args=("Thread1",))
    thread2 = threading.Thread(target=worker, args=("Thread2",))

    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for both threads to finish their execution
    thread1.join()
    thread2.join()

    print("Main thread finished")
