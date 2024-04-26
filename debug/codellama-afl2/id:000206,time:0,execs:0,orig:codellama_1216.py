import threading
import time

def worker():
    print("Worker running...")
    time.sleep(2)
    print("Worker finished.")

def main():
    # Create a worker thread
    t = threading.Thread(target=worker, args=(1,))
    # Start the worker thread
    t.start()
    # Wait for the worker to finish
    t.join()

if __name__ == '__main__':
    main()