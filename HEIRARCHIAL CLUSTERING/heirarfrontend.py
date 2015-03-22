# -*- coding: utf-8 -*-


from PyQt4 import QtCore, QtGui
from scipy.cluster.hierarchy import linkage, dendrogram
from DM import *
import scipy.cluster.hierarchy as hac
import pandas as pd
import matplotlib.pyplot as plt

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
        Form.resize(251, 371)
        self.dis=euclidean_distance
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 221, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))

        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(40, 20, 141, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.groupBox_4 = QtGui.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 80, 221, 121))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))

        self.comboBox_2 = QtGui.QComboBox(self.groupBox_4)
        self.comboBox_2.setGeometry(QtCore.QRect(30, 20, 161, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.activated[str].connect(self.getdis)

        self.checkBox_3 = QtGui.QCheckBox(self.groupBox_4)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 60, 151, 17))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))

        self.checkBox_4 = QtGui.QCheckBox(self.groupBox_4)
        self.checkBox_4.setGeometry(QtCore.QRect(30, 90, 151, 17))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))

        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 330, 161, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(self.starthcc)

        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 300, 161, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.takeinput)

        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 200, 221, 80))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))

        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 20, 161, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))

        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 50, 161, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def takeinput(self):
        fname = QtGui.QFileDialog.getOpenFileName(None, 'Open file', 'C:')
        print type(fname)
        df = pd.read_csv(str(fname), sep=",")
        x=list(df[list(df)[0]])
        y=list(df[list(df)[1]])
        self.tr=(zip(x,y))
        #print self.tr
        

                

    def starthcc(self):
        dataFrame = pd.DataFrame(self.tr, columns=['x', 'y'])
        from scipy.spatial.distance import pdist, squareform
        
        # not printed as pretty, but the values are correct
        distxy = squareform(pdist(dataFrame, metric=self.dm))
        #print distxy
        
        plt.figure()
        R = dendrogram(linkage(distxy, method='complete'))
        
        plt.xlabel('X units')
        plt.ylabel('Y units')
        plt.suptitle('Cluster Dendrogram', fontweight='bold', fontsize=14);
       
        plt.show()
        pass

    def getdis(self,txt):
            if txt=="chebychev":
                self.dm=chebyshev_distance
            elif txt=="cityblock":
                self.dm=cityblock_distance
            else:
                self.dm=euclidean_distance
            print self.dm
                
    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "Clusterer", None))
        self.lineEdit.setText(_translate("Form", "Hierarchical", None))
        self.groupBox_4.setTitle(_translate("Form", "Distance", None))
        self.comboBox_2.setItemText(0, _translate("Form", "euclidean", None))
        self.comboBox_2.setItemText(1, _translate("Form", "chebychev", None))
        self.comboBox_2.setItemText(2, _translate("Form", "cityblock", None))
        self.checkBox_3.setText(_translate("Form", "Random Data", None))
        self.checkBox_4.setText(_translate("Form", "plot dendrogram", None))
        self.pushButton_3.setText(_translate("Form", "Start", None))
        self.pushButton.setText(_translate("Form", "Input File", None))
        self.groupBox_2.setTitle(_translate("Form", "info", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Form()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

