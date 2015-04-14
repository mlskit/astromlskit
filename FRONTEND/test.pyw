import sys
from PyQt4 import QtGui,QtCore
import pyqtgraph as pg

import random
from numpy import *
from math import *
import numpy as np

from idleint import *
import find
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar

import warnings
warnings.filterwarnings("ignore")

####################################### all the algorithm files#######################################################################################
import naiveui,knnfront,dtreefront,forestfront,kmnfront,heirarfrontend,svmfront,linearfront,mlinearfront,ridgefront,logisticfront,dbscanfront,gmmfront
import annfront,ldafront,pcafront
import doefront1,doefront2,doefront3
import lassofront,polynomialfront,anovafront
#######################################################################################################################################################

##### a simple editor #########################
import sys
import time
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
 
var = 0
f = ""
choiceStr = ""
cs = False
wwo = False
 
tt = True
tf = True
ts = True
 
 
class Find(QtGui.QDialog):
    def __init__(self,parent = None):
        QtGui.QDialog.__init__(self, parent)
         
        self.initUI()
 
    def initUI(self):
 
        self.lb1 = QtGui.QLabel("Search for: ",self)
        self.lb1.setStyleSheet("font-size: 15px; ")
        self.lb1.move(10,10)
 
        self.te = QtGui.QTextEdit(self)
        self.te.move(10,40)
        self.te.resize(250,25)
 
        self.src = QtGui.QPushButton("Find",self)
        self.src.move(270,40)
 
        self.lb2 = QtGui.QLabel("Replace all by: ",self)
        self.lb2.setStyleSheet("font-size: 15px; ")
        self.lb2.move(10,80)
 
        self.rp = QtGui.QTextEdit(self)
        self.rp.move(10,110)
        self.rp.resize(250,25)
 
        self.rpb = QtGui.QPushButton("Replace",self)
        self.rpb.move(270,110)
 
        self.opt1 = QtGui.QCheckBox("Case sensitive",self)
        self.opt1.move(10,160)
        self.opt1.stateChanged.connect(self.CS)
         
        self.opt2 = QtGui.QCheckBox("Whole words only",self)
        self.opt2.move(10,190)
        self.opt2.stateChanged.connect(self.WWO)
 
        self.close = QtGui.QPushButton("Close",self)
        self.close.move(270,220)
        self.close.clicked.connect(self.Close)
         
         
        self.setGeometry(300,300,360,250)
 
    def CS(self, state):
        global cs
 
        if state == QtCore.Qt.Checked:
            cs = True
        else:
            cs = False
 
    def WWO(self, state):
        global wwo
        print(wwo)
 
        if state == QtCore.Qt.Checked:
            wwo = True
        else:
            wwo = False
 
    def Close(self):
        self.hide()
 
class Date(QtGui.QDialog):
    def __init__(self,parent = None):
        QtGui.QDialog.__init__(self, parent)
         
        self.initUI()
 
    def initUI(self):
 
        self.form = QtGui.QComboBox(self)
        self.form.move(10,10)
        self.form.addItem(time.strftime("%d.%m.%Y"))
        self.form.addItem(time.strftime("%A, %d. %B %Y"))
        self.form.addItem(time.strftime("%d. %B %Y"))
        self.form.addItem(time.strftime("%d %m %Y"))
        self.form.addItem(time.strftime("%X"))
        self.form.addItem(time.strftime("%x"))
        self.form.addItem(time.strftime("%H:%M"))
        self.form.addItem(time.strftime("%A, %d. %B %Y %H:%M"))
        self.form.addItem(time.strftime("%d.%m.%Y %H:%M"))
        self.form.addItem(time.strftime("%d. %B %Y %H:%M"))
 
        self.form.activated[str].connect(self.handleChoice)
         
        self.ok = QtGui.QPushButton("Insert",self)
        self.ok.move(180,10)
 
        self.cancel = QtGui.QPushButton("Cancel",self)
        self.cancel.move(180,40)
        self.cancel.clicked.connect(self.Cancel)
 
        self.setGeometry(300,300,280,70)
 
    def handleChoice(self,choice):
        global choiceStr
 
        choiceStr = choice
 
        print(choiceStr)
 
    def Cancel(self):
        self.close()
         
