
import unittest

def divisible(num1, num2):
    return num1 % num2 == 0


class Test divisible(unittest.TestCase):

    def setUp(self):
        self.num1 = 10
        self.num2 = 2

    def test_ divisible(self):
        self.assertEqual(divisible(self.num1, self.num2), True)


if __name__ == "__main__":
    unittest.main()
