from PyQt4 import QtCore, QtGui
from kNN import *
from DM import *
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
        Form.resize(249, 398)
        
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 221, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))

        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(40, 20, 141, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 80, 221, 80))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))

        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(30, 20, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.checkBox = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(30, 50, 171, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))

        self.spinBox = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox.setGeometry(QtCore.QRect(150, 20, 42, 22))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.spinBox.valueChanged.connect(self.setk)
        

        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 170, 221, 111))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))

##        self.comboBox = QtGui.QComboBox(self.groupBox_3)
##        self.comboBox.setGeometry(QtCore.QRect(30, 20, 161, 22))
##        self.comboBox.setObjectName(_fromUtf8("comboBox"))

        self.checkBox_2 = QtGui.QCheckBox(self.groupBox_3)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 50, 151, 17))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))

        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_3)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 0, 221, 111))
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

        self.checkBox_4 = QtGui.QCheckBox(self.groupBox_4)
        self.checkBox_4.setGeometry(QtCore.QRect(30, 80, 181, 17))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))

        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 300, 161, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.takeinput)
        
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 330, 161, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.takeoutput)
        
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 360, 161, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(self.startknn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def startknn(self):
        #print len(np.array(self.tr).shape),len(np.array(self.classlabels).shape)
        a=train(self.tr,self.classlabels,self.k)
        #print self.k
        out=open("output.txt","w+")
        for i in self.te:
            print>>out,i,classify(a,i,distance_fn=self.dm)
#            print classify(a,i,distance_fn=self.dm)
        print "Done------------"
        
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
        
        

    def takeoutput(self):
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
        
    def getdis(self,dis="euclidean"):
        if dis=="cityblock":
            self.dm=cityblock_distance
        elif dis=="euclidean":
            self.dm=euclidean_distance
        else:
            self.dm=chebyshev_distance
        print self.dm
    
        
    def setk(self):
        self.k=self.spinBox.value()
        print self.k
        
    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "Learner/Classifier Name", None))
        self.lineEdit.setText(_translate("Form", "K Nearest Neighbors", None))
        self.groupBox_2.setTitle(_translate("Form", "Neighbors", None))
        self.label.setText(_translate("Form", "Number of neighbors", None))
        self.checkBox.setText(_translate("Form", "Wieigh by ranks not distances", None))
        self.groupBox_3.setTitle(_translate("Form", "Distance", None))
        self.checkBox_2.setText(_translate("Form", " Ignore Unknown Values", None))
        self.groupBox_4.setTitle(_translate("Form", "Distance", None))
        self.comboBox_2.setItemText(0, _translate("Form", "euclidean", None))
        self.comboBox_2.setItemText(1, _translate("Form", "chebychev", None))
        self.comboBox_2.setItemText(2, _translate("Form", "cityblock", None))
        self.checkBox_3.setText(_translate("Form", " Ignore Unknown Values", None))
        self.checkBox_4.setText(_translate("Form", " Normalize continous attributes", None))
        self.pushButton.setText(_translate("Form", "Input train File", None))
        self.pushButton_2.setText(_translate("Form", "Input test File", None))
        self.pushButton_3.setText(_translate("Form", "Start", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Form()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
