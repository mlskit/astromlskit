# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'svmui.ui'
#
# Created: Sun Mar 22 21:45:22 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from sklearn import svm
import numpy as np
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
        Form.resize(253, 569)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 221, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))

        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(40, 20, 141, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.groupBox_4 = QtGui.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 70, 231, 381))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))

        self.label_2 = QtGui.QLabel(self.groupBox_4)
        self.label_2.setGeometry(QtCore.QRect(60, 20, 81, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.spinBox_2 = QtGui.QSpinBox(self.groupBox_4)
        self.spinBox_2.setGeometry(QtCore.QRect(150, 20, 42, 22))
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))

        self.label_3 = QtGui.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(60, 50, 81, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.spinBox_3 = QtGui.QSpinBox(self.groupBox_4)
        self.spinBox_3.setGeometry(QtCore.QRect(150, 50, 42, 22))
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))

        self.label_4 = QtGui.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(60, 70, 81, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.spinBox_4 = QtGui.QSpinBox(self.groupBox_4)
        self.spinBox_4.setGeometry(QtCore.QRect(150, 70, 42, 22))
        self.spinBox_4.setObjectName(_fromUtf8("spinBox_4"))

        self.label_5 = QtGui.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(60, 100, 81, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.spinBox_5 = QtGui.QSpinBox(self.groupBox_4)
        self.spinBox_5.setGeometry(QtCore.QRect(150, 100, 42, 22))
        self.spinBox_5.setObjectName(_fromUtf8("spinBox_5"))

        self.label_6 = QtGui.QLabel(self.groupBox_4)
        self.label_6.setGeometry(QtCore.QRect(60, 130, 81, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.spinBox_6 = QtGui.QSpinBox(self.groupBox_4)
        self.spinBox_6.setGeometry(QtCore.QRect(150, 130, 42, 22))
        self.spinBox_6.setObjectName(_fromUtf8("spinBox_6"))

        self.label_7 = QtGui.QLabel(self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(60, 160, 81, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))

        self.spinBox_7 = QtGui.QSpinBox(self.groupBox_4)
        self.spinBox_7.setGeometry(QtCore.QRect(150, 160, 42, 22))
        self.spinBox_7.setObjectName(_fromUtf8("spinBox_7"))

        self.label_8 = QtGui.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(60, 190, 81, 20))
        self.label_8.setObjectName(_fromUtf8("label_8"))

        self.label_9 = QtGui.QLabel(self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(60, 220, 81, 20))
        self.label_9.setObjectName(_fromUtf8("label_9"))

        self.spinBox_9 = QtGui.QSpinBox(self.groupBox_4)
        self.spinBox_9.setGeometry(QtCore.QRect(150, 220, 42, 22))
        self.spinBox_9.setObjectName(_fromUtf8("spinBox_9"))

        self.spinBox_10 = QtGui.QSpinBox(self.groupBox_4)
        self.spinBox_10.setGeometry(QtCore.QRect(150, 250, 42, 22))
        self.spinBox_10.setObjectName(_fromUtf8("spinBox_10"))

        self.label_10 = QtGui.QLabel(self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(60, 250, 81, 20))
        self.label_10.setObjectName(_fromUtf8("label_10"))

        self.spinBox_11 = QtGui.QSpinBox(self.groupBox_4)
        self.spinBox_11.setGeometry(QtCore.QRect(150, 280, 42, 22))
        self.spinBox_11.setObjectName(_fromUtf8("spinBox_11"))

        self.label_11 = QtGui.QLabel(self.groupBox_4)
        self.label_11.setGeometry(QtCore.QRect(60, 280, 81, 20))
        self.label_11.setObjectName(_fromUtf8("label_11"))

        self.checkBox_6 = QtGui.QCheckBox(self.groupBox_4)
        self.checkBox_6.setGeometry(QtCore.QRect(60, 340, 181, 17))
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))

        self.checkBox_7 = QtGui.QCheckBox(self.groupBox_4)
        self.checkBox_7.setGeometry(QtCore.QRect(60, 310, 181, 17))
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))

        self.comboBox = QtGui.QComboBox(self.groupBox_4)
        self.comboBox.setGeometry(QtCore.QRect(150, 190, 69, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))

        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 470, 161, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.takeinput)

        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 530, 161, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(self.startsvm)

        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 500, 161, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.taketest)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def startsvm(self):
        clf=svm.SVC()
        clf.fit(self.tr,self.classlabels)
        for i in self.te:
            print "test record:",i,"classlabel:",clf.predict(i)
            
    def takeinput(self):
        fname = QtGui.QFileDialog.getOpenFileName(None, 'Open file', 'C:')
        print type(fname)
        import pandas as pd
        df = pd.read_csv(str(fname), sep=",")
        x=list(df[list(df)[0]])
        y=list(df[list(df)[1]])
        self.classlabels=list(df[list(df)[2]])
        print self.classlabels
        self.tr=(zip(x,y))

    def taketest(self):
        fname = QtGui.QFileDialog.getOpenFileName(None, 'Open file', 'C:')
        print type(fname)
        import pandas as pd
        df = pd.read_csv(str(fname), sep=",")
        x=list(df[list(df)[0]])
        y=list(df[list(df)[1]])
        #print x,y
        self.te=(zip(x,y))
        #print (self.te)
        #print len(np.array(self.te).shape)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "Learner/Classifier Name", None))
        self.lineEdit.setText(_translate("Form", "Support vector machines", None))
        self.groupBox_4.setTitle(_translate("Form", "parameters", None))
        self.label_2.setText(_translate("Form", "C", None))
        self.label_3.setText(_translate("Form", "cache_size", None))
        self.label_4.setText(_translate("Form", "class_weight", None))
        self.label_5.setText(_translate("Form", "coeff0", None))
        self.label_6.setText(_translate("Form", "degree", None))
        self.label_7.setText(_translate("Form", "gamma", None))
        self.label_8.setText(_translate("Form", "kernel", None))
        self.label_9.setText(_translate("Form", "probability", None))
        self.label_10.setText(_translate("Form", "tol", None))
        self.label_11.setText(_translate("Form", "randomstate", None))
        self.checkBox_6.setText(_translate("Form", "verbose", None))
        self.checkBox_7.setText(_translate("Form", "shrinking", None))
        self.comboBox.setItemText(0, _translate("Form", "rbf", None))
        self.comboBox.setItemText(1, _translate("Form", "linear", None))
        self.pushButton.setText(_translate("Form", "Train File", None))
        self.pushButton_3.setText(_translate("Form", "Start", None))
        self.pushButton_2.setText(_translate("Form", "Test file", None))

