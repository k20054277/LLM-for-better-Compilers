import threading

def greet(name):
    print("Hello, " + name)

names = ["Alice", "Bob", "Charlie"]
threads = []
for name in names:
    t = threading.Thread(target=greet, args=(name,))
    threads.append(t)
    t.start()