class Main(QtGui.QMainWindow):
 
    def __init__(self):
        QtGui.QMainWindow.__init__(self,None)
        self.initUI()
 
    def initUI(self):
 
#------- Toolbar --------------------------------------
 
#-- Upper Toolbar -- 
 
        newAction = QtGui.QAction(QtGui.QIcon("icons/new.png"),"New",self)
        newAction.setShortcut("Ctrl+N")
        newAction.setStatusTip("Create a new document from scratch.")
        newAction.triggered.connect(self.New)
 
        openAction = QtGui.QAction(QtGui.QIcon("icons/open.png"),"Open file",self)
        openAction.setStatusTip("Open existing document")
        openAction.setShortcut("Ctrl+O")
        openAction.triggered.connect(self.Open)
 
        saveAction = QtGui.QAction(QtGui.QIcon("icons/save.png"),"Save",self)
        saveAction.setStatusTip("Save document")
        saveAction.setShortcut("Ctrl+S")
        saveAction.triggered.connect(self.Save)
 
        previewAction = QtGui.QAction(QtGui.QIcon("icons/preview.png"),"Page view",self)
        previewAction.setStatusTip("Preview page before printing")
        previewAction.setShortcut("Ctrl+Shift+P")
        previewAction.triggered.connect(self.PageView)
 
        findAction = QtGui.QAction(QtGui.QIcon("icons/find.png"),"Find",self)
        findAction.setStatusTip("Find words in your document")
        findAction.setShortcut("Ctrl+F")
        findAction.triggered.connect(self.Find)
 
        cutAction = QtGui.QAction(QtGui.QIcon("icons/cut.png"),"Cut to clipboard",self)
        cutAction.setStatusTip("Delete and copy text to clipboard")
        cutAction.setShortcut("Ctrl+X")
        cutAction.triggered.connect(self.Cut)
 
        copyAction = QtGui.QAction(QtGui.QIcon("icons/copy.png"),"Copy to clipboard",self)
        copyAction.setStatusTip("Copy text to clipboard")
        copyAction.setShortcut("Ctrl+C")
        copyAction.triggered.connect(self.Copy)
 
        pasteAction = QtGui.QAction(QtGui.QIcon("icons/paste.png"),"Paste from clipboard",self)
        pasteAction.setStatusTip("Paste text from clipboard")
        pasteAction.setShortcut("Ctrl+V")
        pasteAction.triggered.connect(self.Paste)
 
        undoAction = QtGui.QAction(QtGui.QIcon("icons/undo.png"),"Undo last action",self)
        undoAction.setStatusTip("Undo last action")
        undoAction.setShortcut("Ctrl+Z")
        undoAction.triggered.connect(self.Undo)
 
        redoAction = QtGui.QAction(QtGui.QIcon("icons/redo.png"),"Redo last undone thing",self)
        redoAction.setStatusTip("Redo last undone thing")
        redoAction.setShortcut("Ctrl+Y")
        redoAction.triggered.connect(self.Redo)
 
        dtAction = QtGui.QAction(QtGui.QIcon("icons/datetime.png"),"Insert current date/time",self)
        dtAction.setStatusTip("Insert current date/time")
        dtAction.setShortcut("Ctrl+D")
        dtAction.triggered.connect(self.DateTime)
		
        wordCountAction = QtGui.QAction(QtGui.QIcon("icons/count.png"),"See word/symbol count",self)
        wordCountAction.setStatusTip("See word/symbol count")
        wordCountAction.setShortcut("Ctrl+W")
        wordCountAction.triggered.connect(self.wordCount)
         
        printAction = QtGui.QAction(QtGui.QIcon("icons/print.png"),"Print document",self)
        printAction.setStatusTip("Print document")
        printAction.setShortcut("Ctrl+P")
        printAction.triggered.connect(self.Print)
 
        self.toolbar = self.addToolBar("Options")
        self.toolbar.addAction(newAction)
        self.toolbar.addAction(openAction)
        self.toolbar.addAction(saveAction)
        self.toolbar.addSeparator()
        self.toolbar.addAction(printAction)
        #self.toolbar.addAction(pdfAction)
        self.toolbar.addAction(previewAction)
        self.toolbar.addSeparator()
        self.toolbar.addAction(findAction)
        self.toolbar.addAction(cutAction)
        self.toolbar.addAction(copyAction)
        self.toolbar.addAction(pasteAction)
        self.toolbar.addAction(undoAction)
        self.toolbar.addAction(redoAction)
        self.toolbar.addSeparator()
        self.toolbar.addAction(dtAction)
        self.toolbar.addSeparator()
        self.toolbar.addAction(wordCountAction)
 
        self.addToolBarBreak()
 
