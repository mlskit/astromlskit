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
        Form.resize(241, 193)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 201, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(40, 20, 141, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 80, 161, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 140, 161, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 110, 161, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton.clicked.connect(self.takeinput)
        self.pushButton_2.clicked.connect(self.takeoutput)
        self.pushButton_3.clicked.connect(self.startmlinear)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "Regressior", None))
        self.lineEdit.setText(_translate("Form", "Multiple linear", None))
        self.pushButton.setText(_translate("Form", "X-File", None))
        self.pushButton_3.setText(_translate("Form", "Start", None))
        self.pushButton_2.setText(_translate("Form", "Y-File", None))

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
        
    def startmlinear(self):
        import numpy as np
        X=np.array(self.xdata)
        Y=np.array(self.ydata)
        X=[[float(y) for y in x] for x in X]
        Y=[[float(y) for y in x] for x in Y]
        from sklearn import linear_model
        clf = linear_model.LinearRegression()
        clf.fit (X,Y)
        print clf.coef_
    
        

        
    

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Form()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
