# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ann.ui'
#
# Created: Mon Apr 06 14:13:07 2015
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

class Ui_ANN(object):
    def setupUi(self, ANN):
        ANN.setObjectName(_fromUtf8("ANN"))
        ANN.resize(240, 379)
        self.groupBox = QtGui.QGroupBox(ANN)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 221, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(40, 20, 141, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.groupBox_2 = QtGui.QGroupBox(ANN)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 80, 221, 171))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(30, 20, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.spinBox = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox.setGeometry(QtCore.QRect(150, 20, 42, 22))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 111, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox.setGeometry(QtCore.QRect(150, 50, 62, 22))
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.spinBox_2 = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox_2.setGeometry(QtCore.QRect(150, 80, 42, 22))
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 111, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(30, 110, 111, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.spinBox_3 = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox_3.setGeometry(QtCore.QRect(150, 110, 42, 22))
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.spinBox_4 = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox_4.setGeometry(QtCore.QRect(150, 140, 42, 22))
        self.spinBox_4.setObjectName(_fromUtf8("spinBox_4"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(30, 140, 111, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pushButton_3 = QtGui.QPushButton(ANN)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 330, 161, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_2 = QtGui.QPushButton(ANN)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 300, 161, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton = QtGui.QPushButton(ANN)
        self.pushButton.setGeometry(QtCore.QRect(30, 270, 161, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(ANN)
        QtCore.QMetaObject.connectSlotsByName(ANN)

    def retranslateUi(self, ANN):
        ANN.setWindowTitle(_translate("ANN", "Form", None))
        self.groupBox.setTitle(_translate("ANN", "Learner/Classifier Name", None))
        self.lineEdit.setText(_translate("ANN", "Multilayer perceptron", None))
        self.groupBox_2.setTitle(_translate("ANN", "Options", None))
        self.label.setText(_translate("ANN", "Number of inputs", None))
        self.label_2.setText(_translate("ANN", "Input range positive", None))
        self.label_3.setText(_translate("ANN", "Hidden layer neurons", None))
        self.label_4.setText(_translate("ANN", "output layer neurons", None))
        self.label_5.setText(_translate("ANN", "Epoch", None))
        self.pushButton_3.setText(_translate("ANN", "Start", None))
        self.pushButton_2.setText(_translate("ANN", "Test File", None))
        self.pushButton.setText(_translate("ANN", "Train File", None))

