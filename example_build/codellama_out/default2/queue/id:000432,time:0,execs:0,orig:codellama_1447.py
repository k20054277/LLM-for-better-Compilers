import gc

def test_assert():
    x = 5
    assert x == 5, "x is not equal to 5"
    print("Assertion passed!")

def test_garbage_collection():
    x = 5
    y = 10
    del x
    gc.collect()
    print(y)

if __name__ == "__main__":
    test_assert()
    test_garbage_collection()