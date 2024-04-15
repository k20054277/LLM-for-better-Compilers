
import threading
import time

def func(id):
    print("Function {} starting".format(id))
    time.sleep(5)
    print("Function {} ended".format(id))

if __name__ == "__main__":
    threads = []

    for i in range(3):
        t = threading.Thread(target=func, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
