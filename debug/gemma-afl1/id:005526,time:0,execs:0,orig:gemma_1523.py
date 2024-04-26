
import unittest

class MyTest(unittest.TestCase):

    def setUp(self):
        self.my_variable = 10

    def tearDown(self):
        print("Test completed")

    def test_assert(self):
        self.assertEqual(self.my_variable, 10)

    def test_with_context_manager(self):
        with self.assertRaises(ZeroDivisionError):
            self.assertEqual(self.my_variable / 0, 0)


if __name__ == "__main__":
    unittest.main()
