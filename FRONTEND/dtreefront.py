
from dtree import Tree, Data
from PyQt4 import QtCore, QtGui
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
        Form.resize(256, 410)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 221, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.fname=""
        self.temp=""
        self.todo="dtree"
        self.bp=False
        self.v=False
        self.pdf=False
        self.tf=""
        self.method="classification"
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(40, 20, 141, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 80, 221, 80))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))

        self.comboBox = QtGui.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(30, 30, 151, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.activated[str].connect(self.getmethod)

        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 170, 221, 91))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))

        self.checkBox_3 = QtGui.QCheckBox(self.groupBox_3)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 20, 151, 17))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.checkBox_3.stateChanged.connect(self.printtree)
        
        self.checkBox_4 = QtGui.QCheckBox(self.groupBox_3)
        self.checkBox_4.setGeometry(QtCore.QRect(30, 40, 151, 17))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.checkBox_4.stateChanged.connect(self.printvar)

        self.checkBox_5 = QtGui.QCheckBox(self.groupBox_3)
        self.checkBox_5.setGeometry(QtCore.QRect(30, 60, 151, 17))
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.checkBox_5.stateChanged.connect(self.printbp)

        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 340, 161, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(self.startdtree)

        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 280, 161, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.takeinput)

        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 310, 161, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.takeoutput)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def printtree(self):
        print "Tree printed"

    def printvar(self):
        print "Variance"

    def printbp(self):
        print "bp"
        
    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "Regressor/Classifier Name", None))
        self.lineEdit.setText(_translate("Form", "Decision Tree", None))
        self.groupBox_2.setTitle(_translate("Form", "Types", None))
        self.comboBox.setItemText(0, _translate("Form", "classification", None))
        self.comboBox.setItemText(1, _translate("Form", "regression", None))
        self.groupBox_3.setTitle(_translate("Form", "Options", None))
        self.checkBox_3.setText(_translate("Form", "           Print Tree.pdf", None))
        self.checkBox_4.setText(_translate("Form", "           Print Variance", None))
        self.checkBox_5.setText(_translate("Form", "           Print best/probability", None))
        self.pushButton_3.setText(_translate("Form", "Start", None))
        self.pushButton.setText(_translate("Form", "Input File", None))
        self.pushButton_2.setText(_translate("Form", "Test File", None))

    def getmethod(self,txt):
        print txt

    def takeinput(self):
        self.fname = QtGui.QFileDialog.getOpenFileName(None, 'Open file', 'C:')
        #print (self.fname)
        self.a = Tree.build(Data(str(self.fname)))
        print self.a,"hello"
        
    def startdtree(self):
        temp=[]
        for i in self.testdata:
            i=map(int,i)
            tata=dict(zip(self.header,i))
            print tata
            prediction = self.a.predict(tata)
            temp.append(prediction.best)
        print temp

    def takeoutput(self):
        self.tf = QtGui.QFileDialog.getOpenFileName(None, 'Open file', 'C:')
        self.testdata=[]
        for line in open(str(self.tf)):
            row=line.split("\n")[0].split(",")
            self.testdata.append(row)
        self.header=self.testdata[0]
        self.testdata=self.testdata[1:]
            
        #print str(self.tf)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Form()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
