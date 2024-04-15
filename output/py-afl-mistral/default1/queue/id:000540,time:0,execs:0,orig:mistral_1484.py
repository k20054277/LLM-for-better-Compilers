
import threading
import time

QUEUE_SIZE = 5
data_queue = []
lock = threading.Lock()
condition = threading.Condition()

class Producer(threading.Thread):
    def run(self):
        for i in range(10):
            with lock:
                while len(data_queue) >= QUEUE_SIZE:
                    condition.wait_for(lock)
            data = i
            print(f"Producer produced item {data}")
            self.assert(len(data_queue) < QUEUE_SIZE, msg="Queue is full!")
            with lock:
                data_queue.append(data)
                condition.notify()
                time.sleep(1)

class Consumer(threading.Thread):
    def run(self):
        for i in range(10):
            with lock:
                while len(data_queue) == 0:
                    condition.wait_for(lock)
            item = data_queue.pop()
            print(f"Consumer consumed item {item}")
            self.assert(len(data_queue) > 0, msg="Queue is empty!")
            time.sleep(1)

if __name__ == "__main__":
    producer = Producer()
    consumer = Consumer()

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()
