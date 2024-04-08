
import sys
from PyQt5.QtWidgets import QApplication, QWidget

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PyQt Example")
        self.setGeometry(100, 100, 400, 200)

        self.button = QPushButton("Click me")
        self.button.clicked.connect(self.on_click)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def on_click(self):
        print("Button clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    example = Example()
    example.show()
    sys.exit(app.exec_())
