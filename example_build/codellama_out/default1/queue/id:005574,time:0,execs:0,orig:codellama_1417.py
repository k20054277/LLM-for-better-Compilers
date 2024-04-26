import logging

def test_assert(x):
    assert x > 0, "x must be positive"

def main():
    try:
        test_assert(-1)
    except AssertionError as e:
        logging.error("Assertion failed: {}".format(e))

if __name__ == "__main__":
    main()