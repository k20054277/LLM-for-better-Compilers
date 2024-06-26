# This program demonstrates the use of True and Lock in Python
import threading

# Define a function to be executed by the threads
def print_message(lock):
    # Acquire the lock
    with lock:
        print("Hello, World!")

# Create two threads
thread1 = threading.Thread(target=print_message, args=(True,))
thread2 = threading.Thread(target=print_message, args=(True,))

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()