# -- Lower Toolbar -- 
 
        self.fontFamily = QtGui.QFontComboBox(self)
        self.fontFamily.currentFontChanged.connect(self.FontFamily)
 
        fontSize = QtGui.QComboBox(self)
        fontSize.setEditable(True)
        fontSize.setMinimumContentsLength(3)
        fontSize.activated.connect(self.FontSize)
        flist = [6,7,8,9,10,11,12,13,14,15,16,18,20,22,24,26,28,32,36,40,44,48,
                 54,60,66,72,80,88,96]
         
        for i in flist:
            fontSize.addItem(str(i))
 
        fontColor = QtGui.QAction(QtGui.QIcon("icons/color.png"),"Change font color",self)
        fontColor.triggered.connect(self.FontColor)
 
        boldAction = QtGui.QAction(QtGui.QIcon("icons/bold.png"),"Bold",self)
        boldAction.triggered.connect(self.Bold)
         
        italicAction = QtGui.QAction(QtGui.QIcon("icons/italic.png"),"Italic",self)
        italicAction.triggered.connect(self.Italic)
         
        underlAction = QtGui.QAction(QtGui.QIcon("icons/underline.png"),"Underline",self)
        underlAction.triggered.connect(self.Underl)
 
        alignLeft = QtGui.QAction(QtGui.QIcon("icons/alignleft.png"),"Align left",self)
        alignLeft.triggered.connect(self.alignLeft)
 
        alignCenter = QtGui.QAction(QtGui.QIcon("icons/aligncentre.png"),"Align center",self)
        alignCenter.triggered.connect(self.alignCenter)
 
        alignRight = QtGui.QAction(QtGui.QIcon("icons/alignright.png"),"Align right",self)
        alignRight.triggered.connect(self.alignRight)
 
        alignJustify = QtGui.QAction(QtGui.QIcon("icons/alignJustify.png"),"Align justify",self)
        alignJustify.triggered.connect(self.alignJustify)
 
        indentAction = QtGui.QAction(QtGui.QIcon("icons/indent.png"),"Indent Area",self)
        indentAction.setShortcut("Ctrl+Tab")
        indentAction.triggered.connect(self.Indent)
 
        dedentAction = QtGui.QAction(QtGui.QIcon("icons/dedent.png"),"Dedent Area",self)
        dedentAction.setShortcut("Shift+Tab")
        dedentAction.triggered.connect(self.Dedent)
 
        backColor = QtGui.QAction(QtGui.QIcon("icons/backcolor.png"),"Change background color",self)
        backColor.triggered.connect(self.FontBackColor)
 
        bulletAction = QtGui.QAction(QtGui.QIcon("icons/bullet.png"),"Insert Bullet List",self)
        bulletAction.triggered.connect(self.BulletList)
 
        numberedAction = QtGui.QAction(QtGui.QIcon("icons/number.png"),"Insert Numbered List",self)
        numberedAction.triggered.connect(self.NumberedList)
 
        space1 = QtGui.QLabel("  ",self)
        space2 = QtGui.QLabel(" ",self)
        space3 = QtGui.QLabel(" ",self)
         
 
        self.formatbar = self.addToolBar("Format")
        self.formatbar.addWidget(self.fontFamily)
        self.formatbar.addWidget(space1)
        self.formatbar.addWidget(fontSize)
        self.formatbar.addWidget(space2)
         
        self.formatbar.addSeparator()
 
        self.formatbar.addAction(fontColor)
        self.formatbar.addAction(backColor)
 
        self.formatbar.addSeparator()
         
        self.formatbar.addAction(boldAction)
        self.formatbar.addAction(italicAction)
        self.formatbar.addAction(underlAction)
         
        self.formatbar.addSeparator()
 
        self.formatbar.addAction(alignLeft)
        self.formatbar.addAction(alignCenter)
        self.formatbar.addAction(alignRight)
        self.formatbar.addAction(alignJustify)
 
        self.formatbar.addSeparator()
 
        self.formatbar.addAction(indentAction)
        self.formatbar.addAction(dedentAction)
        self.formatbar.addAction(bulletAction)
        self.formatbar.addAction(numberedAction)
         
