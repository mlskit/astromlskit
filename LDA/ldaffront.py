from PyQt4 import QtCore, QtGui
from lda import *
import pylab as pl
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
        Form.resize(248, 395)
        self.d=2
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 350, 161, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 290, 161, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.takeinput)

        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 320, 161, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.takeoutput)
        

        self.groupBox_5 = QtGui.QGroupBox(Form)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 10, 221, 61))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))

        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 20, 141, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))

        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 90, 221, 80))
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
        self.spinBox.valueChanged.connect(self.setd)

        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 180, 221, 101))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.pushButton_3.clicked.connect(self.startlda)
    
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton_3.setText(_translate("Form", "Start", None))
        self.pushButton.setText(_translate("Form", "Input File", None))
        self.pushButton_2.setText(_translate("Form", "Output Folder", None))
        self.groupBox_5.setTitle(_translate("Form", "Learner/Classifier Name", None))
        self.lineEdit_2.setText(_translate("Form", "LDA", None))
        self.groupBox_2.setTitle(_translate("Form", "Options", None))
        self.label.setText(_translate("Form", "Dimensionality", None))
        self.checkBox.setText(_translate("Form", "Print/plot", None))

    def setd(self):
        self.d=self.spinBox.value()
        print self.d
        
    def takeinput(self):
        fname = QtGui.QFileDialog.getOpenFileName(None, 'Open file', 'C:')
        print type(fname)
        
        import pandas as pd
        try:
            df = pd.read_csv(str(fname), sep=",")
        except:
            sys.exit(0)
        x=list(df[list(df)[0]])
        y=list(df[list(df)[1]])
        self.classlabels=list(df[list(df)[2]])
        self.tr=(zip(x,y))
        print self.tr
        
    def takeoutput(self):
        print "output Taken"
        return
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
    
    def startlda(self):
        data=np.array(self.tr)
        labels=np.array(self.classlabels)
        newData,w = lda(data,labels,self.d)
        print newData,w
        out=open("output.txt","w+")
        print>>out,newData,w
        pl.plot(data[:,0],data[:,1],'o',newData[:,0],newData[:,0],'.')
        pl.show()

        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Form()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
