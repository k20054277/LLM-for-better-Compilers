import threading

def worker(lock):
    # Acquire the lock
    with lock:
        print("Worker thread acquired the lock")
        # Sleep for 1 second to simulate work
        time.sleep(1)
        print("Worker thread released the lock")

# Create a lock object
lock = threading.Lock()

# Create two worker threads
worker_thread1 = threading.Thread(target=worker, args=(lock,))
worker_thread2 = threading.Thread(target=worker, args=(lock,))

# Start the worker threads
worker_thread1.start()
worker_thread2.start()

# Join the worker threads
worker_thread1.join()
worker_thread2.join()