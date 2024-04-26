def my_function():
    i = 0
    while True:
        if i % 2 == 0:
            yield False
        else:
            yield True
        i += 1

for result in my_function():
    print(result)