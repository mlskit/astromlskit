import sys
from PyQt4 import QtGui,QtCore
#import kmeans
import pyqtgraph as pg
import random
from numpy import *
from math import *

#######################################################################################################
class Binomial():

	def __init__(self):
		n=self.trial=random.randint(10,1000) #randomly generate the number of trials
		p=self.probability=random.uniform(0.0,1.0) #randomly generate the probability of success
		self.x=[] #define a list for plotting
		self.y=[] #define a list for plotting
		for i in range(n+1):
			r=i
			self.x.append(r)
			c=(factorial(n))/(factorial(n-r)*factorial(r)) #ncr
			q=1-p
			s=n-r
			P=c*(p**r)*(q**s)
	#		print p
			self.y.append(P)

	def graph(self,pw):
		pw.plot(self.x,self.y)
		#pl.show()
	def rand(self):
		return self.y
	def NumberOfTrials(self):
		return self.trial
	def ProbabilityOfSuccess(self):
		return self.probability

########################################################################################################
class Poisson():

	def __init__(self):
		u=self.mean=random.uniform(0,50.0)
		self.x=[]
		self.y=[]
		for i in range(50):
			self.x.append(i)
			f=((u**i)*exp(-u))/factorial(i);
			self.y.append(f)

	def graph(self,pw):
		pl.plot(self.x,self.y)
		#pl.show()
	def rand(self):
		return self.y
	def getMean(self):
		return self.mean
#########################################################################################################
class Normal():

	def __init__(self):
		u=self.mean=random.uniform(30,100.0)
		self.x=[]
		self.y=[]
		s=self.standardDeviation=random.uniform(1,30)
		for i in range(-100,200):
			self.x.append(i)
			f=(1/(s*sqrt(2*pi)))*exp(-((i-u)**2)/(2*(s**2)))
			self.y.append(f)
	def graph(self,pw):
		pw.plot(self.x,self.y)
		#pl.show()
	def rand(self):
		return self.y
	def getMean(self):
		return self.mean
	def getSD(self):
		return self.standardDeviation
############################################################################################################
class LogNormal():

	def __init__(self):
		m=self.mean=random.uniform(50,100)
		v=self.standardDeviation=random.uniform(1,30)
		u=log((m**2)/(sqrt(v+(m**2))))
		s=sqrt(log(1+(v/m**2)))
		self.x=[]
		self.y=[]
		for i in range(1,200):
			self.x.append(i)
			f=(1/(i*s*sqrt(2*pi)))*exp(-((log(i)-u)**2)/(2*(s**2)))
			self.y.append(f)
	#		print self.x
	#		print self.y
	def graph(self,pw):
		#print self.x
		pw.plot(self.x,self.y)
		#pl.show()
	def rand(self):
		return self.y
	def getMean(self):
		return self.mean
	def getSD(self):
		return self.standardDeviation

###############################################################################################################
class Expo():

	def __init__(self):
		a=self.scaleparameter=random.randint(1,100)
		self.x=[ ]
		self.y=[ ]
		end=random.randint(0,1000)
		#print end,"end"
		#time.sleep(1)
		for i in range(0,random.randint(1,2000)):
			self.x.append(i)
			fx =(1.0/a)*exp(-((i*1.0)/a))
			#print fx
		#	time.sleep(2)
			self.y.append(fx)
	def graph(self,pw):
		pw.plot(self.x,self.y)
		#pl.show()

##########################################################################
class Beta():

	def __init__(self):
		#shape parameters are here
		a=self.param1=random.random()
		b=self.param2=random.random()
		#a=self.param1=0.5
		#b=self.param2=0.5
		self.x=[]
		self.y=[]
		#print "in beta",a,b
		for i in arange(0,1,0.01):
			self.x.append(i)
			beta=(gamma(a)*gamma(b))/(gamma(a+b))
			fx=(pow(i,a)*pow((1-i),b-1))/beta
#			print "fx",fx
			self.y.append(fx)
		return

	def graph(self,pw):
		#print "plotting graph"
		pw.plot(self.x,self.y)
		#pl.show()


#########################################
class Bern():
		def __init__(self):
			self.x=[]
			self.y=[]
			p=self.success=random.random()
			for i in arange(0,1.1,random.random()):
				self.x.append(i)
				if i == 0:
					self.y.append(1-p)
				elif i == 1:
					self.y.append(p)
				else:
					self.y.append(0)
		def graph(self,pw):
		#	print "plotting graph"
			pw.plot(self.x,self.y)
			#pl.show()
