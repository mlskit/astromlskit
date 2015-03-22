# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kmeansui.ui'
#
# Created: Sun Mar 15 17:55:09 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from DM import *
from kmeans import *
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
        Form.resize(250, 360)
        self.dm=euclidean_distance
        #setting k and number of trails
        self.k=1
        self.notr=1
        self.fname="waste.txt"
        
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 221, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))

        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(40, 20, 141, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 80, 221, 61))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))

        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(30, 20, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.spinBox = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox.setGeometry(QtCore.QRect(150, 20, 42, 22))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.spinBox.valueChanged.connect(self.setk)

        self.groupBox_4 = QtGui.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 150, 221, 111))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))

        self.comboBox_2 = QtGui.QComboBox(self.groupBox_4)
        self.comboBox_2.setGeometry(QtCore.QRect(30, 20, 161, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.activated[str].connect(self.getdis)

        self.checkBox_3 = QtGui.QCheckBox(self.groupBox_4)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 50, 151, 17))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))

        self.label_2 = QtGui.QLabel(self.groupBox_4)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 111, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.spinBox_2 = QtGui.QSpinBox(self.groupBox_4)
        self.spinBox_2.setGeometry(QtCore.QRect(150, 70, 42, 22))
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.spinBox_2.valueChanged.connect(self.settrails)
        
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 320, 161, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(self.startkmn)

        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 280, 161, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.takeinput)

##        self.spinBox_3 = QtGui.QSpinBox(Form)
##        self.spinBox_3.setGeometry(QtCore.QRect(40, 310, 161, 23))
##        self.spinBox_3.setObjectName(_fromUtf8("spinBox_2"))
##        self.spinBox_3.valueChanged.connect(self.settrails)
        

##        self.pushButton_2 = QtGui.QPushButton(Form)
##        self.pushButton_2.setGeometry(QtCore.QRect(40, 310, 161, 23))
##        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
##        self.pushButton_2.clicked.connect(self.takeoutput)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def takeinput(self):
        self.fname = QtGui.QFileDialog.getOpenFileName(None, 'Open file', 'C:')
        print type(self.fname)
        
    def setk(self):
        self.k=self.spinBox.value()
        print self.k

    def settrails(self):
        self.notr=self.spinBox_2.value()
        print self.notr

    def takeoutput(self):
        return
        fname = QtGui.QFileDialog.getOpenFileName(None, 'Open file', 'C:')
        print type(fname)
        import pandas as pd
        df = pd.read_csv(str(fname), sep=",")
        x=list(df[list(df)[0]])
        y=list(df[list(df)[1]])
        #print x,y
        self.te=(zip(x,y))
        
        
    def getdis(self,dis):
        if dis=="cityblock":
            self.dm=cityblock_distance
        elif dis=="euclidean":
            self.dm=euclidean_distance
        else:
            self.dm=chebyshev_distance
        print self.dm

    def startkmn(self):
                   
        
        import pandas as pd
        df = pd.read_csv(str(self.fname), sep=",")
        print (df)
        x=list(df[list(df)[7]])
        y=list(df[list(df)[6]])
        self.tr=(zip(x,y))
        print self.tr
        c = KMeansClustering(self.tr,self.dm)
        jj=c.getclusters(self.k)
        import matplotlib.pyplot as plt
        
        
        for pairs in jj:
            area = np.pi * (15 * np.random.rand(len(pairs)))
            colors=np.random.rand(len(pairs))
            plt.scatter([p[0] for p in pairs], [p[1] for p in pairs],s=area ,c=colors,alpha=1)
            plt.show()
        
        

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "Clusterer", None))
        self.lineEdit.setText(_translate("Form", "K-Means", None))
        self.groupBox_2.setTitle(_translate("Form", "Neighbors", None))
        self.label.setText(_translate("Form", "Number of neighbors", None))
        self.groupBox_4.setTitle(_translate("Form", "Distance", None))
        self.comboBox_2.setItemText(0, _translate("Form", "euclidean", None))
        self.comboBox_2.setItemText(1, _translate("Form", "chebychev", None))
        self.comboBox_2.setItemText(2, _translate("Form", "cityblock", None))
        self.checkBox_3.setText(_translate("Form", "Equality measure", None))
        self.label_2.setText(_translate("Form", "Number of Trails", None))
        self.pushButton_3.setText(_translate("Form", "Start", None))
        self.pushButton.setText(_translate("Form", "Input File", None))
        #self.pushButton_2.setText(_translate("Form", "Output Folder", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Form()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

