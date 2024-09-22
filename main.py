import sys
import openai
from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget, QTextEdit, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self, openai_key):
        super().__init__()
        self.setWindowTitle('Brainstorm with AI')
        self.setGeometry(100, 100, 1200, 800)
        self.openai_key = openai_key
        openai.api_key = self.openai_key  # Set the API key for the OpenAI client
        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.central_layout = QVBoxLayout()
        self.chat_box = QTextEdit()
        self.generate_flow_button = QPushButton('Generate Code Flow')
        self.generate_flow_button.clicked.connect(self.generate_flow_with_openai)
        self.central_layout.addWidget(self.chat_box)
        self.central_layout.addWidget(self.generate_flow_button)
        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)
        self.initialize_other_widgets()

    def initialize_other_widgets(self):
        self.dock_flow = QDockWidget("Code Flow", self)
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

        self.dock_code = QDockWidget("Generated Code", self)
        self.dock_code_widget = QTextEdit()
        self.dock_code.setWidget(self.dock_code_widget)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_code)

        self.dock_placeholder = QDockWidget("Additional Tools", self)
        self.dock_placeholder_widget = QLabel("Future functionalities can be added here.")
        self.dock_placeholder.setWidget(self.dock_placeholder_widget)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_placeholder)

    def generate_flow_with_openai(self):
        task_description = self.chat_box.toPlainText()
        prompt = f"Write a detailed pseudocode algorithm to accomplish the following task: {task_description}"
        try:
            response = openai.Completion.create(
                model="code-davinci-002",
                prompt=prompt,
                max_tokens=150,
                temperature=0.7
            )
            algorithm = response.choices[0].text.strip() if response.choices else "No algorithm could be generated."
            self.flow_text_edit.setText(algorithm)
        except Exception as e:
            print(f"An error occurred: {e}")

    def generate_code(self):
        code = "Generated code from the flow:\n\n" + self.flow_text_edit.toPlainText()
        self.dock_code_widget.setText(code)

def main():
    app = QApplication(sys.argv)
    openai_key = "your_openai_api_key_here"  # Ensure to replace with your actual API key
    main_window = MainWindow(openai_key)
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
