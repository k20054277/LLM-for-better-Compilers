
import assert
with open("test.txt") as f:
    assert f.read() == "Hello, world!"

print("Test passed!")
