import numpy as np

def test_function(x):
    assert x > 0, "x must be positive"
    return x ** 2 + 1

x = np.array([-1, 0, 1])
y = test_function(x)
print(y)