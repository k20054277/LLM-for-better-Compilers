import multiprocessing

def test_function(x):
    assert x > 0, "x must be positive"
    return x * x

if __name__ == '__main__':
    p = multiprocessing.Pool()
    results = p.map(test_function, [1, -2, 3])
    print(results)