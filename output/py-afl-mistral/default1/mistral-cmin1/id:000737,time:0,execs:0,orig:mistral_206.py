
import threading
import time

counter = 0
lock = threading.Lock()

def increment_counter():
    global counter
    
    while True:
        # Acquire the lock before incrementing the counter to avoid race condition.
        with lock:
            if counter < 10:
                counter += 1
                print(f'Thread {threading.current_thread().name} - Counter: {counter}')
                break

        # Release the lock after incrementing to allow other threads to proceed.
        time.sleep(0.1)

threads = [threading.Thread(target=increment_counter) for _ in range(5)]

for thread in threads:
    thread.start()

# Wait for all the threads to finish their task.
for thread in threads:
    thread.join()
