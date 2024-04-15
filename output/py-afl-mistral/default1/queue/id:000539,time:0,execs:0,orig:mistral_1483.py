
import threading

class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

def increment_counter(counter):
    with counter.lock:
        assert isinstance(counter, Counter), "Counter is not initialized."
        counter.value += 1
        print(f"Thread {threading.current_thread().name} increments the counter to {counter.value}")

class ThreadA(threading.Thread):
    def run(self):
        counter = Counter()
        for _ in range(10):
            increment_counter(counter)

class ThreadB(threading.Thread):
    def run(self):
        counter = Counter()
        for _ in range(10):
            increment_counter(counter)

if __name__ == "__main__":
    thread_a = ThreadA()
    thread_b = ThreadB()

    thread_a.start()
    thread_b.start()

    thread_a.join()
    thread_b.join()
