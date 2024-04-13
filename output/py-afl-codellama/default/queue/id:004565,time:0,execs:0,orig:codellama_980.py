import threading
import time

# Create a queue to store the data produced by the producer
data_queue = Queue()

# Create a semaphore for the producer to signal that it has finished producing data
producer_done = Semaphore(0)

# Create a semaphore for the consumer to signal that it has finished consuming data
consumer_done = Semaphore(0)

def producer():
    # Produce data and add it to the queue
    for i in range(10):
        time.sleep(1)
        data_queue.put(i)

    # Signal that the producer is done producing data
    producer_done.release()

def consumer():
    # Consume data from the queue until the producer is done
    while True:
        try:
            data = data_queue.get(timeout=1)
        except Empty:
            break

        print("Consumed data:", data)

        # Signal that the consumer has consumed some data
        consumer_done.release()

# Create a thread for the producer and a thread for the consumer
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Start the threads
producer_thread.start()
consumer_thread.start()

# Wait for both threads to finish
producer_thread.join()
consumer_thread.join()