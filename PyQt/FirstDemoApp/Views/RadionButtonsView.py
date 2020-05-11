# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RadionButtonsView.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class RadioButtonsDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(405, 300)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButtonSecondClass = QtWidgets.QRadioButton(self.widget)
        self.radioButtonSecondClass.setObjectName("radioButtonSecondClass")
        self.verticalLayout.addWidget(self.radioButtonSecondClass)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.radioButtonFirstClass = QtWidgets.QRadioButton(self.widget)
        self.radioButtonFirstClass.setObjectName("radioButtonFirstClass")
        self.verticalLayout.addWidget(self.radioButtonFirstClass)
        self.labelFare = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelFare.setFont(font)
        self.labelFare.setObjectName("labelFare")
        self.verticalLayout.addWidget(self.labelFare)
        self.radioButtonThirdClass = QtWidgets.QRadioButton(self.widget)
        self.radioButtonThirdClass.setObjectName("radioButtonThirdClass")
        self.verticalLayout.addWidget(self.radioButtonThirdClass)
        self.horizontalLayout.addWidget(self.splitter)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        #self.buttonBox.accepted.connect(Dialog.accept)
        #self.buttonBox.rejected.connect(Dialog.reject)
        #QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.radioButtonSecondClass.setText(_translate("Dialog", "First Class $125"))
        self.label.setText(_translate("Dialog", "Choose the figure type"))
        self.radioButtonFirstClass.setText(_translate("Dialog", "First Class $150"))
        self.labelFare.setText(_translate("Dialog", "TextLabel"))
        self.radioButtonThirdClass.setText(_translate("Dialog", "First Class $100"))