#------- Text Edit -----------------------------------
 
        self.text = QtGui.QTextEdit(self)
        self.text.setTabStopWidth(12)
        self.setCentralWidget(self.text)
 
#------- Statusbar ------------------------------------
         
        self.status = self.statusBar()
 
        self.text.cursorPositionChanged.connect(self.CursorPosition)
 
 
#---------Window settings --------------------------------
         
        self.setGeometry(100,100,700,700)
        self.setWindowTitle("Editor v 1.0")
        self.setWindowIcon(QtGui.QIcon("icons/feather.png"))
        self.show()
 
#------- Menubar --------------------------------------
         
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        view = menubar.addMenu("View")
 
        file.addAction(newAction)
        file.addAction(openAction)
        file.addAction(saveAction)
        file.addAction(printAction)
        file.addAction(previewAction)
 
        edit.addAction(undoAction)
        edit.addAction(redoAction)
        edit.addAction(cutAction)
        edit.addAction(copyAction)
        edit.addAction(findAction)
        edit.addAction(dtAction)
 
        toggleTool = QtGui.QAction("Toggle Toolbar",self,checkable=True)
        toggleTool.triggered.connect(self.handleToggleTool)
         
        toggleFormat = QtGui.QAction("Toggle Formatbar",self,checkable=True)
        toggleFormat.triggered.connect(self.handleToggleFormat)
         
        toggleStatus = QtGui.QAction("Toggle Statusbar",self,checkable=True)
        toggleStatus.triggered.connect(self.handleToggleStatus)
 
        view.addAction(toggleTool)
        view.addAction(toggleFormat)
        view.addAction(toggleStatus)
 
    def handleToggleTool(self):
        global tt
 
        if tt == True:
            self.toolbar.hide()
            tt = False
        else:
            self.toolbar.show()
            tt = True
 
    def handleToggleFormat(self):
        global tf
 
        if tf == True:
            self.formatbar.hide()
            tf = False
        else:
            self.formatbar.show()
            tf = True
 
    def handleToggleStatus(self):
        global ts
 
        if ts == True:
            self.status.hide()
            ts = False
        else:
            self.status.show()
            ts = True
             
