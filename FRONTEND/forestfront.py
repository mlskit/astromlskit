

from PyQt4 import QtCore, QtGui
from dtree import *
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

class Ui_RandomForest(object):
    def setupUi(self, RandomForest):
        RandomForest.setObjectName(_fromUtf8("RandomForest"))
        RandomForest.resize(257, 442)
        self.groupBox = QtGui.QGroupBox(RandomForest)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 221, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))

        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(40, 20, 141, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.groupBox_2 = QtGui.QGroupBox(RandomForest)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 80, 211, 251))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))

        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(30, 20, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.spinBox = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox.setGeometry(QtCore.QRect(150, 20, 42, 22))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.spinBox.valueChanged.connect(self.notree)

        self.spinBox_2 = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox_2.setGeometry(QtCore.QRect(150, 50, 42, 22))
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.spinBox_2.valueChanged.connect(self.sample)

        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 111, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.comboBox_2 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 100, 161, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.activated[str].connect(self.grow)

        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(60, 80, 111, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(60, 130, 111, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.comboBox_3 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_3.setGeometry(QtCore.QRect(20, 150, 161, 22))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.activated[str].connect(self.weigh)

        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(60, 180, 111, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.comboBox_4 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_4.setGeometry(QtCore.QRect(20, 200, 161, 22))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.activated[str].connect(self.ent)

        self.pushButton = QtGui.QPushButton(RandomForest)
        self.pushButton.setGeometry(QtCore.QRect(40, 340, 161, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.takeinput)
       

        self.pushButton_2 = QtGui.QPushButton(RandomForest)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 380, 161, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.taketest)
        
        self.pushButton_3 = QtGui.QPushButton(RandomForest)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 410, 161, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(self.startrft)

        self.retranslateUi(RandomForest)
        QtCore.QMetaObject.connectSlotsByName(RandomForest)
        
    def takeinput(self):
        self.fname = QtGui.QFileDialog.getOpenFileName(None, 'Open file', 'C:')
        print type(self.fname)
        
    def taketest(self):
        self.tfname = QtGui.QFileDialog.getOpenFileName(None, 'Open file', 'C:')
        print (self.tfname)

    def startrft(self):
        print 'Testing forest...'

        cdata2 = Data(str(self.fname))
        cda=Data(str(self.tfname))
        cdata2test=list(cda)

        print self.no,self.samp

        forest = Forest(
        data=cdata2,
        size=int(self.no), # Grow 10 trees.
        sample_ratio=int(self.samp)/10.0, # Train each tree on 80% of all records.
        grow_method=GROW_AUTO_INCREMENTAL, # Incrementally grow each tree.
        weighting_method=Forest.mean_oob_mae_weight,
        #weighting_method=str(self.wei),
        tree_kwargs=dict(metric=ENTROPY2),
        )
        mae = None
        for _ in xrange(10):
            for row in cdata2test:
                #print row
                forest.train(row)
            mae = forest.test(cdata2test)
            print 'Forest MAE:',mae.mean
        #if mae.mean==1.0:
            #print "WellDone!!!"
        from pprint import pprint
        trees = list(forest.trees)
        trees.sort(key=lambda t:t.out_of_bag_mae.mean)
        print 'Best tree:'
        pprint(trees[-1].to_dict(), indent=4)
        #assertEqual(trees[-1].auto_grow, True)
        print "--------- ALL TREES---------------"
        for tree in trees:
                    pprint(tree.to_dict(), indent=4)
        

        print "---done----"
            
    def ent(self,txt):
        self.ent=txt
        print txt
    def grow(self,txt):
        self.grw=txt
        print txt
    def weigh(self,txt):
        self.wei=txt
        print txt        
    def notree(self):
        self.no=self.spinBox.value()
        print self.no
        
    def sample(self):
        self.samp=self.spinBox_2.value()
        if self.samp>10:
            self.samp=10
        print self.samp/10.0

    def retranslateUi(self, RandomForest):
        RandomForest.setWindowTitle(_translate("RandomForest", "Forest Learner", None))
        self.groupBox.setTitle(_translate("RandomForest", "Learner/Classifier Name", None))
        self.lineEdit.setText(_translate("RandomForest", "Random Forest", None))
        self.groupBox_2.setTitle(_translate("RandomForest", "Options", None))
        self.label.setText(_translate("RandomForest", "Number of Trees", None))
        self.label_2.setText(_translate("RandomForest", "Sample ratio", None))
        self.comboBox_2.setItemText(0, _translate("RandomForest", "GROW_RANDOM", None))
        self.comboBox_2.setItemText(1, _translate("RandomForest", "GROW_AUTO_INCREMENTAL", None))
        self.comboBox_2.setItemText(2, _translate("RandomForest", "GROW_AUTO_MINI_BATCH", None))
        self.label_3.setText(_translate("RandomForest", "Grow Method", None))
        self.label_4.setText(_translate("RandomForest", "weighting_method", None))
        self.comboBox_3.setItemText(0, _translate("RandomForest", "mean_oob_mae_weight", None))
        self.comboBox_3.setItemText(1, _translate("RandomForest", "best_oob_mae_weight", None))
        self.label_5.setText(_translate("RandomForest", "Entropy metric", None))
        self.comboBox_4.setItemText(0, _translate("RandomForest", "ENTROPY1", None))
        self.comboBox_4.setItemText(1, _translate("RandomForest", "ENTROPY2", None))
        self.comboBox_4.setItemText(2, _translate("RandomForest", "ENTROPY3", None))
        self.pushButton.setText(_translate("RandomForest", "Train File", None))
        self.pushButton_2.setText(_translate("RandomForest", "Test File", None))
        self.pushButton_3.setText(_translate("RandomForest", "Start", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_RandomForest()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
