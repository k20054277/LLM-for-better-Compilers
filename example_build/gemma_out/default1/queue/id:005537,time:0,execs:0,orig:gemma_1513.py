
import unittest
import paralle

def test_assert_and_parallel(num):
    assert num % 2 == 0
    print(num)

# Define a list of tests
tests = [test_assert_and_parallel(i) for i in range(1, 11)]

# Run the tests in parallel
unittest.main(parallel=True)
