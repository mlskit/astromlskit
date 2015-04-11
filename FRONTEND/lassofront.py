# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lassoui.ui'
#
# Created: Sat Apr 11 09:14:27 2015
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
        Form.resize(235, 342)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 211, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(40, 20, 141, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 70, 211, 171))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(50, 20, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox.setGeometry(QtCore.QRect(110, 20, 62, 22))
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 111, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.spinBox = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox.setGeometry(QtCore.QRect(110, 60, 61, 22))
        self.spinBox.setMaximum(10000000)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.checkBox = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(30, 90, 81, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_2.setGeometry(QtCore.QRect(120, 90, 121, 17))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_3 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 120, 81, 17))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 280, 161, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 250, 161, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "Regressor Name", None))
        self.lineEdit.setText(_translate("Form", "LASSO(L1)", None))
        self.groupBox_2.setTitle(_translate("Form", "Options", None))
        self.label.setText(_translate("Form", "Alpha", None))
        self.label_2.setText(_translate("Form", "Max iterations", None))
        self.checkBox.setText(_translate("Form", "  Normalise", None))
        self.checkBox_2.setText(_translate("Form", "Positive", None))
        self.checkBox_3.setText(_translate("Form", "Fit intercept", None))
        self.pushButton_3.setText(_translate("Form", "Start", None))
        self.pushButton.setText(_translate("Form", "Input File", None))

