# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ridgefront.ui'
#
# Created: Mon Apr 06 08:47:55 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from ridge import *

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

class Ui_Ridge(object):
    def setupUi(self, Ridge):
        Ridge.setObjectName(_fromUtf8("Ridge"))
        Ridge.resize(233, 299)
        self.pushButton_3 = QtGui.QPushButton(Ridge)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 240, 161, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.groupBox = QtGui.QGroupBox(Ridge)
        self.alpha=0.2
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 201, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(40, 20, 141, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton_2 = QtGui.QPushButton(Ridge)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 200, 161, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton = QtGui.QPushButton(Ridge)
        self.pushButton.setGeometry(QtCore.QRect(40, 160, 161, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.groupBox_2 = QtGui.QGroupBox(Ridge)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 90, 201, 51))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(30, 20, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.spinBox = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox.setGeometry(QtCore.QRect(120, 20, 42, 22))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.pushButton_3.clicked.connect(self.startridge)
        self.pushButton.clicked.connect(self.takeinput)
        self.pushButton_2.clicked.connect(self.takeoutput)
        self.spinBox.valueChanged.connect(self.setalpha)
        

        self.retranslateUi(Ridge)
        QtCore.QMetaObject.connectSlotsByName(Ridge)
    def setalpha(self):
        self.alpha=self.spinBox.value()

    def retranslateUi(self, Ridge):
        Ridge.setWindowTitle(_translate("Ridge", "Form", None))
        self.pushButton_3.setText(_translate("Ridge", "Start", None))
        self.groupBox.setTitle(_translate("Ridge", "Regressior", None))
        self.lineEdit.setText(_translate("Ridge", "Ridge Regression", None))
        self.pushButton_2.setText(_translate("Ridge", "Y-File", None))
        self.pushButton.setText(_translate("Ridge", "X-File", None))
        self.groupBox_2.setTitle(_translate("Ridge", "Options", None))
        self.label.setText(_translate("Ridge", "Alpha Parameter", None))
    def takeinput(self):
        self.fname1 = QtGui.QFileDialog.getOpenFileName(None, 'Open file', 'C:')
        self.xdata=[]
        for line in open(str(self.fname1)):
            row=line.split("\n")[0].split(",")
            self.xdata.append(row)
        
    def takeoutput(self):
        self.fname2 = QtGui.QFileDialog.getOpenFileName(None, 'Open file', 'C:')
        self.ydata=[]
        for line in open(str(self.fname2)):
            row=line.split("\n")[0].split(",")
            self.ydata.append(row)
        print self.ydata
        
    def startridge(self):
        import numpy as np
        X=np.array(self.xdata)
        Y=np.array(self.ydata)
        X=[[float(y) for y in x] for x in X]
        Y=[[float(y) for y in x] for x in Y]
        r = RidgeRegressor()
        print "fitting"
        r.fit(np.array(X), np.array(Y))
        #print r.predict(tX)
    



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Ridge()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

