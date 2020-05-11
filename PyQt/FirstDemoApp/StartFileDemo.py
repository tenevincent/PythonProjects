
import MainDialogView as dlg
from PyQt5 import QtCore, QtGui, QtWidgets






import sys
from PyQt5.QtGui import QIcon

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
ui = dlg.Ui_Dialog()



ui.setupUi(widget)
widget.setWindowIcon(QIcon('web.png'))  # Add icon icon, if there is no picture, there is no such sentence
widget.show()
sys.exit(app.exec_())

