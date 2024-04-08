def my_function(x):
    assert x > 0, "x must be positive"
    return x ** 2

@deployment
def main():
    result = my_function(-1)
    print(result)