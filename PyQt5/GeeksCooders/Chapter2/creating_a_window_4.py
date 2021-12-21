import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")
        button.clicked.connect(self.show_printed)
        # Set the central widget of the Window.
        self.setCentralWidget(button)
        #self.setFixedSize(QSize(400, 300))

    def show_printed(self):
        print("The button has been clicked!")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
