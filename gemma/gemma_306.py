
def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

print(list(even_numbers(10)))
