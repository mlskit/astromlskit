# -*- coding: utf-8 -*-

# Ege Öz

from PyQt4 import QtCore, QtGui
import os

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

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName(_fromUtf8("MainWindow"))
		MainWindow.resize(910, 614)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		MainWindow.setWindowIcon(icon)
		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.gridLayout = QtGui.QGridLayout(self.centralwidget)
		self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
		self.geri = QtGui.QPushButton(self.centralwidget)
		self.geri.setText(_fromUtf8(""))
		icon = QtGui.QIcon.fromTheme(_fromUtf8("back"))
		self.geri.setIcon(icon)
		self.geri.setObjectName(_fromUtf8("geri"))
		self.gridLayout.addWidget(self.geri, 0, 0, 1, 1)
		self.ileri = QtGui.QPushButton(self.centralwidget)
		self.ileri.setText(_fromUtf8(""))
		icon = QtGui.QIcon.fromTheme(_fromUtf8("forward"))
		self.ileri.setIcon(icon)
		self.ileri.setObjectName(_fromUtf8("ileri"))
		self.gridLayout.addWidget(self.ileri, 0, 1, 1, 1)
		self.adres = QtGui.QLineEdit(self.centralwidget)
		self.adres.setObjectName(_fromUtf8("adres"))
		self.gridLayout.addWidget(self.adres, 0, 2, 1, 1)
		self.yenile = QtGui.QPushButton(self.centralwidget)
		self.yenile.setText(_fromUtf8(""))
		icon = QtGui.QIcon.fromTheme(_fromUtf8("gtk-refresh"))
		self.yenile.setIcon(icon)
		self.yenile.setObjectName(_fromUtf8("yenile"))
		self.gridLayout.addWidget(self.yenile, 0, 3, 1, 1)
		self.durdur = QtGui.QPushButton(self.centralwidget)
		self.durdur.setText(_fromUtf8(""))
		icon = QtGui.QIcon.fromTheme(_fromUtf8("process-stop"))
		self.durdur.setIcon(icon)
		self.durdur.setObjectName(_fromUtf8("durdur"))
		self.gridLayout.addWidget(self.durdur, 0, 4, 1, 1)
		self.git = QtGui.QPushButton(self.centralwidget)
		self.git.setText(_fromUtf8(""))
		icon = QtGui.QIcon.fromTheme(_fromUtf8("draw-arrow-forward"))
		self.git.setIcon(icon)
		self.git.setObjectName(_fromUtf8("git"))
		self.gridLayout.addWidget(self.git, 0, 5, 1, 1)
		self.ev = QtGui.QPushButton(self.centralwidget)
		self.ev.setText(_fromUtf8(""))
		icon = QtGui.QIcon.fromTheme(_fromUtf8("go-home"))
		self.ev.setIcon(icon)
		self.ev.setObjectName(_fromUtf8("ev"))
		self.gridLayout.addWidget(self.ev, 0, 6, 1, 1)
		self.arama = QtGui.QLineEdit(self.centralwidget)
		self.arama.setObjectName(_fromUtf8("arama"))
		self.gridLayout.addWidget(self.arama, 0, 7, 1, 1, QtCore.Qt.AlignRight)
		self.ara = QtGui.QPushButton(self.centralwidget)
		self.ara.setText(_fromUtf8(""))
		icon = QtGui.QIcon.fromTheme(_fromUtf8("search"))
		self.ara.setIcon(icon)
		self.ara.setObjectName(_fromUtf8("ara"))
		self.gridLayout.addWidget(self.ara, 0, 8, 1, 1)
		self.webView = QtWebKit.QWebView(self.centralwidget)
		self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
		self.webView.setObjectName(_fromUtf8("webView"))
		self.gridLayout.addWidget(self.webView, 1, 0, 1, 9)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtGui.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 910, 21))
		self.menubar.setObjectName(_fromUtf8("menubar"))
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtGui.QStatusBar(MainWindow)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		MainWindow.setStatusBar(self.statusbar)

		QtCore.QObject.connect(self.adres, QtCore.SIGNAL(_fromUtf8("returnPressed()")),self.btn_git)
		QtCore.QObject.connect(self.arama, QtCore.SIGNAL(_fromUtf8("returnPressed()")),self.btn_ara)
		QtCore.QObject.connect(self.webView, QtCore.SIGNAL(_fromUtf8("loadStarted()")),self.wbconnectingg)
		QtCore.QObject.connect(self.webView, QtCore.SIGNAL(_fromUtf8("loadFinished()")),self.wbconnectedd)
		QtCore.QObject.connect(self.git, QtCore.SIGNAL(_fromUtf8("clicked()")), self.btn_git)
		QtCore.QObject.connect(self.yenile, QtCore.SIGNAL(_fromUtf8("clicked()")), self.webView.reload)
		QtCore.QObject.connect(self.durdur, QtCore.SIGNAL(_fromUtf8("clicked()")), self.webView.stop)
		QtCore.QObject.connect(self.ara, QtCore.SIGNAL(_fromUtf8("clicked()")), self.btn_ara)
		QtCore.QObject.connect(self.ev, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ev_kaydet)
		QtCore.QObject.connect(self.ileri, QtCore.SIGNAL(_fromUtf8("clicked()")),self.btn_ileri)
		QtCore.QObject.connect(self.geri, QtCore.SIGNAL(_fromUtf8("clicked()")),self.btn_geri)
		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		self.webView.urlChanged.connect(lambda u: self.adres.setText(u.toString()))

	def btn_ileri(self):
		self.webView.forward()

	def btn_geri(self):
		self.webView.back()

	def wbconnectingg(self):
		self.statusbar.showMessage("Connecting to "+ self.adres.text())

	def wbconnectedd(self):
		self.statusbar.showMessage("Connected.")

	def btn_git(self):
		self.webView.setUrl(QtCore.QUrl(_fromUtf8("http://" + self.adres.text())))

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "PyBrowser", None))

	def btn_ara(self):
		self.webView.setUrl(QtCore.QUrl("http://www.google.com/search?hl=en&q="+self.arama.text()+ "&aq=f&oq="))

	def ev_kaydet(self):
		evdizini=os.getenv("USER")
		yol="/home/"+evdizini+"/.pybrowser.config"
		
		if not os.path.exists(yol):
			f=open (yol,"w")
			self.statusbar.showMessage("Home page setted: "+self.adres.text())
			homepage=self.adres.text()
			f.write(homepage)
			f.close()
			
		elif os.path.exists(yol):
			f = open (yol,"r")
			evv=f.read()
			self.webView.setUrl(QtCore.QUrl(evv))
			f.close()

