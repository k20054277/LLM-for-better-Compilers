
import time

def long_running_task(num):
    """A simple long-running task"""
    print(f"Task {num} started")
    time.sleep(2)  # Simulate some heavy computation
    print(f"Task {num} completed")
