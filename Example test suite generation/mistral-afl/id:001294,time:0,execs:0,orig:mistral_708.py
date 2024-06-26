
import threading
import time

# Initialize a lock and a condition variable
lock = threading.Lock()
cond_var = threading.Condition()

# Define a shared variable (for demonstration purposes)
data = 0

def producer(num):
    """ Producer function that sets the shared data """

    # Wait if the lock is not free, then acquire it
    while not lock.acquire():
        print(f"Producer {threading.current_thread().name} waiting for lock.")
        time.sleep(0.1)

    # Produce data and print the message
    print(f"Producer {threading.current_thread().name}: Setting shared data to {num}")
    global data
    data = num

    # Notify all waiting consumers that data is available
    cond_var.notify()

    # Release the lock
    lock.release()

def consumer(num):
    """ Consumer function that reads the shared data """

    while True:
        # Wait for the lock and condition to be available
        lock.acquire()
        cond_var.wait()

        if data is not None:
            print(f"Consumer {threading.current_thread().name}: Consumed data = {data}")
            global data
            data = None

        # Release the lock and condition
        lock.release()

if __name__ == "__main__":
    producer_thread = threading.Thread(target=producer, args=(1,))
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    # Join threads to the main program execution
    producer_thread.join()
    consumer_thread.join()
