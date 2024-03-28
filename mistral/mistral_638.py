
import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt & True Example")

        self.central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QtWidgets.QHBoxLayout(self.central_widget)

        self.button1 = QtWidgets.QPushButton("Button 1")
        self.button1.clicked.connect(lambda: print(f"Button 1 clicked: {self.button1.isChecked()}"))

        self.button2 = QtWidgets.QPushButton("Button 2")
        self.button2.clicked.connect(lambda: print(f"Button 2 clicked: {self.button2.isChecked()}"))

        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MyApp()
    window.show()
    sys.exit(app.exec_())
