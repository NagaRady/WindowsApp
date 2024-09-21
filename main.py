from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

# Base window class
class BaseWindow(QMainWindow):
    def __init__(self, title):
        super().__init__()
        self.setGeometry(200, 200, 300, 300)  # X, Y, Width, Height
        self.setWindowTitle(title)
        self.initUI()

    def initUI(self):
        # This method should be overridden in each subclass
        pass

# First specific window
class FirstWindow(BaseWindow):
    def initUI(self):
        label = QtWidgets.QLabel(self)
        label.setText("This is the First Window!")
        label.move(100, 130)

# Second specific window
class SecondWindow(BaseWindow):
    def initUI(self):
        label = QtWidgets.QLabel(self)
        label.setText("This is the Second Window!")
        label.move(100, 130)

# Third specific window
class ThirdWindow(BaseWindow):
    def initUI(self):
        label = QtWidgets.QLabel(self)
        label.setText("This is the Third Window!")
        label.move(100, 130)

# Fourth specific window
class FourthWindow(BaseWindow):
    def initUI(self):
        label = QtWidgets.QLabel(self)
        label.setText("This is the Fourth Window!")
        label.move(100, 130)

def main():
    app = QApplication(sys.argv)
    
    first = FirstWindow("First Window")
    second = SecondWindow("Second Window")
    third = ThirdWindow("Third Window")
    fourth = FourthWindow("Fourth Window")

    # Show all windows for demonstration
    first.show()
    second.show()
    third.show()
    fourth.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
