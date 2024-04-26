
import threading
import unittest

def thread_function(n):
    assert n > 0
    print("Thread:", n)

def main():
    threads = []
    for i in range(5):
        thread = threading.Thread(target=thread_function, args=(i,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("Main completed")

if __name__ == "__main__":
    unittest.main()
    main()
