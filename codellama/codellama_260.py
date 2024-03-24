import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = QtWidgets.QPushButton("Click me!", self)
        self.button.clicked.connect(self.print_hello)
        self.setCentralWidget(self.button)

    def print_hello(self):
        print("Hello World!")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())