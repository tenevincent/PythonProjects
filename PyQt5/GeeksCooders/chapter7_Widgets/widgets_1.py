import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel("Hello")
        font = label.font()  # <1>
        font.setPointSize(30)
        label.setFont(font)
        label.setPixmap(QPixmap("otje.jpg"))
        label.setScaledContents(True)

        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # <2>

        self.setCentralWidget(label)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
