
import pyqt.qtwidgets as qtw
import unittest

class ExampleTest(unittest.TestCase):

    def setUp(self):
        self.window = qtw.QWidget()

    def tearDown(self):
        self.window.close()

    def test_assert_equal(self):
        self.assertEqual(self.window.title(), "PyQt Example")

    def test_assert_greater_than(self):
        self.assertGreater than(self.window.width(), 500)


if __name__ == "__main__":
    unittest.main()
