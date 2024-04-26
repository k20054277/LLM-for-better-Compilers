
from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

class MyApp(QWidget):
    def __init__(self, title="PyQt with None"):
        super().__init__()

        self.title = title
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("No button clicked yet")
        layout.addWidget(self.label)

        self.button = QPushButton("Click me!")
        self.button.clicked.connect(self.on_button_clicked)
        layout.addWidget(self.button)

        self.setLayout(layout)
        self.setWindowTitle(self.title)
        self.show()

    def on_button_clicked(self):
        if self.label.text() == "No button clicked yet":
            self.label.setText("Button clicked!")
        else:
            self.label.setText("No button clicked yet")

if __name__ == "__main__":
    app = QApplication(argv)
    
    my_app = MyApp()
    my_app.exec_()
