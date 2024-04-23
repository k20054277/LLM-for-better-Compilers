
import threading

# Function that will be run in a new thread
def worker(arg=None):
    if arg is not None:
        print("Thread received argument:", arg)
    else:
        print("Thread does not have an argument")

# Create a new thread and start the function
thread = threading.Thread(target=worker, args=(None,))
thread.start()

# Function that runs in the main thread
def main():
    arg = "Hello from main thread"
    print("Main thread has an argument:", arg)
    # Start worker thread with an argument
    thread2 = threading.Thread(target=worker, args=(arg,))
    thread2.start()

if __name__ == "__main__":
    main()
