
import threading
import time

def thread_function(name):
    for i in range(10):
        print("Hello, " + name + "!")
        time.sleep(1)

if __name__ == "__main__":
    # Create a list of threads
    threads = []

    # Start a thread for each name
    for name in ["Alice", "Bob", "Charlie"]:
        thread = threading.Thread(target=thread_function, args=("Thread " + name,))
        threads.append(thread)

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("All threads completed!")
