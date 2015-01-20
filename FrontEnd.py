import sys
from PyQt4 import QtGui,QtCore
#add frontend here

class Exampleone(QtGui.QWidget):
    #remove this
    def __init__(self):
        super(Exampleone, self).__init__()
        self.initUI()
        
    def initUI(self):      

        cb = QtGui.QCheckBox('time pass]', self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)
   
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QtGui.QCheckBox')
        self.show()
        
    def changeTitle(self, state):
      
        if state == QtCore.Qt.Checked:
            self.setWindowTitle('QtGui.QCheckBox')
        else:
            self.setWindowTitle('')


class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        cb = QtGui.QCheckBox('Show title', self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QtGui.QCheckBox')
        self.show()
        
    def changeTitle(self, state):
      
        if state == QtCore.Qt.Checked:
            self.setWindowTitle('QtGui.QCheckBox')
        else:
            self.setWindowTitle('')


class App(QtGui.QMainWindow):
    
    def __init__(self):
        super(App, self).__init__()
        
        self.initUI()

    def testme(self):
        print "Opening a new popup window..."
        self.w = Example()
        self.w.show()
        
    def Scat(self):
        print "Opening a new popup sca window..."
        self.w = Exampleone()
        self.w.show()
        pass
    
    def initUI(self):               
        
        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        self.statusBar()

        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&EDA')
        fileMenu.addAction('Scatter Plot',self.Scat)
        

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Regression and Anova')
        fileMenu.addAction('Regression',self.Scat)
        fileMenu.addAction('Mixed effect',self.Scat)
        fileMenu.addAction('Anova',self.Scat)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Machine learning')
        fileMenu1 = fileMenu.addMenu('Dumb')
        fileMenu1.addAction('classification',self.testme)
        fileMenu1.addAction('cluster Analysis',self.Scat)
        fileMenu1.addAction('feature selection',self.Scat)
    
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Visualisation')
        fileMenu.addAction('Scatter Plots',self.testme)
        fileMenu.addAction('Dendograms',self.testme)
        fileMenu.addAction('Biplots',self.testme)
        fileMenu.addAction('Andrew Plots',self.testme)
        fileMenu.addAction('Glyph Plots',self.testme)
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Goodness Fit')
        fileMenu.addAction('Chi-square',self.testme)
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('DOE')
        fileMenu.addAction('Fractional factorial',self.testme)
        

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Distribution')
        fileMenu.addAction('All-in-one',self.testme)
        
        
        self.setGeometry(1000, 300, 300, 200)
        self.setWindowTitle('Statistical Toolkit v1.0')    
        self.show()
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main() 
