
import threading
import time

# Create a boolean variable and a lock
shared_data = True
lock = threading.Lock()

def worker(num):
    """Function to be executed by each worker thread."""

    # Acquire the lock before accessing shared data
    with lock:
        if not shared_data:
            print(f"Thread {num}: Data is already processed.")
            return
        shared_data = False

    print(f"Thread {num}: Processing data...")
    time.sleep(2)
    print(f"Thread {num}: Data processing completed.")

if __name__ == "__main__":
    threads = [threading.Thread(target=worker, args=(i,)) for i in range(5)]

    # Start all worker threads
    for thread in threads:
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()
