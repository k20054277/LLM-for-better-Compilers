
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        self.label1 = QLabel("Input 1:")
        self.lineedit1 = QLineEdit()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.lineedit1)

        self.label2 = QLabel("Input 2:")
        self.lineedit2 = QLineEdit()
        vbox.addWidget(self.label2)
        vbox.addWidget(self.lineedit2)

        self.button = QPushButton("Check Inputs")
        self.button.clicked.connect(self.check_inputs)
        vbox.addWidget(self.button)

        self.show()

    def check_inputs(self):
        input1 = self.lineedit1.text()
        input2 = self.lineedit2.text()

        if len(input1) > 0 and len(input2) > 0:
            print("Both inputs are non-empty!")
            # Add your code here to perform actions based on both inputs being non-empty
        else:
            print("One or both inputs are empty.")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    demo = MyApp()
    sys.exit(app.exec_())
