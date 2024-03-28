import sys
from PyQt5 import QtWidgets, QtCore

class Example(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Example")
        self.resize(300, 200)
        
        self.btn = QtWidgets.QPushButton("Press me!", self)
        self.btn.move(100, 100)
        self.btn.clicked.connect(self.on_click)
    
    def on_click(self):
        print("Hello, world!")
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())