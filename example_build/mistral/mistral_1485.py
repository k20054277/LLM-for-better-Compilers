
import threading
import time

class Queue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size
        self.mutex = threading.Lock()
        self.not_full = threading.Semaphore(value=max_size)
        self.not_empty = threading.Semaphore(value=0)

    def put(self, item):
        with self.mutex:
            self.not_full.acquire()
            assert len(self.queue) < self.max_size, "Queue is full!"
            self.queue.append(item)

        print(f'Produced: {item}')
        self.not_empty.release()

    def get(self):
        with self.mutex:
            self.not_empty.acquire()
            assert len(self.queue) > 0, "Queue is empty!"
            item = self.queue.pop()

        print(f'Consumed: {item}')
        self.not_full.release()

class Producer(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        for i in range(10):
            self.queue.put(i)
            time.sleep(0.1)

class Consumer(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        for _ in range(10):
            self.queue.get()
            time.sleep(0.1)

if __name__ == '__main__':
    queue = Queue(max_size=5)
    producer = Producer(queue)
    consumer = Consumer(queue)

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()
