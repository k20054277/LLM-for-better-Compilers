import threading

def do_something(i):
    print("Doing something...")
    time.sleep(1)
    return i * 2

if __name__ == "__main__":
    threads = []
    for i in range(5):
        t = threading.Thread(target=do_something, args=(i,))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print("All threads finished!")