#-------- Toolbar slots -----------------------------------
 
    def New(self):
        self.text.clear()
 
    def Open(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        f = open(filename, 'r')
        filedata = f.read()
        self.text.setText(filedata)
        f.close()
 
    def Save(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        f = open(filename, 'w')
        filedata = self.text.toPlainText()
        f.write(filedata)
        f.close()
 
    def PageView(self):
        preview = QtGui.QPrintPreviewDialog()
        preview.paintRequested.connect(self.PaintPageView)
        preview.exec_()
 
    def Print(self):
        dialog = QtGui.QPrintDialog()
        if dialog.exec_() == QtGui.QDialog.Accepted:
            self.text.document().print_(dialog.printer())
 
    def PDF(self):
        printer = QtGui.QPrinter()
        printer.setOutputFormat(printer.NativeFormat)
         
        dialog = QtGui.QPrintDialog(printer)
        dialog.setOption(dialog.PrintToFile)
        if dialog.exec_() == QtGui.QDialog.Accepted:
            self.text.document().print_(dialog.printer())
         
         
    def PaintPageView(self, printer):
        self.text.print_(printer)
 
    def Find(self):
        global f
         
        find = Find(self)
        find.show()
 
        def handleFind():
 
            f = find.te.toPlainText()
            print(f)
             
            if cs == True and wwo == False:
                flag = QtGui.QTextDocument.FindBackward and QtGui.QTextDocument.FindCaseSensitively
                 
            elif cs == False and wwo == False:
                flag = QtGui.QTextDocument.FindBackward
                 
            elif cs == False and wwo == True:
                flag = QtGui.QTextDocument.FindBackward and QtGui.QTextDocument.FindWholeWords
                 
            elif cs == True and wwo == True:
                flag = QtGui.QTextDocument.FindBackward and QtGui.QTextDocument.FindCaseSensitively and QtGui.QTextDocument.FindWholeWords
             
            self.text.find(f,flag)
 
        def handleReplace():
            f = find.te.toPlainText()
            r = find.rp.toPlainText()
 
            text = self.text.toPlainText()
             
            newText = text.replace(f,r)
 
            self.text.clear()
            self.text.append(newText)
         
        find.src.clicked.connect(handleFind)
        find.rpb.clicked.connect(handleReplace)
 
 
    def Undo(self):
        self.text.undo()
 
    def Redo(self):
        self.text.redo()
 
    def Cut(self):
        self.text.cut()
 
    def Copy(self):
        self.text.copy()
 
    def Paste(self):
        self.text.paste()
 
    def DateTime(self):
 
        date = Date(self)
        date.show()
 
        date.ok.clicked.connect(self.insertDate)
 
    def insertDate(self):
        global choiceStr
        print(choiceStr)
        self.text.append(choiceStr)
         
    def CursorPosition(self):
        line = self.text.textCursor().blockNumber()
        col = self.text.textCursor().columnNumber()
        linecol = ("Line: "+str(line)+" | "+"Column: "+str(col))
        self.status.showMessage(linecol)
	
    def wordCount(self):
        wc = wordcount.WordCount(self)
        wc.getText()
        wc.show()
 
    def FontFamily(self,font):
        font = QtGui.QFont(self.fontFamily.currentFont())
        self.text.setCurrentFont(font)
 
    def FontSize(self, fsize):
        size = (int(fsize))
        self.text.setFontPointSize(size)
 
    def FontColor(self):
        c = QtGui.QColorDialog.getColor()
 
        self.text.setTextColor(c)
         
    def FontBackColor(self):
        c = QtGui.QColorDialog.getColor()
 
        self.text.setTextBackgroundColor(c)
 
    def Bold(self):
        w = self.text.fontWeight()
        if w == 50:
            self.text.setFontWeight(QtGui.QFont.Bold)
        elif w == 75:
            self.text.setFontWeight(QtGui.QFont.Normal)
         
    def Italic(self):
        i = self.text.fontItalic()
         
        if i == False:
            self.text.setFontItalic(True)
        elif i == True:
            self.text.setFontItalic(False)
         
    def Underl(self):
        ul = self.text.fontUnderline()
 
        if ul == False:
            self.text.setFontUnderline(True) 
        elif ul == True:
            self.text.setFontUnderline(False)
             
    def lThrough(self):
        lt = QtGui.QFont.style()
 
        print(lt)
 
    def alignLeft(self):
        self.text.setAlignment(Qt.AlignLeft)
 
    def alignRight(self):
        self.text.setAlignment(Qt.AlignRight)
 
    def alignCenter(self):
        self.text.setAlignment(Qt.AlignCenter)
 
    def alignJustify(self):
        self.text.setAlignment(Qt.AlignJustify)
 
    def Indent(self):
        tab = "\t"
        cursor = self.text.textCursor()
 
        start = cursor.selectionStart()
        end = cursor.selectionEnd()
 
        cursor.setPosition(end)
        cursor.movePosition(cursor.EndOfLine)
        end = cursor.position()
 
        cursor.setPosition(start)
        cursor.movePosition(cursor.StartOfLine)
        start = cursor.position()
 
 
        while cursor.position() < end:
            global var
 
            print(cursor.position(),end)
             
            cursor.movePosition(cursor.StartOfLine)
            cursor.insertText(tab)
            cursor.movePosition(cursor.Down)
            end += len(tab)
 
            '''if cursor.position() == end:
                var +=1
 
            if var == 2:
                break'''
             
             
 
    def Dedent(self):
        tab = "\t"
        cursor = self.text.textCursor()
 
        start = cursor.selectionStart()
        end = cursor.selectionEnd()
 
        cursor.setPosition(end)
        cursor.movePosition(cursor.EndOfLine)
        end = cursor.position()
 
        cursor.setPosition(start)
        cursor.movePosition(cursor.StartOfLine)
        start = cursor.position()
 
 
        while cursor.position() < end:
            global var
             
            cursor.movePosition(cursor.StartOfLine)
            cursor.deleteChar()
            cursor.movePosition(cursor.EndOfLine)
            cursor.movePosition(cursor.Down)
            end -= len(tab)
 
            '''if cursor.position() == end:
                var +=1
 
            if var == 2:
                break'''
 
    def BulletList(self):
        print("bullet connects!")
        self.text.insertHtml("<ul><li> ...</li></ul>")
 
    def NumberedList(self):
        print("numbered connects!")
        self.text.insertHtml("<ol><li> ...</li></ol>")
          
 







###############################################################
###########ditributions########################################
###############################################################
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
        
   ########################################################################################################################################################         

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



########################################################################################################################################################
          
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
#################################################################################

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
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QtGui.QCheckBox')
        self.show()
        
    def changeTitle(self, state):
      
        if state == QtCore.Qt.Checked:
            self.setWindowTitle('QtGui.QCheckBox')
        else:
            self.setWindowTitle('')
################################################################################
####   classes for each format                                          ########
################################################################################
class nbmain(QtGui.QMainWindow):
        def __init__(self):
                super(nbmain, self).__init__()
                self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
                self.ui = naiveui.Ui_Form()
                self.ui.setupUi(self)
                
class pcamain(QtGui.QMainWindow):
        def __init__(self):
                super(pcamain, self).__init__()
                self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
                self.ui = pcafront.Ui_Form()
                self.ui.setupUi(self)

class knnmain(QtGui.QMainWindow):
        def __init__(self):
                super(knnmain, self).__init__()
                self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
                self.ui = knnfront.Ui_Form()
                self.ui.setupUi(self)
                
class dtreemain(QtGui.QMainWindow):
        def __init__(self):
                super(dtreemain, self).__init__()
                self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
                self.ui = dtreefront.Ui_Form()
                self.ui.setupUi(self)
                
class forestmain(QtGui.QMainWindow):
        def __init__(self):
                super(forestmain, self).__init__()
                self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
                self.ui = forestfront.Ui_RandomForest()
                self.ui.setupUi(self)
                
class svmmain(QtGui.QMainWindow):
        def __init__(self):
                super(svmmain, self).__init__()
                self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
                self.ui = svmfront.Ui_Form()
                self.ui.setupUi(self)
                
class lrlmain(QtGui.QMainWindow):
        def __init__(self):
                super(lrlmain, self).__init__()
                self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
                self.ui = logisticfront.Ui_Form()
                self.ui.setupUi(self)
                
class annmain(QtGui.QMainWindow):
        def __init__(self):
                super(annmain, self).__init__()
                self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
                self.ui = annfront.Ui_ANN()
                self.ui.setupUi(self)
class ldamain(QtGui.QMainWindow):
        def __init__(self):
                super(ldamain, self).__init__()
                self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
                self.ui = ldafront.Ui_Form()
                self.ui.setupUi(self)

##################################################################################################
################### Cluster UI mains #############################################################
##################################################################################################
                
class kmeansmain(QtGui.QMainWindow):
        def __init__(self):
                super(kmeansmain, self).__init__()
                self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
                self.ui = kmnfront.Ui_Form()
                self.ui.setupUi(self)

class hmain(QtGui.QMainWindow):
        def __init__(self):
                super(hmain, self).__init__()
                self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
                self.ui = heirarfrontend.Ui_Form()
                self.ui.setupUi(self)

class dbmain(QtGui.QMainWindow):
        def __init__(self):
                super(dbmain, self).__init__()
                self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
                self.ui = dbscanfront.Ui_Form()
                self.ui.setupUi(self)
class gmmmain(QtGui.QMainWindow):
        def __init__(self):
                super(gmmmain, self).__init__()
                self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
                self.ui = gmmfront.Ui_Form()
                self.ui.setupUi(self)


class editormain(QtGui.QMainWindow):
        def __init__(self):
                super(editormain, self).__init__()
                self.ui = Main()

####################################################
#######################DOE##########################
####################################################

class doefront1main(QtGui.QMainWindow):
        def __init__(self):
                super(doefront1main, self).__init__()
                self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
                self.ui = doefront1.Ui_Form()
                self.ui.setupUi(self)
class doefront2main(QtGui.QMainWindow):
        def __init__(self):
                super(doefront2main, self).__init__()
                self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
                self.ui = doefront2.Ui_Form()
                self.ui.setupUi(self)
class doefront3main(QtGui.QMainWindow):
        def __init__(self):
                super(doefront3main, self).__init__()
                self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
                self.ui = doefront3.Ui_Form()
                self.ui.setupUi(self)



                

############################################################################################
############################ Regressions Main Classes for UI ###############################
############################################################################################
                
class linearmain(QtGui.QMainWindow):
        def __init__(self):
                super(linearmain, self).__init__()
                self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
                self.ui = linearfront.Ui_SimpleLinear()
                self.ui.setupUi(self)

class mlinearmain(QtGui.QMainWindow):
        def __init__(self):
                super(mlinearmain, self).__init__()
                self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
                self.ui = mlinearfront.Ui_Form()
                self.ui.setupUi(self)


class ridgemain(QtGui.QMainWindow):
        def __init__(self):
                super(ridgemain, self).__init__()
                self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
                self.ui = ridgefront.Ui_Ridge()
                self.ui.setupUi(self)
                
class lassomain(QtGui.QMainWindow):
        def __init__(self):
                super(lassomain, self).__init__()
                self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
                self.ui = lassofront.Ui_Form()
                self.ui.setupUi(self)
        
        
class polymain(QtGui.QMainWindow):
        def __init__(self):
                super(polymain, self).__init__()
                self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
                self.ui = polynomialfront.Ui_Form()
                self.ui.setupUi(self)
        
class anovamain(QtGui.QMainWindow):
        def __init__(self):
                super(anovamain, self).__init__()
                self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
                self.ui = anovafront.Ui_Form()
                self.ui.setupUi(self)

##############################################################################################################################
######################   main function class #################################################################################
##############################################################################################################################
                
class App(QtGui.QMainWindow):
    
    def __init__(self):
        super(App, self).__init__()
        self.win = MyInterpreter(None)
        self.setCentralWidget(self.win)
        #self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.initUI()

    def scatter(self):
        self.w= visuals()
        self.w.draw()

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
        self.w51=ldamain()
        self.w51.show()

    def flrl(self):
        self.w17=lrlmain()
        self.w17.show()

    def fsvm(self):
        self.w7=svmmain()
        self.w7.show()    
        
    def fann(self):
        self.w8=annmain()
        self.w8.show()

    def fkmeans(self):
        self.w9=kmeansmain()
        self.w9.show()    
        
    def fdbscna(self):
        pass

    def fpoly(self):
        print "polymain"
        self.w30=polymain()
        self.w30.show()

    def fhierarchy(self):
        self.w11=hmain()
        print "showing\n"
        self.w11.show()

    def fanova(self):
        self.w333=anovamain()
        self.w333.show()
        
    def fgmm(self):
        self.w20=gmmmain()
        self.w20.show()
        
    def fpca(self):
        self.w211=pcamain()
        self.w211.show()

    def fgsa(self):
        pass

    def flinear(self):
        self.w15=linearmain()
        self.w15.show()

    def fmlinear(self):
        self.w16=mlinearmain()
        self.w16.show()

    def fridge(self):
        self.w17=ridgemain()
        self.w17.show()

    def flasso(self):
        self.w18=lassomain()
        self.w18.show()

    def fdb(self):
        self.w19=dbmain()
        self.w19.show()
        
    def editdisp(self):
        self.main= editormain()
        self.main.show()
    def ffront1(self):
        self.w900=doefront1main()
        self.w900.show()
    def ffront2(self):
        self.w901=doefront2main()
        self.w901.show()
    def ffront3(self):
        self.w902=doefront3main()
        self.w902.show()
        
    
    def gitcall(self):
        import subprocess
        subprocess.Popen(['C:\\Program Files (x86)\\Git\\bin\\wish.exe','C:\\Program Files (x86)\\Git\\libexec\\git-core\\git-gui'])
    def browsecall(self):
        import subprocess
        subprocess.Popen(['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'])
    
    def initUI(self):               

        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)
        #nbaction=QtGui.QAction(QtGui.QIcon('nb.png'),'Naive Bayes',self.fnb)

        
        self.statusBar()    
        cut = QtGui.QAction(QtGui.QIcon("icons/nb.png"),"Naive bayes",self)
        cut.setStatusTip("Delete and copy text to clipboard")
        cut.setShortcut("Ctrl+X")
        cut.triggered.connect(self.fnb)


        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Classification')
        fileMenu.addAction(cut)
        fileMenu.addAction('K- Nearest Neighbors',self.fknn)
        fileMenu.addAction('Decision tree',self.fdtree)
        fileMenu.addAction('Random Forest',self.fforest)
        fileMenu.addAction('LDA classifier',self.flda)
        fileMenu.addAction('Logistic regression learner',self.flrl)
        fileMenu.addAction('SVM',self.fsvm)
        fileMenu.addAction('A-Neural-nets',self.fann)
        

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Regression')
        fileMenu.addAction('Linear Regression',self.flinear)
        fileMenu.addAction('Multiple Regression',self.fmlinear)
        fileMenu.addAction('Lasso',self.flasso)
        fileMenu.addAction('Ridge',self.fridge)
        fileMenu.addAction('Curvilinear',self.fpoly)
        


        menubar = self.menuBar()
        fileMenu1 = menubar.addMenu('&Unsupervised Clustering')
        #fileMenu1 = fileMenu.addMenu('Dumb')
        fileMenu1.addAction('K-Means',self.fkmeans)
        fileMenu1.addAction('Dbscan',self.fdb)        
        fileMenu1.addAction('Hierarchial',self.fhierarchy)
        fileMenu1.addAction('Gausiann Mixture',self.fgmm)
        fileMenu1.addAction('PCA',self.fpca)
        fileMenu1.addAction('Gravitational clustering',self.Scat)
    
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Visualisation')
        fileMenu.addAction('Scatter Plots',self.scatter)
        fileMenu.addAction('Dendograms',self.testme)
        #fileMenu.addAction('Biplots',self.testme)
        fileMenu.addAction('Andrew Plots',self.testme)
        #fileMenu.addAction('Glyph Plots',self.testme)
        fileMenu.addAction('Heat Maps',self.testme)
        fileMenu.addAction('Radviz',self.testme)
        #fileMenu.addAction('polyviz',self.testme)
        fileMenu.addAction('Sieve Multigram',self.testme)
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Evaluation Metrics')
        fileMenu.addAction('Confusion matrix',self.testme)
        fileMenu.addAction('ROC analysis',self.testme)
        fileMenu.addAction('Calibration plot',self.testme)
        fileMenu.addAction('Test Learners',self.testme)
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&DOE')
        fileMenu.addAction('Full factorial',self.ffront1)
        fileMenu.addAction('2-L-Fullfactorial',self.ffront2)
        fileMenu.addAction('Fractional factorial',self.ffront3)
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Tests')
        fileMenu.addAction('ANOVA',self.fanova)
        fileMenu.addAction('ARIMA',self.testme)
        fileMenu.addAction('chi-2',self.testme)
        fileMenu.addAction('P-test',self.testme)
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Distribution')
        fileMenu.addAction('All-in-one',self.dist)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Markov Sampling')
        fileMenu.addAction('Metropolis Hastings',self.testme)
        fileMenu.addAction('Slice Sampling',self.testme)
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Extra-Features')
        fileMenu.addAction('Editor',self.editdisp)
        fileMenu.addAction('Browser',self.browsecall)
        fileMenu.addAction('Git',self.gitcall)
        fileMenu.addAction('G-Drive',self.testme)
        
        #self.setGeometry(100, 100, 700, 600)
        self.showMaximized()
        self.setWindowTitle('MLSKit V 1.0')
        self.layout = QVBoxLayout(self)
        self.show()        

def splashscreen(app):
        import sys,time
        splash_pix = QPixmap('conti1.png')
        splash = QSplashScreen(splash_pix)
        progressBar = QProgressBar(splash)
        progressBar.setGeometry(splash.width()*0.2, splash.height()*0.95,splash.width()*0.8, splash.height()/25.0)

        splash.setMask(splash_pix.mask())


        splash.show()
        for i in range(0, 101):
            progressBar.setValue(i)
            t = time.time()
            while time.time() < t + 0:
               app.processEvents()

        # Simulate something that takes time
        time.sleep(1)
    
def main():
    import sys,time
    
    app = QtGui.QApplication(sys.argv)
    splashscreen(app)
    app.setStyle('plastique')
    ex = App()
    #splash.finish(App)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main() 
