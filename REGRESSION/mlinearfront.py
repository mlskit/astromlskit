# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'multiplefront.ui'
#
# Created: Mon Apr 06 08:43:01 2015
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
        Form.resize(241, 193)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 201, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(40, 20, 141, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 80, 161, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 140, 161, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 110, 161, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "Regressior", None))
        self.lineEdit.setText(_translate("Form", "Multiple linear", None))
        self.pushButton.setText(_translate("Form", "X-File", None))
        self.pushButton_3.setText(_translate("Form", "Start", None))
        self.pushButton_2.setText(_translate("Form", "Y-File", None))

