
import threading
import time

def thread_function(n):
    for i in range(n):
        print("Thread %s is running" % n)
        time.sleep(1)

# Create a list of threads
threads = []

# Create and start threads
for i in range(5):
    thread = threading.Thread(target=thread_function, args=(i,))
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All threads have completed")
