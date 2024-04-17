
import threading
import time

# Define a shared resource with two operations: increment and print
class SharedResource:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.value += 1
            print(f"Thread: {threading.current_thread().name}, Value: {self.value}")

    def print_value(self):
        with self.lock:
            print(f"Thread: {threading.current_thread().name}, Value: {self.value}")

# Create an instance of the SharedResource class
resource = SharedResource()

def thread_func(resource):
    for i in range(5):
        resource.increment()

# Create two threads and start them
threads = [threading.Thread(target=thread_func, args=(resource,)) for _ in range(2)]
for t in threads:
    t.start()

# Wait for all threads to finish before exiting the main thread
for t in threads:
    t.join()
