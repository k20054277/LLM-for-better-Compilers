import threading

def print_hello(name):
    print("Hello, " + name)

def main():
    threads = []
    for i in range(5):
        t = threading.Thread(target=print_hello, args=("World",))
        threads.append(t)
        t.start()

if __name__ == "__main__":
    main()