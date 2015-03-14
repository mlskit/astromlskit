# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'knn.ui'
#
# Created: Fri Mar 06 08:18:19 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from kNN import *
from DM import *

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
        Form.resize(240, 320)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 221, 51))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))

        self.textEdit = QtGui.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 201, 21))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 60, 221, 80))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))

        self.spinBox = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox.setGeometry(QtCore.QRect(160, 20, 42, 31))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.spinBox.valueChanged.connect(self.setk)

        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(20, 25, 111, 21))
        self.label.setObjectName(_fromUtf8("label"))

        self.checkBox = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(20, 60, 181, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))

        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 150, 221, 121))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))

        self.comboBox = QtGui.QComboBox(self.groupBox_3)
        self.comboBox.setGeometry(QtCore.QRect(20, 20, 181, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem("manhattan")
        self.comboBox.addItem("euclidean")
        self.comboBox.addItem("minkowski")
        self.comboBox.activated[str].connect(self.onActivated)
        

        self.checkBox_2 = QtGui.QCheckBox(self.groupBox_3)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 60, 181, 17))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))

        self.checkBox_3 = QtGui.QCheckBox(self.groupBox_3)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 90, 201, 17))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))

        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(34, 280, 171, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.startknn)

        

        self.fileDialog = QtGui.QFileDialog(Form)
        self.fileDialog.show()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def onActivated(self,text):
        if text=="manhattan":
            self.dm=cityblock_distance
        elif text=="euclidean":
            self.dm=euclidean_distance
        else:
            self.dm=minkowski_distance

        #print self.dm

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "Learner/Classifier Name", None))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">kNN</span></p></body></html>", None))
        self.groupBox_2.setTitle(_translate("Form", "Neighbors", None))
        self.label.setText(_translate("Form", "Number of neighbors", None))
        self.checkBox.setText(_translate("Form", "Weighting by ranks,not distances", None))
        self.groupBox_3.setTitle(_translate("Form", "GroupBox", None))
       
        self.checkBox_2.setText(_translate("Form", "Normalize continous attributes", None))
        self.checkBox_3.setText(_translate("Form", "ignore unknown values", None))
        self.pushButton.setText(_translate("Form", "Apply", None))

    def setk(self):
        self.k=self.spinBox.value()
        print self.k

    def startknn(self):
        a=train([[1,2],[2,3]],[0,1],self.k)
        print self.k
        print classify(a,[2,5],distance_fn=self.dm)

        

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Form()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
