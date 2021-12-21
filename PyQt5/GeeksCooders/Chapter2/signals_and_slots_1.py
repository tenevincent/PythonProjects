from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton  # <1>
from PyQt5.QtCore import Qt

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # <2>

        self.setWindowTitle("My App")

        btnPress = QPushButton("Press Me!")
        btnPress.setCheckable(True)
        btnPress.clicked.connect(self.the_button_was_clicked)

        # Set the central widget of the Window.
        self.setCentralWidget(btnPress)

    def the_button_was_clicked(self):
        print("Clicked!")


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()

