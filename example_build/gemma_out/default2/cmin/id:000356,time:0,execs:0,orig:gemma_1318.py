
import unittest

async def my_async_function():
    return True

class MyTest(unittest.TestCase):
    def setUp(self):
        self.my_async_function_result = my_async_function()

    def test_my_async_function(self):
        assert self.my_async_function_result is True

if __name__ == "__main__":
    unittest.main()
