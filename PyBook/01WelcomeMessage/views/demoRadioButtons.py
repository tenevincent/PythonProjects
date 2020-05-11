# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoRadioButtons.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(353, 167)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButtonFirstClass = QtWidgets.QRadioButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.radioButtonFirstClass.setFont(font)
        self.radioButtonFirstClass.setObjectName("radioButtonFirstClass")
        self.verticalLayout.addWidget(self.radioButtonFirstClass)
        self.radioButtonBusinessClass = QtWidgets.QRadioButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.radioButtonBusinessClass.setFont(font)
        self.radioButtonBusinessClass.setObjectName("radioButtonBusinessClass")
        self.verticalLayout.addWidget(self.radioButtonBusinessClass)
        self.radioButtonEconomyClass = QtWidgets.QRadioButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.radioButtonEconomyClass.setFont(font)
        self.radioButtonEconomyClass.setObjectName("radioButtonEconomyClass")
        self.verticalLayout.addWidget(self.radioButtonEconomyClass)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.labelStatusBar = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelStatusBar.setFont(font)
        self.labelStatusBar.setText("")
        self.labelStatusBar.setObjectName("labelStatusBar")
        self.verticalLayout_2.addWidget(self.labelStatusBar)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Choose the flight type"))
        self.radioButtonFirstClass.setText(_translate("Dialog", "First Class $150"))
        self.radioButtonBusinessClass.setText(_translate("Dialog", "Business Class $125"))
        self.radioButtonEconomyClass.setText(_translate("Dialog", "Economy Class $100"))
