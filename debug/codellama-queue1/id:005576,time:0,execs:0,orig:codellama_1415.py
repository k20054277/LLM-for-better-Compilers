def test_function():
    x = 5
    y = 10
    z = x + y
    assert z > 15, "The sum of x and y is not greater than 15"
    try:
        if z < 20:
            raise Exception("The sum of x and y is less than 20")
    except Exception as e:
        print(e)