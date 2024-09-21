import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget

# Define a class for each sub-window
class SubWindow(QWidget):
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(100, 100, 300, 200)
        self.initUI()
    
    def initUI(self):
        label = QLabel("This is the " + self.windowTitle() + ".", self)
        label.move(50, 50)

# Main Window class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 600, 400)
        self.initUI()
    
    def initUI(self):
        self.buttons = []
        titles = ['Window 1', 'Window 2', 'Window 3', 'Window 4']
        for i, title in enumerate(titles):
            btn = QPushButton('Open ' + title, self)
            btn.move(50, 50 + i*50)
            btn.clicked.connect(self.make_show_window(title))
            self.buttons.append(btn)

    def make_show_window(self, title):
        def show_window():
            window = SubWindow(title)
            window.show()
        return show_window

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
