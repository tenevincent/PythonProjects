# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CheckBoxDemoApp.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class CheckBoxAppDemo(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(521, 370)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setCheckable(True)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.groupBox)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBoxChoclateAlmond = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBoxChoclateAlmond.setObjectName("checkBoxChoclateAlmond")
        self.verticalLayout_3.addWidget(self.checkBoxChoclateAlmond)
        self.checkBoxRockyRoad = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBoxRockyRoad.setObjectName("checkBoxRockyRoad")
        self.verticalLayout_3.addWidget(self.checkBoxRockyRoad)
        self.checkBoxCookieDough = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBoxCookieDough.setObjectName("checkBoxCookieDough")
        self.verticalLayout_3.addWidget(self.checkBoxCookieDough)
        self.checkBoxChoclateChips = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBoxChoclateChips.setObjectName("checkBoxChoclateChips")
        self.verticalLayout_3.addWidget(self.checkBoxChoclateChips)
        self.verticalLayout_2.addWidget(self.splitter)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setCheckable(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBoxCoffee = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBoxCoffee.setObjectName("checkBoxCoffee")
        self.verticalLayout.addWidget(self.checkBoxCoffee)
        self.checkBoxSoda = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBoxSoda.setObjectName("checkBoxSoda")
        self.verticalLayout.addWidget(self.checkBoxSoda)
        self.checkBoxTea = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBoxTea.setObjectName("checkBoxTea")
        self.verticalLayout.addWidget(self.checkBoxTea)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.labelAmount = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelAmount.setFont(font)
        self.labelAmount.setObjectName("labelAmount")
        self.verticalLayout_4.addWidget(self.labelAmount)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Menu"))
        self.groupBox.setTitle(_translate("Dialog", "Ice Creams"))
        self.checkBoxChoclateAlmond.setText(_translate("Dialog", "Chocolate Almond $3"))
        self.checkBoxRockyRoad.setText(_translate("Dialog", "Rocky Road $5"))
        self.checkBoxCookieDough.setText(_translate("Dialog", "Cookie Dough $2"))
        self.checkBoxChoclateChips.setText(_translate("Dialog", "Mint Chocolate Chips $ 4"))
        self.groupBox_2.setTitle(_translate("Dialog", "Drinks"))
        self.checkBoxCoffee.setText(_translate("Dialog", "Coffee $2"))
        self.checkBoxSoda.setText(_translate("Dialog", "Soda $ 3"))
        self.checkBoxTea.setText(_translate("Dialog", "Tea $ 1"))
        self.labelAmount.setText(_translate("Dialog", "Menu"))
