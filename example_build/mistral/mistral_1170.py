
from PyQt5 import QtCore, QtGui, QtWidgets

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt Example")
        self.setGeometry(300, 300, 400, 300)

        label = QtWidgets.QLabel("Hello, PyQt!", parent=self)
        label.move(50, 100)

        self.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication.instance() if QtWidgets.QApplication.instance() else QtWidgets.QApplication.new_instance(sys.argv)
    as my_app(MyApp())
    sys.exit(app.exec_())
