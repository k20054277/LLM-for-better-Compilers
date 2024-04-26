
import time

def worker1(tag):
    print(f"Worker 1 started with tag: {tag}")
    time.sleep(3)
    print("Worker 1 finished")

if __name__ == "__main__":
    import multiprocessing

    process = multiprocessing.Process(target=worker1, args=(1,))
    process.start()
    process.join()
