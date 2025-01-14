# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Programmer\Documents\Raffle 2\FRSettings.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingUI(object):
    def setupUi(self, SettingUI):
        SettingUI.setObjectName("SettingUI")
        SettingUI.setWindowModality(QtCore.Qt.ApplicationModal)
        SettingUI.resize(448, 254)
        SettingUI.setStyleSheet("*{\n"
"    \n"
"    color: black;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.pbClose = QtWidgets.QPushButton(SettingUI)
        self.pbClose.setGeometry(QtCore.QRect(190, 190, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pbClose.setFont(font)
        self.pbClose.setObjectName("pbClose")
        self.pbChange = QtWidgets.QPushButton(SettingUI)
        self.pbChange.setGeometry(QtCore.QRect(310, 190, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pbChange.setFont(font)
        self.pbChange.setObjectName("pbChange")
        self.RBReg = QtWidgets.QRadioButton(SettingUI)
        self.RBReg.setGeometry(QtCore.QRect(290, 20, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        self.RBReg.setFont(font)
        self.RBReg.setAutoFillBackground(False)
        self.RBReg.setObjectName("RBReg")
        self.RBIrr = QtWidgets.QRadioButton(SettingUI)
        self.RBIrr.setGeometry(QtCore.QRect(120, 20, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        self.RBIrr.setFont(font)
        self.RBIrr.setAutoFillBackground(False)
        self.RBIrr.setStyleSheet("")
        self.RBIrr.setObjectName("RBIrr")
        self.leQty = QtWidgets.QLineEdit(SettingUI)
        self.leQty.setEnabled(False)
        self.leQty.setGeometry(QtCore.QRect(140, 100, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.leQty.setFont(font)
        self.leQty.setInputMask("")
        self.leQty.setText("")
        self.leQty.setObjectName("leQty")
        self.lblIQ = QtWidgets.QLabel(SettingUI)
        self.lblIQ.setGeometry(QtCore.QRect(20, 100, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblIQ.setFont(font)
        self.lblIQ.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblIQ.setObjectName("lblIQ")
        self.comboChoice = QtWidgets.QComboBox(SettingUI)
        self.comboChoice.setEnabled(False)
        self.comboChoice.setGeometry(QtCore.QRect(140, 60, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.comboChoice.setFont(font)
        self.comboChoice.setStyleSheet("color: rgb(0, 0, 0);")
        self.comboChoice.setEditable(False)
        self.comboChoice.setFrame(True)
        self.comboChoice.setObjectName("comboChoice")
        self.lblIN = QtWidgets.QLabel(SettingUI)
        self.lblIN.setGeometry(QtCore.QRect(20, 60, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblIN.setFont(font)
        self.lblIN.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblIN.setObjectName("lblIN")
        self.leSpecify = QtWidgets.QLineEdit(SettingUI)
        self.leSpecify.setEnabled(False)
        self.leSpecify.setGeometry(QtCore.QRect(140, 140, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.leSpecify.setFont(font)
        self.leSpecify.setInputMask("")
        self.leSpecify.setText("")
        self.leSpecify.setObjectName("leSpecify")
        self.lblSpecify = QtWidgets.QLabel(SettingUI)
        self.lblSpecify.setEnabled(True)
        self.lblSpecify.setGeometry(QtCore.QRect(20, 140, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblSpecify.setFont(font)
        self.lblSpecify.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblSpecify.setObjectName("lblSpecify")

        self.retranslateUi(SettingUI)
        QtCore.QMetaObject.connectSlotsByName(SettingUI)

    def retranslateUi(self, SettingUI):
        _translate = QtCore.QCoreApplication.translate
        SettingUI.setWindowTitle(_translate("SettingUI", "Dialog"))
        self.pbClose.setText(_translate("SettingUI", "Cancel"))
        self.pbChange.setText(_translate("SettingUI", "Set Details"))
        self.RBReg.setText(_translate("SettingUI", "REGULAR"))
        self.RBIrr.setText(_translate("SettingUI", "NON-REGULAR"))
        self.leQty.setPlaceholderText(_translate("SettingUI", "Input Item Quantity"))
        self.lblIQ.setText(_translate("SettingUI", "Item Qty:"))
        self.comboChoice.setPlaceholderText(_translate("SettingUI", "Select Item to Raffle"))
        self.lblIN.setText(_translate("SettingUI", "Item Name:"))
        self.leSpecify.setPlaceholderText(_translate("SettingUI", "Input Item Name"))
        self.lblSpecify.setText(_translate("SettingUI", "Specify:"))