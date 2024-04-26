
import tensorflow as tf
import unittest

class TestTensorFlow(unittest.TestCase):

    def setUp(self):
        self.x = tf.constant(5)

    def test_tensor_value(self):
        self.assertEqual(self.x.numpy(), 5)

    def test_tensor_sum(self):
        self.assertEqual(self.x + 10, tf.constant(15))

if __name__ == "__main__":
    unittest.main()
