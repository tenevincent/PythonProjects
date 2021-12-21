import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QSpinBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        spinBox = QSpinBox()
        # Or: widget = QDoubleSpinBox()

        spinBox.setMinimum(-10)
        spinBox.setMaximum(20)
        # Or: widget.setRange(-10,3)

        spinBox.setPrefix("$")
        spinBox.setSuffix("c")
        spinBox.setSingleStep(1)  # Or e.g. 0.5 for QDoubleSpinBox
        spinBox.valueChanged.connect(self.value_changed)
        spinBox.valueChanged[str].connect(self.value_changed_str)

        self.setCentralWidget(spinBox)

    def value_changed(self, i):
        print(i)

    def value_changed_str(self, s):
        print(s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
