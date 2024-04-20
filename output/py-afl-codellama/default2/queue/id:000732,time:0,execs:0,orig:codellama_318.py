import sys
from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
window = QLabel('Hello World!')
window.show()
sys.exit(app.exec_())