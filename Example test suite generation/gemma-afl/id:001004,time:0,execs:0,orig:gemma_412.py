
import pyqt

# Define a function that returns False
def is_even(n):
    return n % 2 == 0

# Create a PyQt window
app = pyqt.QtWidgets.QApplication(sys.argv)
window = pyqt.QtWidgets.QMainWindow()

# Create a label to display the result
label = pyqt.QtWidgets.QLabel()

# Set the label text
label.setText("The number is even: {}".format(is_even(10)))

# Show the window
window.show()

# Run the event loop
app.exec_()
