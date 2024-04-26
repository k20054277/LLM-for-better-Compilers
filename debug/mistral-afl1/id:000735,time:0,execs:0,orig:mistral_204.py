
import threading
import time

# Shared variable
counter = 0

def increment_counter():
    """Thread function to increment the counter"""
    global counter

    for _ in range(1000):
        counter += 1

# Create two threads
thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=increment_counter)

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Counter value:", counter)
