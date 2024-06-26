from contextlib import contextmanager

@contextmanager
def my_context_manager():
    print("Entering my_context_manager")
    try:
        yield "Hello from my_context_manager"
    finally:
        print("Exiting my_context_manager")

with my_context_manager() as message:
    print(message)