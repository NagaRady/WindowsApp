import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QDockWidget, QTextEdit, QListWidget, QMenuBar, QAction)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My RStudio-like App')
        self.setGeometry(100, 100, 800, 600)
        self.initUI()

    def initUI(self):
        # Central widget (text editor)
        self.central_widget = QTextEdit()
        self.setCentralWidget(self.central_widget)

        # Dock Widget 1: Console
        self.dock_console = QDockWidget("Console", self)
        self.dock_console_widget = QTextEdit()
        self.dock_console.setWidget(self.dock_console_widget)
        self.addDockWidget(Qt.BottomDockWidgetArea, self.dock_console)

        # Dock Widget 2: Environment/History
        self.dock_env = QDockWidget("Environment/History", self)
        self.dock_env_widget = QListWidget()
        self.dock_env.setWidget(self.dock_env_widget)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_env)

        # Dock Widget 3: Files/Plots/Help/Viewer
        self.dock_files = QDockWidget("Files/Plots", self)
        self.dock_files_widget = QListWidget()
        self.dock_files.setWidget(self.dock_files_widget)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_files)

        # Creating a menu bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        view_menu = menubar.addMenu('View')

        # Adding actions to menus
        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
