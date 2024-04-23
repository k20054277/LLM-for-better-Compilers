
import threading
import queue

class ProducerConsumerQueue:
    def __init__(self):
        self.q = queue.Queue()
        self.cond = threading.Condition()

    def put(self, item):
        self.q.put(item)
        self.cond.notify()

    def get(self):
        while True:
            if not self.q.empty():
                item = self.q.get()
                print(f'[{threading.current_thread().name}]: Got {item}')
                return item
            else:
                print('Queue is empty. Waiting...')
                self.cond.wait()

    def run(self):
        while True:
            item = yield self
            self.put(item)
