import logging

def main():
    logging.basicConfig(level=logging.INFO)

    # Log some messages at different levels
    logging.info("This is an info message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")

if __name__ == "__main__":
    main()