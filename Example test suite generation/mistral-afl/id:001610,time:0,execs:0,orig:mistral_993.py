
import threading
import time

# Shared variable
shared_var = 0

# Mutex lock
mutex = threading.Lock()

def function(num):
    for i in range(10):
        # Acquire mutex lock
        mutex.acquire()

        # Critical section: update the shared variable
        global shared_var
        shared_var += num

        print(f'Thread {threading.current_thread().name}: updated shared_var to {shared_var}')

        # Release mutex lock
        mutex.release()

        # Sleep for a little while to allow other thread to have some time
        time.sleep(0.01)

# Create two threads
thread1 = threading.Thread(target=function, args=(1,))
thread2 = threading.Thread(target=function, args=(2,))

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish their execution
thread1.join()
thread2.join()

print("Main thread: shared_var = ", shared_var)
