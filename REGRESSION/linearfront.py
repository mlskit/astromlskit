# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'linearfront.ui'
#
# Created: Mon Apr 06 08:37:32 2015
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

class Ui_SimpleLinear(object):
    def setupUi(self, SimpleLinear):
        SimpleLinear.setObjectName(_fromUtf8("SimpleLinear"))
        SimpleLinear.resize(211, 184)
        self.groupBox = QtGui.QGroupBox(SimpleLinear)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 221, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(40, 20, 141, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton_3 = QtGui.QPushButton(SimpleLinear)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 140, 161, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_2 = QtGui.QPushButton(SimpleLinear)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 110, 161, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton = QtGui.QPushButton(SimpleLinear)
        self.pushButton.setGeometry(QtCore.QRect(30, 80, 161, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(SimpleLinear)
        QtCore.QMetaObject.connectSlotsByName(SimpleLinear)

    def retranslateUi(self, SimpleLinear):
        SimpleLinear.setWindowTitle(_translate("SimpleLinear", "Form", None))
        self.groupBox.setTitle(_translate("SimpleLinear", "Regressior", None))
        self.lineEdit.setText(_translate("SimpleLinear", "Simple Linear", None))
        self.pushButton_3.setText(_translate("SimpleLinear", "Start", None))
        self.pushButton_2.setText(_translate("SimpleLinear", "Y-File", None))
        self.pushButton.setText(_translate("SimpleLinear", "X-File", None))

