
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        label = QLabel("Enter a number between 1 and 10:")
        line_edit = QLineEdit(self)
        button = QPushButton("Submit", self)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(line_edit)
        layout.addWidget(button)

        self.setLayout(layout)
        self.setWindowTitle('PyQt5 Assert Example')
        self.show()

        button.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        try:
            number = int(self.findChild(QLineEdit, "lineEdit").text())
            assert 1 <= number <= 10, "Number must be between 1 and 10."
            label = self.findChild(QLabel, "label")
            label.setText("You entered: {}".format(number))
        except AssertionError as e:
            QMessageBox.critical(self, 'Input error', e)
        except ValueError:
            QMessageBox.information(self, 'Error', 'Please enter a valid number.')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
