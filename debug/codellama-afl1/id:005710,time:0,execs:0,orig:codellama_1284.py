def demo_assert():
    x = 5
    y = "hello"
    z = 10
    assert x > 0, "x must be greater than 0"
    assert y == "hello", "y must be equal to 'hello'"
    assert z > 0, "z must be greater than 0"

def demo_raise():
    try:
        raise ValueError("This is a value error")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    demo_assert()
    demo_raise()