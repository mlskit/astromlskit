import sys
from PyQt4 import QtGui,QtCore
#import kmeans
import pyqtgraph as pg
import random
from numpy import *
from math import *
import numpy as np
from idleint import *
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
####################################### all the algorithm files###################################################
import naiveui,knnfront,dtreefront,forestfront,kmnfront,heirarfrontend

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
		pw.plot(self.x,self.y)
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
##########################################################################
class Pareto():#range restricted to 10000
                def __init__(self):
                        self.x=[]
                        self.y=[]
                        a=self.shape=random.randint(1,10000)
                        #a=2
                        for i in range(1,random.randint(1,1000)):
                                       self.x.append(i)
                                       fx=((a*1.0)*(pow(i,-(a+1))))
                                       self.y.append(fx)
                def graph(self,pw):
                        pw.plot(self.x,self.y)
###############################################################################                                                   
class Chi2():

        def __init__(self):
                self.x=[]
                self.y=[]
                v=self.sdof=random.randint(1,100)
                #print "v",v
                #v=1
                for i in range(1,random.randint(0,1000)):
                               self.x.append(i)
                               aa=(v-2)/2.0
                               numerator=(pow(i,aa))*exp(-(i/2.0))
                               denominator=(pow(2,(v/2.0)))*(gamma(v/2.0))
                               fx=numerator/denominator
                               #print fx
                               self.y.append(fx)
        def graph(self,pw):
                pw.plot(self.x,self.y)
################################################################
class Student():

        def __init__(self):
                self.x=[]
                self.y=[]
                #v=self.sdof=random.randint(1,100)
                v=1
                for i in range(0,40):
                        self.x.append(i)
                        numerator=gamma((v+1)/2.0)*(pow((1+(i/(v*v*1.0))),-(v+1)/2.0))
                        denominator=math.sqrt(v*(22/7.0))*gamma(v/2.0)
                        #print numerator,denominator
                        fx=numerator/denominator
                        self.y.append(fx)
        def graph(self,pw):
                pw.plot(self.x,self.y)

                
                

##########################################################
class Ray():
        def __init__(self):
                self.x=[]
                self.y=[]
                #a=self.alpha=random.randint(1,100)
                a=2
                for i in range(0,500):
                        self.x.append(i)
                        numerator=i*(exp(-i*i/2*a*a*1.0))
                        denominator=a*a*1.0
                        print numerator,denominator,i
                        fx=numerator/denominator
                        self.y.append(fx)
        def graph(self,pw):
                pw.plot(self.x,self.y)
#############################################################
class visuals(QtGui.QMainWindow):
    def __init__(self):
        super(visuals,self).__init__()
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
        self.show()

    def draw(self):
        view = pg.GraphicsLayoutWidget()  ## GraphicsView with GraphicsLayout inserted by default
        self.setCentralWidget(view)
        w1 = view.addPlot()
        n = 5
        s1 = pg.ScatterPlotItem(size=10, pen=pg.mkPen(None), brush=pg.mkBrush(255, 255, 255, 120))
        pos = np.random.normal(size=(2,n), scale=1e-5)
        spots = [{'pos': pos[:,i], 'data': 1} for i in range(n)] + [{'pos': [0,0], 'data': 1}]
        s1.addPoints(spots)
        w1.addItem(s1)
        w1.show()
        w2 = view.addPlot()
        n = 5
        s2 = pg.ScatterPlotItem(size=10, pen=pg.mkPen(None), brush=pg.mkBrush(100, 100, 255, 120))
        pos = np.random.normal(size=(2,n), scale=1e-5)
        spots = [{'pos': pos[:,i], 'data': 1} for i in range(n)] + [{'pos': [0,0], 'data': 1}]
        s2.addPoints(spots)
        w1.addItem(s2)
        w1.show()
        
            

#################################################################
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
       self.combo.addItem("BINOMIAL")
       self.combo.addItem("F")
       self.combo.addItem("NORMAL")
       self.combo.addItem("EXPONENTIAL")
       self.combo.addItem("BETA")
       self.combo.addItem("BERN")
       self.combo.addItem("POISSON")
       self.combo.addItem("LOGNORMAL")
       self.combo.addItem("ERLANG")
       self.combo.addItem("GAMMA")
       self.combo.addItem("PARETO")
       self.combo.addItem("CHI2")
       self.combo.addItem("STUDENT-T")
       self.combo.addItem("RAY")
       
       self.combo.activated[str].connect(self.draw)
       #self.toolbar = self.addToolBar(
       self.show()

    def draw(self,txt):
       pw = pg.PlotWidget(name='Plot1')
       self.setCentralWidget(pw)
       if txt == "BINOMIAL":
          xx=Binomial()
          xx.graph(pw)
       elif txt == "RAY":
          xx=Ray()
          xx.graph(pw)   
       elif txt == "STUDENT-T":
          xx=Student()
          xx.graph(pw)
       elif txt == "CHI2":
          xx=Chi2()
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
       elif txt=="PARETO":
          #pl.clf()
          xx=Pareto()
          xx.graph(pw)
