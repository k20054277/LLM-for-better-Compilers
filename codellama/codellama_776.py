import threading

def worker(name, lock):
    # Acquire the lock before accessing shared data
    with lock:
        print(f"Worker {name} has started.")
        
        # Sleep for a random amount of time to simulate work
        time.sleep(random.uniform(1, 5))
        
        # Release the lock after accessing shared data
        print(f"Worker {name} has finished.")
    
# Create a mutex object and a list of worker threads
lock = threading.Lock()
workers = []
for i in range(5):
    workers.append(threading.Thread(target=worker, args=(f"Worker {i}", lock)))

# Start the worker threads
for w in workers:
    w.start()

# Join the worker threads to wait for them to finish
for w in workers:
    w.join()