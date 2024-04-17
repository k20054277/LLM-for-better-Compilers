import sys
from PyQt5 import QtWidgets, QtCore

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("My Window")
        self.label = QtWidgets.QLabel("Hello World", self)
        self.label.move(30, 60)
        self.button = QtWidgets.QPushButton("Click me!", self)
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        assert False, "This is a test assertion"

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())