import sys
from PyQt5.QtWidgets import QApplication, QPushButton

class Window(QPushButton):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt')
        self.setGeometry(300, 300, 300, 150)
        self.setObjectName("button")
        self.clicked.connect(self.handle_click)

    def handle_click(self):
        print("Button clicked")

def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()