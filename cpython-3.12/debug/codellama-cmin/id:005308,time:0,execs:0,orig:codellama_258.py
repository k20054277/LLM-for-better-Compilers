import threading

def do_something(name):
    print(f"{name} is doing something")

def main():
    t1 = threading.Thread(target=do_something, args=("Alice",))
    t2 = threading.Thread(target=do_something, args=("Bob",))

    t1.start()
    t2.start()

    print("Main thread is doing something")

    # Wait for both threads to finish
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()