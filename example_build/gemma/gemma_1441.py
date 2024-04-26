
import pytorch
import unittest

class TestPytorch(unittest.TestCase):
    def setUp(self):
        self.x = pytorch.randn(3, 3)

    def test_pytorch(self):
        # Assert that the tensor has the expected shape
        self.assertEqual(self.x.shape, (3, 3))

        # Assert that the tensor is approximately equal to the expected value
        self.assertAlmostEqual(self.x.mean(), 0.0)

if __name__ == "__main__":
    unittest.main()
