
import pytest

@pytest.fixture(name="custom_number")
def fixture_custom_number():
    number = 42
    yield number
    print("Custom fixture cleaned up.")

@pytest.fixture
def double(custom_number):
    value = custom_number * 2
    yield value
    print("Double fixture cleaned up.")
