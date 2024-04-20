def test_and_lambda():
    numbers = [1, 2, 3, 4, 5]
    even_numbers = filter(lambda x: x % 2 == 0, numbers)
    print(list(even_numbers))

test_and_lambda()