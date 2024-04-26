
import threading
import time

# Shared variable or resource
shared_data = 0

# Mutex lock for the shared data
lock = threading.Lock()

def increment():
    global shared_data

    # Acquire the mutex lock before accessing the shared data
    with lock:
        shared_data += 1
        print(f"Thread {threading.current_thread().name}: Increased shared data to {shared_data}")

if __name__ == "__main__":
    threads = []

    # Create and start five threads that will increment the shared data
    for i in range(5):
        thread = threading.Thread(target=increment)
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish their execution
    for thread in threads:
        thread.join()

print("Shared data has been incremented 5 times")
