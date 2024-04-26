
import threading
import time

# Define a shared counter that will be accessed by multiple threads
counter = 0

# Create a lock for synchronization
lock = threading.Lock()

def increment_counter(name):
    """Increments the counter."""
    
    # Loop for 100 times to simulate some work being done
    for _ in range(100):
        pass

    # Acquire the lock before accessing the shared counter
    with lock:
        global counter
        counter += 1
        print(f"{name} incremented the counter to {counter}")

# Create two threads and start them
thread_a = threading.Thread(target=increment_counter, args=("Thread A",))
thread_b = threading.Thread(target=increment_counter, args=("Thread B",))

# Start both threads
thread_a.start()
thread_b.start()

# Wait for both threads to finish their work
thread_a.join()
thread_b.join()
