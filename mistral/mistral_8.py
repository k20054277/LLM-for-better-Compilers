
# Synchronous Python program demonstrating the use of False

def function_that_returns_false():
    """A simple function that always returns False"""
    return False

if __name__ == '__main__':
    is_true = True

    while is_true:
        print("This statement will be printed repeatedly until is_true becomes False.")
        is_true = function_that_returns_false()
        
    print("The while loop has terminated because a False value was returned.")
