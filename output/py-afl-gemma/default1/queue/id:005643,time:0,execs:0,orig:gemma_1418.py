
import datetime
import unittest

class TestDatetime(unittest.TestCase):

    def setUp(self):
        self.datetime_obj = datetime.datetime.now()

    def test_datetime_object(self):
        assert isinstance(self.datetime_obj, datetime.datetime)
        self.assertEqual(self.datetime_obj.year, 2023)
        self.assertEqual(self.datetime_obj.month, 10)
        self.assertEqual(self.datetime_obj.day, 26)

    def test_datetime_now(self):
        assert datetime.datetime.now() is not None
        self.assertIsNotEqual(datetime.datetime.now(), self.datetime_obj)

if __name__ == '__main__':
    unittest.main()
