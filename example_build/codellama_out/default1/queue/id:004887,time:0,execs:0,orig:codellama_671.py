def test_true():
    x = 5
    y = 10
    if x > y:
        print("x is greater than y")
    else:
        print("x is not greater than y")

def test_locals():
    x = 5
    y = 10
    z = 15
    print(locals())

test_true()
test_locals()