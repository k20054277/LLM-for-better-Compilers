
import threading
import time

# Define a shared resource that requires mutual exclusion
resource = 0
lock = threading.Lock()

# Define a function to be executed in threads
def worker(thread_id):
    global resource

    # Demonstrate the use of Boolean flags
    flag = not thread_id % 2

    print(f"Thread {thread_id} is waiting for its turn to access the shared resource...")
    
    while flag:
        if lock.acquire(blocking=True):
            # Critical section: Access the shared resource
            if resource > 0:
                print(f"Thread {thread_id} found a non-zero value in the shared resource.")
                resource += 1
                print(f"Thread {thread_id} updated the shared resource to {resource}")
            else:
                print(f"Thread {thread_id} did not find anything in the shared resource.")

            lock.release()
        else:
            print("Thread", thread_id, "is waiting for the lock to be released...")
            time.sleep(0.1)
    
# Create and start threads
threads = [threading.Thread(target=worker, args=(i,)) for i in range(4)]
for t in threads:
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()
