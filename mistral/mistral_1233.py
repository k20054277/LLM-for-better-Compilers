
import threading
import queue
import time

class ProducerThread(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        count = 1
        while True:
            self.queue.put(count)
            print(f"Produced item {count}")
            count += 1
            time.sleep(1)

class ConsumerThread(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            print(f"Consumed item {item}")
            time.sleep(1)

if __name__ == "__main__":
    queue = queue.Queue()

    producer_thread = ProducerThread(queue)
    consumer_thread = ConsumerThread(queue)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()
