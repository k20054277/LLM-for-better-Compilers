
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class MyClass:
    def __init__(self, arg=None):
        self.arg = arg

if __name__ == "__main__":
    my_instance = MyClass()
    logging.info(f"Created an instance of MyClass with argument: {my_instance.arg}")

    my_instance.arg = "some value"
    logging.info(f"Assigned a new value to the argument: {my_instance.arg}")
