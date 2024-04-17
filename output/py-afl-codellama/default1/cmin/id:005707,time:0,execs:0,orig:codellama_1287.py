def generator():
    i = 0
    while True:
        assert i < 10, "i is greater than 10"
        yield i
        i += 1

for num in generator():
    print(num)