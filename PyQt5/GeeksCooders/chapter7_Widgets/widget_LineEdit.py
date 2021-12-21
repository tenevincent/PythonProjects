import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        lineEdit = QLineEdit()
        lineEdit.setMaxLength(10)
        lineEdit.setPlaceholderText("Enter your text")

        # widget.setReadOnly(True) # uncomment this to make readonly

        lineEdit.returnPressed.connect(self.return_pressed)
        lineEdit.selectionChanged.connect(self.selection_changed)
        lineEdit.textChanged.connect(self.text_changed)
        lineEdit.textEdited.connect(self.text_edited)
        lineEdit.setInputMask('000.000.000.000;_')



        self.setCentralWidget(lineEdit)

    def return_pressed(self):
        print("Return pressed!")
        self.centralWidget().setText("BOOM!")

    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())

    def text_changed(self, s):
        print("Text changed...")
        print(s)

    def text_edited(self, s):
        print("Text edited...")
        print(s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
