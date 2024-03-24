import time

def print_message(message, delay):
    if message == "Hello":
        return None
    else:
        return message

def main():
    messages = ["Hello", "World"]
    for message in messages:
        result = print_message(message, 1)
        if result is not None:
            process(result)

def process(result):
    # Do something with the result of print_message() here
    pass