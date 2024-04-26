def test_assert():
    x = 5
    y = 10
    assert x < y, "x is not less than y"

try:
    test_assert()
except AssertionError as error:
    print("Assertion failed:", error)