#! /usr/bin/env python
import sys
#from PyQt4.QtGui import *
import PyQt4.QtGui as qtgui

class MainWindow(qtgui.QWidget):
	layout_main_vert = None
	label_lineedit= []
	submit = None

	def __init__(self):
		super(MainWindow, self).__init__()
		self.label_lineedit= []

		self.setGeometry(300,300,250,150)
		self.setWindowTitle("Dis Window Title")

		self.layout_main_vert = qtgui.QVBoxLayout()
		self.submit = qtgui.QPushButton("Submit!")
		self.submit.clicked.connect(self.debug)
		self.initUI()	

	def initUI(self):
		self.addLine("One", "dues")
		self.layout_main_vert.addWidget(self.submit)
		self.setLayout(self.layout_main_vert)
		self.show()

	def addLine(self, label_text, lineedit_text):
		temp_layout_hz = qtgui.QHBoxLayout()
		temp_label = qtgui.QLabel(label_text)
		temp_lineedit = qtgui.QLineEdit(lineedit_text)
		temp_layout_hz.addWidget(temp_label)
		temp_layout_hz.addWidget(temp_lineedit)
	
		self.layout_main_vert.addLayout(temp_layout_hz)
	
	def debug(self):
		self.addLine("Hello", "World!")
		print("FLAGGED!")
	

a = qtgui.QApplication(sys.argv)
window = MainWindow()
sys.exit(a.exec_())
