
import threading
import time

def thread_function(num):
    for i in range(num):
        print("Thread", num, "is running")
        time.sleep(1)

if __name__ == "__main__":
    threads = []
    for i in range(5):
        thread = threading.Thread(target=thread_function, args=(i,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("All threads have completed")
