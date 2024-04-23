import threading

def worker():
    # do some work
    pass

if __name__ == '__main__':
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()