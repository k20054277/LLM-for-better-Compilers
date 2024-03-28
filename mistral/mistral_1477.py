
import threading
import time

# Counter class with lock for thread-safe access
class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

# Function to be executed in separate threads
def increment_counter(counter):
    for i in range(1000):
        with counter.lock:
            assert counter.value == i, f"Counter value incorrect: {counter.value} != {i}"
            counter.value += 1

# Create and start threads
counter = Counter()
threads = []
for _ in range(5):
    t = threading.Thread(target=increment_counter, args=(counter,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("Final counter value:", counter.value)
