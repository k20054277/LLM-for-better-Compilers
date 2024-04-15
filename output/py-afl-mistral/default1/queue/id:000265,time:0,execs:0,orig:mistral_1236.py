
import multiprocessing

# Function representing a resource with a lock
def acquire_resource(name, lock):
    print(f"{Process.current_process().name}: Acquiring {name}...")
    lock.acquire()

# Function representing a producer producing data
def producer(data):
    print(f"Producer: Produced data: {data}")
    resource1.release()  # Release resource 1 before acquiring resource 2 (deadlock condition)
    acquire_resource("Resource 2", resource2.lock)

# Function representing a consumer consuming data
def consumer(data):
    print(f"Consumer: Consumed data: {data}")
    resource2.release()  # Release resource 2 before acquiring resource 1 (deadlock condition)
    acquire_resource("Resource 1", resource1.lock)

# Creating resources and locks
resource1 = multiprocessing.Lock()
resource2 = multiprocessing.Lock()

# Creating processes
processes = [multiprocessing.Process(target=producer, args=(i,)) for i in range(3)]
consumers = [multiprocessing.Process(target=consumer, args=(i,)) for i in range(3)]

# Starting processes
for p in processes:
    p.start()

for c in consumers:
    c.start()

# Waiting for processes to finish
for p in processes + consumers:
    p.join()
