def true_yield():
    for i in range(5):
        if i % 2 == 0:
            yield True
        else:
            yield False

for result in true_yield():
    print(result)