from PyQt4 import QtWebKit

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	MainWindow = QtGui.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())



























































































###-*- coding: utf-8 -*-
##import sys, pickle
##from PyQt4 import QtGui, QtCore
##from PyQt4.QtWebKit import *
##
####b = open("bookmarks.txt","rb")
####bookmarks = pickle.loads(b.read())
####b.close()
#### 
##url = ""
## 
##class Main(QtGui.QMainWindow):
## 
##    def __init__(self):
##        QtGui.QMainWindow.__init__(self)
##        self.initUI()
## 
##    def initUI(self):
## 
##        global bookmarks
##         
##        self.centralwidget = QtGui.QWidget(self)
## 
##        self.line = QtGui.QLineEdit(self)
##        self.line.setMinimumSize(1150,30)
##        self.line.setStyleSheet("font-size:15px;")
## 
##        self.enter = QtGui.QPushButton(self)
##        self.enter.resize(0,0)
##        self.enter.clicked.connect(self.Enter)
##        self.enter.setShortcut("Return")
## 
##        self.reload = QtGui.QPushButton("↻",self)
##        self.reload.setMinimumSize(35,30)
##        self.reload.setShortcut("F5")
##        self.reload.setStyleSheet("font-size:23px;")
##        self.reload.clicked.connect(self.Reload)
## 
##        self.back = QtGui.QPushButton("◀",self)
##        self.back.setMinimumSize(35,30)
##        self.back.setStyleSheet("font-size:23px;")
##        self.back.clicked.connect(self.Back)
## 
##        self.forw = QtGui.QPushButton("▶",self)
##        self.forw.setMinimumSize(35,30)
##        self.forw.setStyleSheet("font-size:23px;")
##        self.forw.clicked.connect(self.Forward)
## 
##        self.book = QtGui.QPushButton("☆",self)
##        self.book.setMinimumSize(35,30)
##        self.book.clicked.connect(self.Bookmark)
##        self.book.setStyleSheet("font-size:18px;")
## 
##        self.pbar = QtGui.QProgressBar()
##        self.pbar.setMaximumWidth(120)
## 
##        self.web = QWebView(loadProgress = self.pbar.setValue, loadFinished = self.pbar.hide, loadStarted = self.pbar.show, titleChanged = self.setWindowTitle)
##        self.web.setMinimumSize(1360,700)
## 
##        self.list = QtGui.QComboBox(self)
##        self.list.setMinimumSize(35,30)
## 
##        for i in bookmarks:
##            self.list.addItem(i)
## 
##        self.list.activated[str].connect(self.handleBookmarks)
##        self.list.view().setSizePolicy(QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Minimum)
## 
##        self.web.urlChanged.connect(self.UrlChanged)
##         
##        self.web.page().linkHovered.connect(self.LinkHovered)
## 
##        grid = QtGui.QGridLayout()
## 
##        grid.addWidget(self.back,0,0, 1, 1)
##        grid.addWidget(self.line,0,3, 1, 1)
##        grid.addWidget(self.book,0,4, 1, 1)
##        grid.addWidget(self.forw,0,1, 1, 1)
##        grid.addWidget(self.reload,0,2, 1, 1)
##        grid.addWidget(self.list,0,5, 1, 1)
##        grid.addWidget(self.web, 2, 0, 1, 6)
## 
##        self.centralwidget.setLayout(grid)
## 
###---------Window settings --------------------------------
## 
##        self.setGeometry(50,50,1360,768)
##        self.setWindowTitle("PySurf")
##        self.setWindowIcon(QtGui.QIcon(""))
##        self.setStyleSheet("background-color:")
##         
##        self.status = self.statusBar()
##        self.status.addPermanentWidget(self.pbar)
##        self.status.hide()
## 
##        self.setCentralWidget(self.centralwidget)
## 
##    def Enter(self):
##        global url
##        global bookmarks
##         
##        url = self.line.text()
## 
##        http = "http://"
##        www = "www."
##         
##        if www in url and http not in url:
##            url = http + url
##             
##        elif "." not in url:
##            url = "http://www.google.com/search?q="+url
##             
##        elif http in url and www not in url:
##            url = url[:7] + www + url[7:]
## 
##        elif http and www not in url:
##            url = http + www + url
## 
## 
##        self.line.setText(url)
## 
##        self.web.load(QtCore.QUrl(url))
## 
##        if url in bookmarks:
##            self.book.setText("★")
##             
##        else:
##            self.book.setText("☆")
##             
##        self.status.show()
##         
##    def Bookmark(self):
##        global url
##        global bookmarks
## 
##        bookmarks.append(url)
## 
##        b = open("bookmarks.txt","wb")
##        pickle.dump(bookmarks,b)
##        b.close()
##         
##        self.list.addItem(url)
##        self.book.setText("★")
## 
##def handleBookmarks(self,choice):
##        global url
## 
##        url = choice
##        self.line.setText(url)
##        self.Enter()
## 
##def Back(self):
##    self.web.back()
##         
##    def Forward(self):
##        self.web.forward()
## 
##    def Reload(self):
##        self.web.reload()
## 
##    def UrlChanged(self):
##        self.line.setText(self.web.url().toString())
## 
##    def LinkHovered(self,l):
##        self.status.showMessage(l)
## 
##     
## 
##def main():
##    app = QtGui.QApplication(sys.argv)
##    main= Main()
##    main.show()
## 
##    sys.exit(app.exec_())
## 
##if __name__ == "__main__":
##    main()
