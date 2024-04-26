
import sys
from PyQt5.QtWidgets import QApplication, QWidget

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 200, 200)
        self.setWindowTitle("PyQt Example")

        self.button = QtWidgets.QPushButton("Click me")
        self.button.clicked.connect(self.on_click)

        self.show()

    def on_click(self):
        print("Button clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
