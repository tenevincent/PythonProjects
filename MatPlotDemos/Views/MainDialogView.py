# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainDialogView.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.labelName = QtWidgets.QLabel(Dialog)
        self.labelName.setObjectName("labelName")
        self.gridLayout.addWidget(self.labelName, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 0, 2, 4, 1)
        self.labelVorname = QtWidgets.QLabel(Dialog)
        self.labelVorname.setObjectName("labelVorname")
        self.gridLayout.addWidget(self.labelVorname, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.labelDepartment = QtWidgets.QLabel(Dialog)
        self.labelDepartment.setObjectName("labelDepartment")
        self.gridLayout.addWidget(self.labelDepartment, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 3, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelName.setText(_translate("Dialog", "Name"))
        self.labelVorname.setText(_translate("Dialog", "Vorname"))
        self.labelDepartment.setText(_translate("Dialog", "Department"))
        self.label_4.setText(_translate("Dialog", "TextLabel"))


if __name__=="__main__":
    import sys
    from PyQt5.QtGui import QIcon
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(widget)
    widget.setWindowIcon(QIcon('web.png'))#Add icon icon, if there is no picture, there is no such sentence
    widget.show()
    sys.exit(app.exec_())