###############################################################################################################################################
          ## Clustering algorithms
#################################################################################################################################################
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
################################################################################################################################################

#DummY test code
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
#########################################################################################################
####   classes for each format                                          ########
################################################################################
class nbmain(QtGui.QMainWindow):
        def __init__(self):
                super(nbmain, self).__init__()

                self.ui = naiveui.Ui_Form()
                self.ui.setupUi(self)

class knnmain(QtGui.QMainWindow):
        def __init__(self):
                super(knnmain, self).__init__()

                self.ui = knnfront.Ui_Form()
                self.ui.setupUi(self)
                
class dtreemain(QtGui.QMainWindow):
        def __init__(self):
                super(dtreemain, self).__init__()

                self.ui = dtreefront.Ui_Form()
                self.ui.setupUi(self)
class forestmain(QtGui.QMainWindow):
        def __init__(self):
                super(forestmain, self).__init__()

                self.ui = forestfront.Ui_RandomForest()
                self.ui.setupUi(self)


############################################################################################################################################
################### Cluster UI mains ##########################################################################################################
################################################################################################################################################
class kmeansmain(QtGui.QMainWindow):
        def __init__(self):
                super(kmeansmain, self).__init__()

                self.ui = kmnfront.Ui_Form()
                self.ui.setupUi(self)

class hmain(QtGui.QMainWindow):
        def __init__(self):
                super(hmain, self).__init__()

                self.ui = heirarfrontend.Ui_Form()
                self.ui.setupUi(self)


############################################################################################################################################

                
class App(QtGui.QMainWindow):
    
    def __init__(self):
        super(App, self).__init__()
        self.win = MyInterpreter(None)
        self.setCentralWidget(self.win)
        self.initUI()

    def scatter(self):
        self.w= visuals()
        self.w.draw()
        #self.w.draw()
        
#        pass
    def dist(self):
        print "Opening a new popup window..."
        self.w = DisPlot()
        self.w.show()
    def testme(self):
        pass
    def Scat(self):
        pass
    def kmn(self):
        print "Doing Kmeans  ...."
        self.w=KmeansG()
        self.w.show()
    def knn(self):
        pass

    def fnb(self):
        self.w1=nbmain()
        self.w1.show()
        


    def fknn(self):
        self.w2=knnmain()
        self.w2.show()
        

    def fdtree(self):
        self.w3=dtreemain()
        self.w3.show()
        

    def fforest(self):
        self.w4=forestmain()
        self.w4.show()
        
    def flda(self):
        pass

    def flrl(self):
        pass
    def fsvm(self):
        pass
    def fann(self):
        pass
    def fkmeans(self):
        self.w9=kmeansmain()
        self.w9.show()    
        
    def fdbscna(self):
        pass
    def fhierarchy(self):
        self.w11=hmain()
        print "showing\n"
        self.w11.show()
    def fgmm(self):
        pass
    def fpca(self):
        pass
    def fgsa(self):
        pass


    
    def initUI(self):               

        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        self.statusBar()

        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Classification')
        fileMenu.addAction('Naive Bayes',self.fnb)
        fileMenu.addAction('K- Nearest Neighbors',self.fknn)
        fileMenu.addAction('Decision tree',self.fdtree)
        fileMenu.addAction('Random Forest',self.fforest)
        fileMenu.addAction('LDA classifier',self.flda)
        fileMenu.addAction('Logistic regression learner',self.flrl)
        fileMenu.addAction('SVM',self.fsvm)
        fileMenu.addAction('A-Neural-nets',self.fann)
        

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Regression')
        fileMenu.addAction('Linear Regression',self.Scat)
        fileMenu.addAction('Multiple Regression',self.Scat)
        fileMenu.addAction('Lasso',self.Scat)
        fileMenu.addAction('Ridge',self.Scat)


        menubar = self.menuBar()
        fileMenu1 = menubar.addMenu('Unsupervised Clustering')
        #fileMenu1 = fileMenu.addMenu('Dumb')
        fileMenu1.addAction('K-Means',self.fkmeans)
        fileMenu1.addAction('Dbscan',self.Scat)        
        fileMenu1.addAction('Hierarchial',self.fhierarchy)
        fileMenu1.addAction('Gausiann Mixture',self.Scat)
        fileMenu1.addAction('PCA',self.Scat)
        fileMenu1.addAction('Gravitational clustering',self.Scat)
    
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Visualisation')
        fileMenu.addAction('Scatter Plots',self.scatter)
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
        fileMenu.addAction('All-in-one',self.dist)
        
        self.setGeometry(100, 100, 700, 600)
        self.setWindowTitle('Statistical Toolkit v1.0')

        self.layout = QVBoxLayout(self)
        
        
        self.show()        

def main():

    
    app = QtGui.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main() 
