import sys
from PyQt5 import QtWidgets, QtCore

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("PyQt Example")
        self.resize(640, 480)
        
        self.label = QtWidgets.QLabel("Hello, World!", self)
        self.label.move(30, 50)
        
        self.pushButton = QtWidgets.QPushButton("Click me!", self)
        self.pushButton.move(160, 200)
        self.pushButton.clicked.connect(self.button_clicked)
        
    def button_clicked(self):
        print("Button clicked")
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec_())