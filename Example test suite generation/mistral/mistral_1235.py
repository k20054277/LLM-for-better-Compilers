
import threading
import time

counter = 0
lock = threading.Lock()

def increment_counter(thread_name):
    global counter
    for i in range(100):
        with lock:
            old_value = counter
            new_value = old_value + 1
            counter = new_value
        print(f"Thread {thread_name} incremented the counter from {old_value} to {counter}")
        time.sleep(0.01)

def thread_function():
    thread_name = threading.current_thread().name
    increment_counter(thread_name)

if __name__ == '__main__':
    threads = [threading.Thread(target=thread_function, name='ThreadA') for i in range(2)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
