
import threading
import time

class MyLock(threading.RLock):
    pass

class Worker(threading.Thread):
    def __init__(self, name, lock):
        super().__init__()
        self.name = name
        self.lock = lock

    def run(self):
        while True:
            self.lock.acquire()  # Acquire the lock before accessing shared resource
            print(f"Thread {self.name} started.")
            self.do_work()
            self.lock.release()   # Release the lock after finishing work
            time.sleep(1)

    def do_work(self):
        """Perform some computational work."""
        print(f"Thread {self.name} doing some work...")
        for i in range(10):
            # Some heavy computation...
            x = i * i
            time.sleep(0.1)

if __name__ == "__main__":
    lock = MyLock()
    workers = [Worker("Worker-{}".format(i), lock) for i in range(5)]

    for worker in workers:
        worker.start()
