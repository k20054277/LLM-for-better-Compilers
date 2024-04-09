
import threading
import time

def thread_function(n):
    for i in range(n):
        print("Thread:", i)
        time.sleep(1)

if __name__ == "__main__":
    # Create a thread
    thread = threading.Thread(target=thread_function, args=(5,))

    # Start the thread
    thread.start()

    # Wait for the thread to complete
    thread.join()

    print("Main:", "Finished")
