# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anova.ui'
#
# Created: Sat Apr 11 09:33:51 2015
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
        Form.resize(238, 435)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 221, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(40, 20, 141, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 80, 221, 231))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 161, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox.setGeometry(QtCore.QRect(120, 50, 62, 22))
        self.doubleSpinBox.setMaximum(999999.99)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(50, 50, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.comboBox = QtGui.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(110, 80, 69, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.comboBox_2 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_2.setGeometry(QtCore.QRect(110, 120, 69, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(40, 160, 46, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.comboBox_3 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_3.setGeometry(QtCore.QRect(110, 160, 69, 22))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.checkBox = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(50, 190, 131, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 320, 161, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 360, 161, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "Statistical estimator", None))
        self.lineEdit.setText(_translate("Form", "ANOVA", None))
        self.groupBox_2.setTitle(_translate("Form", "Options", None))
        self.pushButton.setText(_translate("Form", "Model equation file", None))
        self.label.setText(_translate("Form", "Scale", None))
        self.comboBox.setItemText(0, _translate("Form", "F", None))
        self.comboBox.setItemText(1, _translate("Form", "Cp", None))
        self.comboBox.setItemText(2, _translate("Form", "ChiSq", None))
        self.label_2.setText(_translate("Form", "Test", None))
        self.label_3.setText(_translate("Form", "Type", None))
        self.comboBox_2.setItemText(0, _translate("Form", "1", None))
        self.comboBox_2.setItemText(1, _translate("Form", "2", None))
        self.comboBox_2.setItemText(2, _translate("Form", "3", None))
        self.label_4.setText(_translate("Form", "Robust", None))
        self.comboBox_3.setItemText(0, _translate("Form", "Noene", None))
        self.comboBox_3.setItemText(1, _translate("Form", "hc0", None))
        self.comboBox_3.setItemText(2, _translate("Form", "hc1", None))
        self.comboBox_3.setItemText(3, _translate("Form", "hc2", None))
        self.comboBox_3.setItemText(4, _translate("Form", "hc3", None))
        self.checkBox.setText(_translate("Form", "                print to a file", None))
        self.pushButton_2.setText(_translate("Form", "Input File", None))
        self.pushButton_3.setText(_translate("Form", "Start", None))