###################################################
class Erlang():

		def __init__(self):
			self.x=[]
			self.y=[]
			a=self.scale=random.random()
			m=self.shapeparam=random.randint(0,100)

			for i in range(0,random.randint(0,21)):
				self.x.append(i)
				pdf=pow(i,m-1)*exp(-i/(a*1.0));
				pdf=pdf/(factorial(m-1)*pow(a,m)*1.0)
				self.y.append(pdf)
			#	print "pdf",pdf
		def graph(self,pw):
		#	print "plotting graph"
			pw.plot(self.x,self.y)
			#pl.show()
#################################################
class F():

	def __init__(self):
		self.x=[]
		self.y=[]
		n=self.degreefreedom1=random.randint(1,10)
		m=self.degreefreedom2=random.randint(1,10)
		for i in range(0,random.randint(1,1000)):
			self.x.append(i)
			term1=pow((n*1.0)/m,(n/2.0))/((gamma(n/2.0)*gamma(m/2.0))/gamma((n/2.0)+(m/2.0)))
			term2=pow(i,n-2/(2.0))
			term3=pow((1+(n/(m*1.0))*(i)),-(n+m)/2.0)
			fx=term1*term2*term3
			#print fx
			self.y.append(fx)
	def graph(self,pw):
			#print "plotting graph"
			pw.plot(self.x,self.y)
			#pl.show()

################################################
class Gamma():

	def __init__(self):
		self.x=[]
		self.y=[]
		a=self.scale=random.randint(1,100)
		b=self.shape=random.randint(1,10)
		for i in range(0,random.randint(1,300)):
			self.x.append(i)
			term1=pow((i/(a*1.0)),b-1)
			term2=exp(-i*1.0/a)
			term3=a*gamma(b)
			fx=term1*term2*term3
			self.y.append(fx)
	def graph(self,pw):
			#print "plotting graph"
			pw.plot(self.x,self.y)
			#pl.show()



################################################################

class DisPlot(QtGui.QMainWindow):
    def __init__(self):
        super(DisPlot,self).__init__()
        self.initUI()
        
    def initUI(self):
       self.setGeometry(300, 300, 350, 300)
       self.setWindowTitle('File dialog')
       menubar = self.menuBar()
       fileMenu = menubar.addMenu('&File')
       fileMenu = menubar.addMenu('&View')
       fileMenu = menubar.addMenu('&Tools')
       fileMenu = menubar.addMenu('&Window')
       fileMenu = menubar.addMenu('&Help')


       exitAction = QtGui.QAction(QtGui.QIcon('exit24.png'), 'Exit', self)
       exitAction.setShortcut('Ctrl+Q')
       exitAction.triggered.connect(QtGui.qApp.quit)
        
       self.toolbar = self.addToolBar('Exit')
       self.toolbar.addAction(exitAction)
       self.combo=QtGui.QComboBox()
       self.lbl = QtGui.QLabel("Distributions", self)
       self.toolbar.addWidget(self.lbl)
       self.toolbar.addWidget(self.combo)
       self.combo.addItem("Binomial")
       self.combo.addItem("F")
       self.combo.addItem("NORMAL")
       self.combo.addItem("EXPONENTIAL")
       self.combo.addItem("BETA")
       self.combo.addItem("BERN")
       
       self.combo.activated[str].connect(self.draw)
       #self.toolbar = self.addToolBar(
       self.show()

    def draw(self,txt):
       pw = pg.PlotWidget(name='Plot1')
       self.setCentralWidget(pw)
       if txt == "Binomial":
          xx=Binomial()
          xx.graph(pw)
       elif txt == "POISSON":
          xx=Poisson()
          xx.graph(pw)
       elif txt == "NORMAL":
          xx=Normal()
          xx.graph(pw)
       elif txt == "LOGNORMAL":
          xx=LogNormal()
          xx.graph(pw)
       elif txt == "EXPONENTIAL":
          #pl.clf()
          xx=Expo()
          xx.graph(pw)
       elif txt == "BETA":
         # pl.clf()
          xx=Beta()
          xx.graph(pw)
       elif txt == "BERN":
          #pl.clf()
          xx=Bern()
          xx.graph(pw)
       elif txt =="ERLANG":
          xx=Erlang()
          xx.graph(pw)
       elif txt =="F":
          xx=F()
          xx.graph(pw)
       elif txt=="GAMMA":
          #pl.clf()
          xx=Gamma()
          xx.graph(pw)
       #pw.plot(self.x,self.y)

       
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
        self.show()
        
    def handleButton(self):
        title = self.button.text()
        for path in QtGui.QFileDialog.getOpenFileNames(self, title):
            self.filename=path
            
            
    def begin(self):
        km = kmeans.kClusterer(self.filename,3)
        km.kCluster()
        km.showMembers()
        #exit(0)
        
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
        self.w = DisPlot()
        self.w.show()
    def Scat(self):
        print "Opening a new popup sca window..."
        self.w = DisPlot()
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
