from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import uic
import sys


class UI(QWidget):
    def __init__(self):
        super().__init__()

        #this is used for loading ui file
        uic.loadUi("dialog.ui", self)
        # find our widgets
        okBtn = self.findChild(QPushButton, 'btnAccept')
        okBtn.clicked.connect(self.ok_btn)

        # find our widgets
        btnCancel = self.findChild(QPushButton, 'btnCancel')
        btnCancel.clicked.connect(self.cancel_btn)


    def ok_btn(self):
        print("Accept Button Clicked")

    def cancel_btn(self):
        print("Cancel Button Clicked")


app = QApplication([])
window = UI()
window.show()
app.exec_()
