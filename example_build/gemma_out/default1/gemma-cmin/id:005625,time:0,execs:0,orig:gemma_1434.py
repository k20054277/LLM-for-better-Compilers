
import matplotlib.pyplot as plt
import unittest

class TestMatplotlib(unittest.TestCase):

    def setUp(self):
        self.x = [1, 2, 3, 4, 5]
        self.y = [i**2 for i in self.x]

    def test_matplotlib(self):
        # Create a line plot
        plt.plot(self.x, self.y)
        plt.xlabel("X-axis label")
        plt.ylabel("Y-axis label")
        plt.title("Line Plot")

        # Assert that the plot has the correct title and labels
        self.assertEqual(plt.title().get_text(), "Line Plot")
        self.assertEqual(plt.xlabel().get_text(), "X-axis label")
        self.assertEqual(plt.ylabel().get_text(), "Y-axis label")

        # Display the plot
        plt.show()

if __name__ == "__main__":
    unittest.main()
