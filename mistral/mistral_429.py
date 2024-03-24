
import logging

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler = logging.FileHandler("app.log")
file_handler.setFormatter(formatter)
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

class MyClass:
    def __init__(self):
        self.data = None

    def method(self):
        """A simple method that returns None"""
        return None

if __name__ == "__main__":
    my_instance = MyClass()
    result = my_instance.method()
    
    logger.debug("Instance initialized")
    logger.info("Method called, returned None")
    if result is not None:
        logger.warning(f"Unexpected non-None value: {result}")

logger.info("Program ended successfully")
