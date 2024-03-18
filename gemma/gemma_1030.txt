
import threading
import Queue

# Define a shared resource
shared_queue = Queue.Queue()

# Define a mutex
mutex = threading.Lock()

# Define a thread function
def thread_function(q, l):
    for i in range(10):
        # Acquire the mutex
        with l:
            # Add an item to the shared queue
            q.put(i)

# Create a list of threads
threads = []

# Create and start threads
for i in range(5):
    thread = threading.Thread(target=thread_function, args=(shared_queue, mutex))
    thread.start()
    threads.append(thread)

# Join all threads
for thread in threads:
    thread.join()

# Print the items in the shared queue
print(shared_queue.get())
