
import threading
import time

def thread_function(n):
    for i in range(n):
        print("Thread", n, "is running")
        time.sleep(1)

# Create a list of threads
threads = []

# Start n threads
for n in range(5):
    thread = threading.Thread(target=thread_function, args=(n,))
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Print "All threads completed"
print("All threads completed")
