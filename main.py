from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)  # X, Y, Width, Height
    win.setWindowTitle("My First PyQt Application")
    
    label = QtWidgets.QLabel(win)
    label.setText("Hello, this is a simple PyQt window!")
    label.move(100, 100)

    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    window()
