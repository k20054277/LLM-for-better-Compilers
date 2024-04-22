
import threading
import time

# Define a function for our worker thread
def worker(id):
    print(f"Thread {id} started.")
    time.sleep(5)
    print(f"Thread {id} finished.")

# Create two threads and start them
threads = []
for i in range(2):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

# Wait for all threads to finish before exiting the main thread
for thread in threads:
    thread.join()

print("All threads finished.")
