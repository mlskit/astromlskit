# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'randomforest.ui'
#
# Created: Sun Mar 22 18:50:08 2015
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

class Ui_RandomForest(object):
    def setupUi(self, RandomForest):
        RandomForest.setObjectName(_fromUtf8("RandomForest"))
        RandomForest.resize(257, 442)
        self.groupBox = QtGui.QGroupBox(RandomForest)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 221, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(40, 20, 141, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.groupBox_2 = QtGui.QGroupBox(RandomForest)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 80, 211, 251))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(30, 20, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.spinBox = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox.setGeometry(QtCore.QRect(150, 20, 42, 22))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.spinBox_2 = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox_2.setGeometry(QtCore.QRect(150, 50, 42, 22))
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 111, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.comboBox_2 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 100, 161, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(60, 80, 111, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(60, 130, 111, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.comboBox_3 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_3.setGeometry(QtCore.QRect(20, 150, 161, 22))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(60, 180, 111, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.comboBox_4 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_4.setGeometry(QtCore.QRect(20, 200, 161, 22))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.pushButton = QtGui.QPushButton(RandomForest)
        self.pushButton.setGeometry(QtCore.QRect(40, 340, 161, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(RandomForest)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 380, 161, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(RandomForest)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 410, 161, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.retranslateUi(RandomForest)
        QtCore.QMetaObject.connectSlotsByName(RandomForest)

    def retranslateUi(self, RandomForest):
        RandomForest.setWindowTitle(_translate("RandomForest", "Form", None))
        self.groupBox.setTitle(_translate("RandomForest", "Learner/Classifier Name", None))
        self.lineEdit.setText(_translate("RandomForest", "Random Forest", None))
        self.groupBox_2.setTitle(_translate("RandomForest", "Options", None))
        self.label.setText(_translate("RandomForest", "Number of Trees", None))
        self.label_2.setText(_translate("RandomForest", "Sample ratio", None))
        self.comboBox_2.setItemText(0, _translate("RandomForest", "GROW_AUTO_INCREMENTAL", None))
        self.label_3.setText(_translate("RandomForest", "Grow Method", None))
        self.label_4.setText(_translate("RandomForest", "weighting_method", None))
        self.comboBox_3.setItemText(0, _translate("RandomForest", "mean_oob_mae_weight", None))
        self.comboBox_3.setItemText(1, _translate("RandomForest", "Forest.best_oob_mae_weight", None))
        self.label_5.setText(_translate("RandomForest", "Entropy metric", None))
        self.comboBox_4.setItemText(0, _translate("RandomForest", "ENTROPY1", None))
        self.comboBox_4.setItemText(1, _translate("RandomForest", "ENTROPY2", None))
        self.comboBox_4.setItemText(2, _translate("RandomForest", "ENTROPY3", None))
        self.pushButton.setText(_translate("RandomForest", "Train File", None))
        self.pushButton_2.setText(_translate("RandomForest", "Test File", None))
        self.pushButton_3.setText(_translate("RandomForest", "Start", None))

