
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        self.label.setText("Hello, True!")

        self.button = QPushButton("Click me")
        self.button.clicked.connect(self.on_click)

        self.setLayout(self.hbox)

    def on_click(self):
        self.label.setText("True, you clicked me!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    example = Example()
    example.show()
    app.exec_()
