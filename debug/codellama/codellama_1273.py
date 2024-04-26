def main():
    try:
        # Code that may raise an exception
        x = 10 / 0
        assert x == 5, "x should be equal to 5"
    except ZeroDivisionError as e:
        print("ZeroDivisionError occurred:", e)