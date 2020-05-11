# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GroupedRadioButtons.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class GroupedRadioButtons(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(549, 410)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButtonMedium = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonMedium.setObjectName("radioButtonMedium")
        self.verticalLayout_2.addWidget(self.radioButtonMedium)
        self.radioButtonLarge = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonLarge.setObjectName("radioButtonLarge")
        self.verticalLayout_2.addWidget(self.radioButtonLarge)
        self.radioButtonXL = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonXL.setObjectName("radioButtonXL")
        self.verticalLayout_2.addWidget(self.radioButtonXL)
        self.radioButtonXXL = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonXXL.setObjectName("radioButtonXXL")
        self.verticalLayout_2.addWidget(self.radioButtonXXL)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButtonDebitCard = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButtonDebitCard.setObjectName("radioButtonDebitCard")
        self.verticalLayout.addWidget(self.radioButtonDebitCard)
        self.radioButtonNetBanking = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButtonNetBanking.setObjectName("radioButtonNetBanking")
        self.verticalLayout.addWidget(self.radioButtonNetBanking)
        self.radioButtonCashOnDelivery = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButtonCashOnDelivery.setObjectName("radioButtonCashOnDelivery")
        self.verticalLayout.addWidget(self.radioButtonCashOnDelivery)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_3.addWidget(self.buttonBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.labelSelected = QtWidgets.QLabel(Dialog)
        self.labelSelected.setObjectName("labelSelected")
        self.verticalLayout_4.addWidget(self.labelSelected)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Choose your Shirt Size"))
        self.radioButtonMedium.setText(_translate("Dialog", "M"))
        self.radioButtonLarge.setText(_translate("Dialog", "L"))
        self.radioButtonXL.setText(_translate("Dialog", "XL"))
        self.radioButtonXXL.setText(_translate("Dialog", "XXL"))
        self.groupBox_2.setTitle(_translate("Dialog", "Choose your payment method"))
        self.radioButtonDebitCard.setText(_translate("Dialog", "Debit/Credit Card"))
        self.radioButtonNetBanking.setText(_translate("Dialog", "Net Banking"))
        self.radioButtonCashOnDelivery.setText(_translate("Dialog", "Cash on Delivery"))
        self.labelSelected.setText(_translate("Dialog", "TextLabel"))
