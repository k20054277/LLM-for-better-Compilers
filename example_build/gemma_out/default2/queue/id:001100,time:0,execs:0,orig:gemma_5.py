
import threading
import time

def thread_function(num):
    for i in range(num):
        print("Thread", num, "is running")
        time.sleep(1)

if __name__ == "__main__":
    # Create a list of threads
    threads = []

    # Start multiple threads
    for i in range(5):
        thread = threading.Thread(target=thread_function, args=(i,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("All threads have completed")
