# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ff2n.ui'
#
# Created: Wed Apr 08 07:09:43 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(239, 253)
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 210, 161, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 221, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(40, 20, 141, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 180, 161, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 70, 221, 80))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(50, 30, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.spinBox = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox.setGeometry(QtCore.QRect(130, 30, 42, 22))
        self.spinBox.setMaximum(10000)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton_3.setText(_translate("Form", "Start", None))
        self.groupBox.setTitle(_translate("Form", "DOE Name", None))
        self.lineEdit.setText(_translate("Form", "Full Factorial 2 n", None))
        self.pushButton_2.setText(_translate("Form", "Output Folder", None))
        self.groupBox_2.setTitle(_translate("Form", "Options", None))
        self.label.setText(_translate("Form", "Enter N", None))

