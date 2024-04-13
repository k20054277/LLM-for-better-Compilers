def test_assertion():
    x = 5
    y = 10
    assert x < y, "x is not less than y"
    print("x is less than y")

if __name__ == '__main__':
    test_assertion()