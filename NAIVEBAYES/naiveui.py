# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nb.ui'
#
# Created: Sat Mar 14 15:23:20 2015
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
        Form.resize(250, 397)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 211, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(30, 20, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 80, 211, 80))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.comboBox = QtGui.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(20, 20, 161, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 350, 161, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 270, 161, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 310, 161, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 170, 211, 80))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.checkBox_5 = QtGui.QCheckBox(self.groupBox_3)
        self.checkBox_5.setGeometry(QtCore.QRect(30, 20, 151, 21))
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_3)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 0, 211, 80))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.checkBox_6 = QtGui.QCheckBox(self.groupBox_4)
        self.checkBox_6.setGeometry(QtCore.QRect(30, 20, 151, 21))
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.checkBox_7 = QtGui.QCheckBox(self.groupBox_4)
        self.checkBox_7.setGeometry(QtCore.QRect(30, 50, 151, 21))
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "Learner/classifier Name", None))
        self.lineEdit.setText(_translate("Form", "Naive Bayes", None))
        self.groupBox_2.setTitle(_translate("Form", "Variants", None))
        self.comboBox.setItemText(0, _translate("Form", "Gaussian", None))
        self.comboBox.setItemText(1, _translate("Form", "Multinomial", None))
        self.pushButton_3.setText(_translate("Form", "Start", None))
        self.pushButton.setText(_translate("Form", "Input File", None))
        self.pushButton_2.setText(_translate("Form", "Output Folder", None))
        self.groupBox_3.setTitle(_translate("Form", "Options", None))
        self.checkBox_5.setText(_translate("Form", " Predict Probaibilty (x)", None))
        self.groupBox_4.setTitle(_translate("Form", "Options", None))
        self.checkBox_6.setText(_translate("Form", " Predict Probaibilty (x)", None))
        self.checkBox_7.setText(_translate("Form", "Return Score", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Form()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
