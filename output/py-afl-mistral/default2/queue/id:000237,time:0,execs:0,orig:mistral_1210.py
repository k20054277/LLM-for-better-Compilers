
def celsius_to_fahrenheit(celsius):
    try:
        fahrenheit = (celsius * 9 / 5) + 32
        return fahrenheit
    except Exception as e:
        print(f"Error occurred: {e}")
        raise

def test_celsius_to_fahrenheit():
    assert type(celsius_to_fahrenheit(-10)) is <class 'float'>
    assert round(celsius_to_fahrenheit(-10), 2) == -6.8
    assert celsius_to_fahrenheit(37) == 98.6

if __name__ == "__main__":
    test_celsius_to_fahrenheit()
