
import threading
import time

def worker_function(name):
    print(f"{name}: Started")
    irepeat = 0
    while True:
        if should_stop:
            print(f"{name}: Stopping...")
            break
        irerepeat += 1
        print(f"{name}: Repeating {irepeat}")
        time.sleep(2)

should_stop = False
thread1 = threading.Thread(target=worker_function, args=("Thread 1",))
thread2 = threading.Thread(target=worker_function, args=("Thread 2",))

# Start the threads
thread1.start()
thread2.start()

# Wait for some time to let the threads run for a while
time.sleep(10)

# Stop both threads
should_stop = True
thread1.join()
thread2.join()
print("All threads stopped.")
