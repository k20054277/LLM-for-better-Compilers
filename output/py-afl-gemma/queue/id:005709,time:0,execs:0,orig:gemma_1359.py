
import unittest

def complex_number(x, y):
    return complex(x, y)


class TestComplexNumber(unittest.TestCase):

    def setUp(self):
        self.c = complex_number(2, 3)

    def test_real_part(self):
        self.assertEqual(self.c.real, 2)

    def test_imag_part(self):
        self.assertEqual(self.c.imag, 3)

    def test_conjugate(self):
        self.assertEqual(complex_number(2, 3).conjugate(), complex_number(2, -3))


if __name__ == "__main__":
    unittest.main()
