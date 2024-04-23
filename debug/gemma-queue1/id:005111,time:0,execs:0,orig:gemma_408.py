
import threading
import time

# Define a function to be executed in a thread
def thread_function(num):
    for i in range(num):
        print("Thread:", i)
        time.sleep(1)

# Create a list of threads
threads = []

# Create and start threads
for i in range(5):
    thread = threading.Thread(target=thread_function, args=(i,))
    thread.start()
    threads.append(thread)

# Join all threads
for thread in threads:
    thread.join()

# Print the main message
print("Main:", "All threads completed")
