
import threading

class SharedData:
    def __init__(self):
        self._value = None
        self._lock = threading.Lock()

data = SharedData()
