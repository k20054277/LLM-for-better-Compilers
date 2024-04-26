
import random
import unittest

def race_condition():
    x = 0
    for _ in range(1000):
        thread1()
        thread2()
        assert x == 1000

def thread1():
    global x
    x += 1

def thread2():
    global x
    x += 1

class Test(unittest.TestCase):
    def setUp(self):
        self.assert_ = unittest.mock.assert_

    def test_race_condition(self):
        race_condition()
        self.assert_called_with(x, 1000)

if __name__ == "__main__":
    unittest.main()
