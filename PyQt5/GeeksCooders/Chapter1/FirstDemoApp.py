from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy
import sys
from PyQt5.QtGui import QIcon
from PyQt5 import uic

from DialogView import DialogForm, display


class WindowExample(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400,300)
        self.setWindowTitle("Geekscoders.com")
        self.setWindowIcon(QIcon('images/app.png'))




        self.create_buttons()


        #self.setWindowOpacity(0.5)
        self.setStyleSheet('background-color:lightgreen')
        self.setVisible(True)

        # this is used for loading ui file
        uic.loadUi("dialog.ui", self)

        self.show()

    def create_buttons(self):

        layoutBox = QVBoxLayout(self)

        btn1 = QPushButton("Click Me",self)
        btn1.setGeometry(100, 100, 100, 100)
        btn1.setIcon(QIcon("images/app.png"))
        btn1.setStyleSheet('color:red')
        btn1.setStyleSheet('background-color:green')

        btn2 = QPushButton("Click Two", self)
        btn2.setGeometry(200,100, 100,100)
        btn2.setIcon(QIcon("images/copy.png"))
        btn2.setStyleSheet('color:yellow')
        btn2.setStyleSheet('background-color:purple')

        layoutBox.addWidget(btn1)
        layoutBox.addWidget(btn2)
        spacer = QSpacerItem(150, 10,  QSizePolicy.Expanding)
        layoutBox.addSpacerItem(spacer)
        self.setLayout(layoutBox)

        btn1.clicked.connect(self.clicked_btn)
        btn2.clicked.connect(self.second_clicked)




    def clicked_btn(self):
        print("Button One Clicked")
        display()
        #dialog.displayView()

    def second_clicked(self):
        print("Second Button Clicked")


app = QApplication(sys.argv)
window = WindowExample()
sys.exit(app.exec_())
