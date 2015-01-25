import sys
from PyQt4 import QtGui,QtCore
import kmeans


class KmeansG(QtGui.QWidget):
    def __init__(self):
        super(KmeansG, self).__init__()
        self.initUI()
        self.filename=""

    def initUI(self):
        layout = QtGui.QVBoxLayout(self)
        self.button = QtGui.QPushButton('Select Files', self)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.handleButton)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.button1 =QtGui.QPushButton('Cluster!!', self)
        self.button1.clicked.connect(self.begin)
        
    def handleButton(self):
        title = self.button.text()
        for path in QtGui.QFileDialog.getOpenFileNames(self, title):
            self.filename=path
            
            
    def begin(self):
        km = kmeans.kClusterer(self.filename,3)
        km.kCluster()
        km.showMembers()
        #exit(0)
        
    

    '''  
    def __init__(self):
        super(KmeansG, self).__init__()
        self.initUI()
                
    def initUI(self):      

        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)       
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()
        
    def showDialog(self):

        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', 
                '/home')
        
        f = open(fname, 'r')
        
        with f:        
            data = f.read()
            self.textEdit.setText(data) 
                                
        
     '''   


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
        self.w = KmeansG()
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
        
        
        self.setGeometry(100, 100, 700, 600)
        self.setWindowTitle('Statistical Toolkit v1.0')    
        self.show()
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main() 
