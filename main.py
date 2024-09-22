import sys
import openai
from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget, QTextEdit, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import Qt  # Import Qt for alignment and widget properties

class MainWindow(QMainWindow):
    def __init__(self, openai_key):
        super().__init__()
        self.setWindowTitle('Engineering Workflow Application with OpenAI')
        self.setGeometry(100, 100, 1200, 800)
        self.openai_key = openai_key
        self.initUI()

    def initUI(self):
        # Central Widget: Chat Box for discussion and generating flow
        self.central_widget = QWidget()
        self.central_layout = QVBoxLayout()
        self.chat_box = QTextEdit()
        self.generate_flow_button = QPushButton('Generate Flow with OpenAI')
        self.generate_flow_button.clicked.connect(self.generate_flow_with_openai)
        self.central_layout.addWidget(self.chat_box)
        self.central_layout.addWidget(self.generate_flow_button)
        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)

        # Initialize other widgets as before
        self.initialize_other_widgets()

    def initialize_other_widgets(self):
        # Dock Widget 1: Display and edit the logic flow
        self.dock_flow = QDockWidget("Algorithm Flow", self)
        self.dock_flow_widget = QWidget()
        self.dock_flow_layout = QVBoxLayout()
        self.flow_text_edit = QTextEdit()
        self.generate_code_button = QPushButton('Generate Code')
        self.generate_code_button.clicked.connect(self.generate_code)
        self.dock_flow_layout.addWidget(self.flow_text_edit)
        self.dock_flow_layout.addWidget(self.generate_code_button)
        self.dock_flow_widget.setLayout(self.dock_flow_layout)
        self.dock_flow.setWidget(self.dock_flow_widget)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_flow)
        
        # Initialize Dock Widget 2 and 3 as before
        self.init_dock_widget_2_and_3()

    def init_dock_widget_2_and_3(self):
        self.dock_code = QDockWidget("Generated Code", self)
        self.dock_code_widget = QTextEdit()
        self.dock_code.setWidget(self.dock_code_widget)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_code)
        
        self.dock_placeholder = QDockWidget("Additional Tools", self)
        self.dock_placeholder_widget = QLabel("Future functionalities can be added here.")
        self.dock_placeholder.setWidget(self.dock_placeholder_widget)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_placeholder)

    def generate_flow_with_openai(self):
        prompt = self.chat_box.toPlainText()
        response = openai.Completion.create(
            engine="davinci-codex",
            prompt=prompt,
            max_tokens=150,
            api_key=self.openai_key
        )
        self.flow_text_edit.setText(response.choices[0].text.strip())

    def generate_code(self):
        code = "Generated code from the flow:\n\n" + self.flow_text_edit.toPlainText()
        self.dock_code_widget.setText(code)

def main():
    app = QApplication(sys.argv)
    # Insert your OpenAI API Key here
    openai_key = "sk-BJZLFlNC4is10LTrNflQjLZd-8oXdR1vR07gCxcaNcT3BlbkFJWicqXw4iH3d_C3lGXPXAAK3JoxWqrMyxlkY4W2KmQA"
    main_window = MainWindow(openai_key)
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
